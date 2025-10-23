package edu.ulpgc.matmul;

import java.util.Random;

public final class MatrixMul {

    public static double[][] randomMatrix(int n, long seed) {
        Random rnd = new Random(seed);
        double[][] M = new double[n][n];
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
                M[i][j] = rnd.nextDouble();
        return M;
    }

    public static double[][] multiply(double[][] A, double[][] B) {
        int n = A.length;
        double[][] C = new double[n][n];
        for (int i=0;i<n;i++) {
            double[] Ai = A[i];
            double[] Ci = C[i];
            for (int k=0;k<n;k++) {
                double aik = Ai[k];
                double[] Bk = B[k];
                for (int j=0;j<n;j++) {
                    Ci[j] += aik * Bk[j];
                }
            }
        }
        return C;
    }
}
