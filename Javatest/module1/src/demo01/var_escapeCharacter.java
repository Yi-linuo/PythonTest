package demo01;

public class var_escapeCharacter {
    public static void main(String[] args) {
        /*
            转义字符:  \
            1.将普通字符转成具有特殊含义的字符
            2.将有特殊含义的字符转成普通字符
         */

        /*
        n:普通字符
        \n:换行符
         */
        System.out.println("你好呀\n");
        System.out.println("linuo\n");

        /*
            t:普通字符
            \t:制表符 ->就是Tab键
         */
        System.out.println("动机式\t访谈法");

        /*
            用String表示一个路径
            \\代表一个\
            \\将后面一个\转成普通字符
         */
        String path = "D:\\test-exercise1";
        System.out.println(path);
    }
}
