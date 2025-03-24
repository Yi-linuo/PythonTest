package demo01;

import com.sun.xml.internal.ws.api.model.wsdl.WSDLOutput;

/*
    类型转换
    a.等号左右两边不一致
    b.不同类型做运算

    注意事项
    1.强制转换可能会造成 精度损失 及 数据溢出(不随意使用,除非没有办法)
    2.byte,short定义的时候如果等号右边是整数常量,如果没有超出范围,jvm自动转


  */
public class DataTypeConversion {
    public static void main(String[] args) {
        //自动类型转换
        /*
            等号左边是long型的变量
            等号右边是整数,整数默认的类型是int
            将取值范围小的数据类型赋值给取值范围大的数据类型
         */
        long num1 = 100;
        System.out.println(num1);

        int i = 10;
        double a = 3.5;

        /*
            double = int+double
            这时候int自动提升为double
            double = double+double
         */
        double sum = i+a;
        System.out.println(sum);

        //强制类型转换 不随意使用(精度损失 及 数据溢出)
        /*
            等号右边小数默认类型为double
            等号左边是float的变量

            大范围类型赋值给小范围类型 -> 报错

         */
        //float num2 = 2.5;
        float num2 = (float)2.5;//强制转换格式
        float num3 = 2.5f;//把等号右边转换成跟左边同样的类型

        /*
            byte,short定义的时候
            如果等号右边是整数常量,如果没有超出范围,jvm自动转
                等号右边有变量参与,自动升为int,结果再赋给byte和short时,需要强转
         */
        byte b = 10;
        b = (byte)(b+1);
        System.out.println(b);

        /*
        char类型数据如果参与运算,自动提升为int型
        对应ASCII码表,unicode码表
         */
        char c = 'A';
        char c1 = '中';
        System.out.println(c+0);//65
        System.out.println(c1+0);//20013
    }
}
