import itertools
import random
import re


class TwentyFourGame:
    def __init__(self):
        self.card_map = {
            'A': 1, 'J': 11, 'Q': 12, 'K': 13,
            '1': 1, '11': 11, '12': 12, '13': 13
        }
        self.operations = ['+', '-', '*', '/']

    def parse_cards(self, cards_input):
        """解析输入的扑克牌"""
        cards = []
        for card in cards_input:
            if card.upper() in self.card_map:
                cards.append(self.card_map[card.upper()])
            else:
                try:
                    cards.append(int(card))
                except ValueError:
                    raise ValueError(f"无效的扑克牌: {card}")
        return cards

    def generate_random_cards(self):
        """生成随机四张牌"""
        cards = [random.randint(1, 13) for _ in range(4)]
        return cards

    def card_to_display(self, card_value):
        """将卡牌值转换为显示格式"""
        if card_value == 1:
            return 'A'
        elif card_value == 11:
            return 'J'
        elif card_value == 12:
            return 'Q'
        elif card_value == 13:
            return 'K'
        else:
            return str(card_value)

    def evaluate_expression(self, expression):
        """安全地计算表达式值"""
        try:
            # 使用浮点数避免整数除法问题
            return eval(expression)
        except ZeroDivisionError:
            return None

    def is_valid_expression(self, expression, target=24):
        """检查表达式是否等于目标值"""
        result = self.evaluate_expression(expression)
        return result is not None and abs(result - target) < 1e-6

    def normalize_expression(self, expression):
        """规范化表达式以便比较重复"""
        # 移除多余空格
        expression = expression.replace(' ', '')

        # 标准化乘法和除法符号
        expression = expression.replace('×', '*').replace('÷', '/')

        return expression

    def generate_expressions(self, cards):
        """生成所有可能的表达式"""
        expressions = set()
        n = len(cards)

        # 所有数字排列
        for num_perm in itertools.permutations(cards):
            # 所有运算符组合
            for ops in itertools.product(self.operations, repeat=n - 1):
                # 尝试不同的括号位置
                patterns = [
                    # (a op b) op c op d
                    "({}{}{}){}{}{}{}",
                    # a op (b op c) op d
                    "{}{}({}{}{}){}{}",
                    # a op b op (c op d)
                    "{}{}{}{}({}{}{})",
                    # (a op b op c) op d
                    "({}{}{}{}{}){}{}",
                    # a op (b op c op d)
                    "{}{}({}{}{}{}{})",
                    # (a op b) op (c op d)
                    "({}{}{}){}({}{}{})",
                    # a op b op c op d (无括号)
                    "{}{}{}{}{}{}{}"
                ]

                for pattern in patterns:
                    try:
                        # 构建表达式
                        expr = pattern.format(
                            num_perm[0], ops[0], num_perm[1], ops[1],
                            num_perm[2], ops[2], num_perm[3]
                        )

                        # 检查表达式是否有效
                        if self.is_valid_expression(expr):
                            # 规范化并存储表达式
                            normalized = self.normalize_expression(expr)
                            expressions.add(normalized)
                    except:
                        continue

        return expressions

    def play_random_mode(self):
        """随机模式游戏"""
        cards = self.generate_random_cards()
        card_display = [self.card_to_display(card) for card in cards]
        print(f"随机抽取的扑克牌: {', '.join(card_display)}")

        solutions = self.generate_expressions(cards)

        if solutions:
            print(f"找到 {len(solutions)} 种解法:")
            for i, solution in enumerate(solutions, 1):
                # 将表达式中的数字转换回扑克牌显示格式
                display_solution = solution
                for num in cards:
                    display_solution = display_solution.replace(
                        str(num), self.card_to_display(num)
                    )
                print(f"{i}. {display_solution}")
        else:
            print("没有找到解法!")

        return cards, solutions

    def play_manual_mode(self):
        """手动输入模式游戏"""
        while True:
            try:
                input_str = input("请输入四张扑克牌(用空格分隔, 如: A 2 3 4): ")
                cards_input = input_str.split()

                if len(cards_input) != 4:
                    print("请输入恰好四张扑克牌!")
                    continue

                cards = self.parse_cards(cards_input)
                break
            except ValueError as e:
                print(e)

        card_display = [self.card_to_display(card) for card in cards]
        print(f"您输入的扑克牌: {', '.join(card_display)}")

        solutions = self.generate_expressions(cards)

        if solutions:
            print(f"找到 {len(solutions)} 种解法:")
            for i, solution in enumerate(solutions, 1):
                # 将表达式中的数字转换回扑克牌显示格式
                display_solution = solution
                for num in cards:
                    display_solution = display_solution.replace(
                        str(num), self.card_to_display(num)
                    )
                print(f"{i}. {display_solution}")
        else:
            print("没有找到解法!")

        return cards, solutions


# 单元测试
import unittest


class TestTwentyFourGame(unittest.TestCase):
    def setUp(self):
        self.game = TwentyFourGame()

    def test_parse_cards(self):
        self.assertEqual(self.game.parse_cards(['A', '2', 'J', 'Q']), [1, 2, 11, 12])
        self.assertEqual(self.game.parse_cards(['1', '11', '12', '13']), [1, 11, 12, 13])
        self.assertEqual(self.game.parse_cards(['10', '4', '3', '6']), [10, 4, 3, 6])

    def test_card_to_display(self):
        self.assertEqual(self.game.card_to_display(1), 'A')
        self.assertEqual(self.game.card_to_display(11), 'J')
        self.assertEqual(self.game.card_to_display(12), 'Q')
        self.assertEqual(self.game.card_to_display(13), 'K')
        self.assertEqual(self.game.card_to_display(5), '5')

    def test_is_valid_expression(self):
        self.assertTrue(self.game.is_valid_expression('(6-2)*(8-2)'))  # 4*6=24
        self.assertTrue(self.game.is_valid_expression('(13-1)*(3-1)'))  # 12*2=24
        self.assertFalse(self.game.is_valid_expression('1+1+1+1'))  # 4≠24
        self.assertFalse(self.game.is_valid_expression('1/0'))  # 除零错误

    def test_normalize_expression(self):
        expr1 = self.game.normalize_expression('(1 + 2) * 3 / 4')
        expr2 = self.game.normalize_expression('(1+2)*3/4')
        self.assertEqual(expr1, expr2)

    def test_generate_expressions(self):
        # 测试一个简单的情况：6/(1-3/4)=24
        solutions = self.game.generate_expressions([6, 1, 3, 4])
        self.assertGreater(len(solutions), 0)

        # 测试一个无解的情况
        solutions = self.game.generate_expressions([1, 1, 1, 1])
        self.assertEqual(len(solutions), 0)


def main():
    game = TwentyFourGame()

    while True:
        print("\n=== 24点游戏 ===")
        print("1. 随机抽取四张牌")
        print("2. 手动输入四张牌")
        print("3. 运行单元测试")
        print("4. 退出")

        choice = input("请选择操作 (1/2/3/4): ")

        if choice == '1':
            game.play_random_mode()
        elif choice == '2':
            game.play_manual_mode()
        elif choice == '3':
            print("运行单元测试...")
            unittest.main(exit=False, verbosity=2)
        elif choice == '4':
            print("谢谢游玩!")
            break
        else:
            print("无效选择，请重新输入!")


if __name__ == "__main__":
    # 不再自动运行测试，而是提供选项
    main()