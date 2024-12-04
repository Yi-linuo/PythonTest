package com.jsong.robostcode;

import lombok.extern.slf4j.Slf4j;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * 如何处写出健壮的代码
 *
 * 参考： Effective Java 第57条 :最小花局部变量的作用域
 *
 */
@Slf4j
public class ForWhlieChoice {

    /**
     * 入口
     */
    public static void main(String[] args) {

        List<String> list = new ArrayList<String>(10);
        list.add("a");
        list.add("b");

        // Interface-based iteration
        for (Iterator<String> it = list.iterator(); it.hasNext(); ) {
            String str = it.next();
            log.info(str);
        }

        // for-each loop
        for (String str : list) {
            log.info(str);
        }

    }
}
