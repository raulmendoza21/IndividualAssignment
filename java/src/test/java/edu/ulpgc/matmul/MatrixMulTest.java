package edu.ulpgc.matmul;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class MatrixMulTest {
    @Test
    void smallMatrixMatchesReference() {
        int n = 5;
        double[][] A = MatrixMul.randomMatrix(n, 42L);
        double[][] B = MatrixMul.randomMatrix(n, 7L);
        double[][] C = MatrixMul.multiply(A,B);

        double[][] R = new double[n][n];
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++) {
                double s=0;
                for (int k=0;k<n;k++) s += A[i][k]*B[k][j];
                R[i][j]=s;
            }
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
                assertEquals(R[i][j], C[i][j], 1e-9);
    }
}
