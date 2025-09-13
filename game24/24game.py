import itertools
import random
import re


# 扑克牌符号映射
def card_to_symbol(card):
    """将数字转换为扑克牌符号"""
    if card == 1:
        return 'A'
    elif card == 11:
        return 'J'
    elif card == 12:
        return 'Q'
    elif card == 13:
        return 'K'
    else:
        return str(card)


def symbol_to_card(symbol):
    """将扑克牌符号转换为数字"""
    symbol = symbol.upper()
    # 转换成大写字母
    if symbol == 'A':
        return 1
    elif symbol == 'J':
        return 11
    elif symbol == 'Q':
        return 12
    elif symbol == 'K':
        return 13
    else:
        try:
            value = int(symbol)
            if 1 <= value <= 13:
                return value
            else:
                return None
        except ValueError:
            return None


def convert_expression(expr):
    """将表达式中的数字转换为扑克牌符号"""
    # 先替换双位数（11,12,13）
    expr = expr.replace('13', 'K')
    expr = expr.replace('12', 'Q')
    expr = expr.replace('11', 'J')
    # 使用正则表达式替换单独的1
    expr = re.sub(r'\b1\b', 'A', expr)
    return expr


def generate_expressions(nums):
    """生成所有可能的四则运算表达式"""
    op_combinations = itertools.product(['+', '-', '*', '/'], repeat=3)
    expressions = []

    # 扩展的括号组合结构（增加更多可能的结构）
    structures = [
        # 原有结构
        "({} {} ({} {} {})) {} {}",  # a op1 (b op2 c) op3 d
        "(({} {} {}) {} {}) {} {}",  # (a op1 b) op2 c op3 d
        "(({} {} {}) {} ({} {} {}))",  # (a op1 b) op2 (c op3 d)
        "({} {} {}) {} ({} {} {})",  # a op1 b op2 (c op3 d)
        "{} {} ({} {} ({} {} {}))",  # a op1 (b op2 (c op3 d))

        # 新增结构
        "{} {} ({} {} {}) {} {}",  # a op1 (b op2 c) op3 d (无外层括号)
        "({} {} {}) {} {} {}",  # (a op1 b) op2 c op3 d (无外层括号)
        "{} {} {} ({} {} {})",  # a op1 b op2 (c op3 d) (无外层括号)
        "({} {} {} {} {})",  # (a op1 b op2 c) op3 d
        "{} {} {} {} {}",  # a op1 b op2 c op3 d (无括号)

        # 特别针对 8/(3-8/3) 的结构
        "{} / ({} - {} / {})",  # a / (b - c / d)
        "{} / ({} - ({} / {}))",  # a / (b - (c / d))
    ]

    # 遍历所有排列和运算符组合
    for perm in itertools.permutations(nums):
        a, b, c, d = [str(x) for x in perm]
        for ops in op_combinations:
            op1, op2, op3 = ops
            for struct in structures:
                expr = struct.format(a, op1, b, op2, c, op3, d)
                expressions.append(expr)
    return expressions


def evaluate_expression(expr):
    """安全评估表达式，处理除零错误"""
    try:
        result = eval(expr)
        return abs(result - 24) < 1e-6  # 处理浮点精度问题
    except ZeroDivisionError:
        return False


def get_user_input():
    """获取用户输入的牌组"""
    while True:
        print("\n请输入四张扑克牌，用空格分隔")
        print("可用格式: A(1), 2-10, J(11), Q(12), K(13)")
        print("例如: A 5 8 Q 或 1 5 8 12")

        user_input = input("您的牌组: ").strip().split()

        if len(user_input) != 4:
            print("错误: 请输入四张牌")
            continue

        cards = []
        valid = True

        for symbol in user_input:
            card = symbol_to_card(symbol)
            if card is None:
                print(f"错误: '{symbol}' 不是有效的扑克牌")
                valid = False
                break
            cards.append(card)

        if valid:
            return cards


def play_24_game():
    """主游戏逻辑"""
    print("=" * 5, "24点游戏", "=" * 5)

    # 选择输入方式
    while True:
        print("请选择输入方式:")
        print("1. 随机生成牌组")
        print("2. 手动输入牌组")
        choice = input("请输入选择 (1 或 2): ").strip()

        if choice == '1':
            cards = [random.randint(1, 13) for _ in range(4)]
            break
        elif choice == '2':
            cards = get_user_input()
            break
        else:
            print("无效选择，请重新输入")

    # 显示牌组
    card_symbols = [card_to_symbol(c) for c in cards]
    print(f"\n您的牌组: {card_symbols} [数值: {cards}]")

    # 生成所有表达式并检查结果
    solutions = set()
    for expr in generate_expressions(cards):
        if evaluate_expression(expr):
            # 转换表达式为扑克牌符号
            converted_expr = convert_expression(expr)
            solutions.add(converted_expr)

    # 输出结果
    if solutions:
        print(f"\n找到 {len(solutions)} 种解法:")
        for i, sol in enumerate(solutions, 1):
            print(f"{i}. {sol} = 24")
    else:
        print(f"\n牌组 {card_symbols} 无法组成24点")

    # 询问是否继续
    while True:
        again = input("\n是否继续游戏? (y/n): ").strip().lower()
        if again == 'y':
            play_24_game()
            break
        elif again == 'n':
            print("游戏结束，谢谢游玩!")
            break
        else:
            print("请输入 y 或 n")


if __name__ == "__main__":
    play_24_game()