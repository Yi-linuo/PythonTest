package demo01;
    /*
        变量的数据类型
            1.基本数据类型:整型(int byte short long)
                          浮点型(float double)
                          字符型(char)
                          布尔型(boolean)
            2.引用数据类型:类 数组 接口 枚举 注解
 */
public class var_definition {
    public static void main(String[] args) {
        //byte
        byte num1 = 100;
        System.out.println(num1);

        //int 整数的默认类型
        int num2 = 13;
        num2 = 20;
        System.out.println(num2);

        //short
        short num3 = 980;
        System.out.println(num3);

        //long 定义的变量后面加L
        long num4 = 1000000L;
        System.out.println(num4);

        /*
            float和double实际开发之中不要直接参加运算
            直接参与运算会有精度损失问题
         */

        //float 定义的变量后面加F 单精度 表示7位小数
        float num5 = 2.5F;
        System.out.println(num5);

        //double 小数的默认类型 双精度 表示16位小数
        double num6 = 3.4;
        System.out.println(num6);

        //char
        char num7 = 'a';
        System.out.println(num7);

        //boolean
        boolean num8 = false;
        boolean num9 = true;
        num9 = num8;//等号右边赋值给左边
        System.out.println(num9);//false


    }
}
