package com.jsong.red;

import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;

/**
 * Function: 测试生成随机数 性能
 *
 * @author jsong
 *         Date: 03/01/2018 16:52
 * @since JDK 1.8
 */
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.NANOSECONDS)
@State(Scope.Benchmark)
public class Random {
    @Benchmark
    public static void generateRandom() {
        double random = Math.random();
    }
    @Benchmark
    public static void generateThreadLocalRandom() {
        double random = ThreadLocalRandom.current().nextDouble();
    }

    public static void main(String[] args) {
        Options opt = new OptionsBuilder()
                .include("generateRandom")
                .include("generateThreadLocalRandom")// 可以用方法名，也可以用XXX.class.getSimpleName()
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
