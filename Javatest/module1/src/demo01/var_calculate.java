package demo01;

public class var_calculate {
    //运算+ - * /
    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 3;

        int sum = num1+num2;
        System.out.println(sum);//13

        int sub = num1-num2;
        System.out.println(sub);//7

        int mul = num1*num2;
        System.out.println(mul);//30

        //
        int div = num1/num2;//3,因为/前后都是整数,结果取整,且赋值给整数变量
        double div1 = num1/num2;//3.0  赋值给了浮点型

    }
}
