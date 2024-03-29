package com.jsong.actual;

import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 *
 * 四个线程打印
 *
 * Function:
 *
 * @author jsong
 *         Date: 2018/11/15 18:06
 * @since JDK 1.8
 */
@State(Scope.Benchmark)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
//@Threads(Threads.MAX)
public class FourThreadPrinter extends Thread {

    private final static Logger LOGGER = LoggerFactory.getLogger(FourThreadPrinter.class);

    private static final Lock lock = new ReentrantLock();

    private static volatile int index = 0;

    private static volatile boolean flag = false;

    public FourThreadPrinter() {
    }

    /**
     * t1=1
     * t2=2
     * t3=3
     * t4=4
     */
    private static volatile int type = 1;

    /**
     * 线程当前状态
     */
    private int currentType;

    public FourThreadPrinter(String name, int currentType) {
        super(name);
        this.currentType = currentType;
    }


    @Benchmark
    @BenchmarkMode({Mode.AverageTime})
    @Override
    public void run() {
        int count = 100;
        while (index < count) {
            if (currentType == type) {
                try {
                    //lock.lock();
                    index++;
                    LOGGER.info("print: " + index + " flag=" + flag);
                    updateCondition();
                } finally {
                    //lock.unlock();
                }
            }
        }
    }

    private void updateCondition() {

        if (Thread.currentThread().getName().equals("t1")) {
            type = 2;
        } else if (Thread.currentThread().getName().equals("t2")) {
            type = 3;
        } else if (Thread.currentThread().getName().equals("t3")) {
            type = 4;
        } else if (Thread.currentThread().getName().equals("t4")) {
            type = 1;
        }

    }

    public void start() {
        Thread t1 = new FourThreadPrinter("t1", 1);
        Thread t2 = new FourThreadPrinter("t2", 2);
        Thread t3 = new FourThreadPrinter("t3", 3);
        Thread t4 = new FourThreadPrinter("t4", 4);
        t1.start();
        t2.start();
        t3.start();
        t4.start();
    }

    public static void main(String[] args) {
        Options opt = new OptionsBuilder()
                .include(FourThreadPrinter.class.getSimpleName()) // 可以用方法名，也可以用XXX.class.getSimpleName()
                .forks(3)//  forks(3)指的是做3轮测试，因为一次测试无法有效的代表结果，所以通过3轮测试较为全面的测试，而每一轮都是先预热，再正式计量。
                .warmupIterations(2)// 预热2轮
                .measurementIterations(2)// 代表正式计量测试做2轮，而每次都是先执行完预热再执行正式计量， 内容都是调用标注了@Benchmark的代码。
                .build();

        try {
            new Runner(opt).run();
        } catch (RunnerException e) {
            throw new RuntimeException(e);
        }
    }
}