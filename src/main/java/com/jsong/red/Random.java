package com.jsong.red;

import org.openjdk.jmh.annotations.*;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.RunnerException;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;

import java.util.SplittableRandom;
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
    public static double generateRandom() {
        return Math.random();
    }

    @Benchmark
    public static double generateThreadLocalRandom() {
        return ThreadLocalRandom.current().nextDouble();
    }

    @Benchmark
    public static double generateSplittableRandom() {
        SplittableRandom random = new SplittableRandom();
        return random.nextDouble();
    }

    public static void main(String[] args) {
        Options opt = new OptionsBuilder()
                .include("generateRandom")
                .include("generateThreadLocalRandom")
                .include("generateSplittableRandom")
                // forks(3)指的是做3轮测试，因为一次测试无法有效的代表结果，所以通过3轮测试较为全面的测试，而每一轮都是先预热，再正式计量。
                .forks(3)
                // 预热2轮
                .warmupIterations(2)
                // 代表正式计量测试做2轮，而每次都是先执行完预热再执行正式计量， 内容都是调用标注了@Benchmark的代码。
                .measurementIterations(2)
                .build();
        try {
            new Runner(opt).run();
        } catch (RunnerException e) {
            throw new RuntimeException(e);
        }
    }

}
