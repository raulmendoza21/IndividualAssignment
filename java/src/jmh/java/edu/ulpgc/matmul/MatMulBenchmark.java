package edu.ulpgc.matmul;

import org.openjdk.jmh.annotations.*;
import java.util.concurrent.TimeUnit;

@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
@Warmup(iterations=3, time=1, timeUnit=TimeUnit.SECONDS)
@Measurement(iterations=5, time=1, timeUnit=TimeUnit.SECONDS)
@Fork(value=2)
@State(Scope.Thread)
public class MatMulBenchmark {

    @Param({"64","128","256"})
    public int n;

    private double[][] A, B;

    @Setup(Level.Trial)
    public void setup() {
        A = MatrixMul.randomMatrix(n, 123L);
        B = MatrixMul.randomMatrix(n, 456L);
    }

    @Benchmark
    public double[][] matmul_naive() {
        return MatrixMul.multiply(A, B);
    }
}
