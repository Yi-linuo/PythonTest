package demo01;

public class Constant {
    public static void main(String[] args) {
        //整数常量
        System.out.println(1);
        System.out.println(-1);

        //小数常量 带小数点的
        System.out.println(1.0);

        //字符常量 单引号中有且只有一个内容  '11'不行
        System.out.println('1');
        System.out.println(' ');//一个空格也算一个内容
        //System.out.println('    '); 多个空格算多个内容,不行

        //字符串常量
        System.out.println("字符串常量");
        System.out.println("");//""内容可为空

        //布尔常量
        System.out.println(true);
        System.out.println(false);

        //空常量 null
        //System.out.println(null);不能直接使用

        //常量间的运算
        System.out.println(10-3);//7
        System.out.println(10+3);//13
        System.out.println(10*3);//30
        /*
        前后如果都是整数,结果就只取整数部分

        前后只要有一个带小数点,结果就会是小数
         */
        System.out.println(10/3);//3
        System.out.println(10.0/3);//3.3333
    }
}
