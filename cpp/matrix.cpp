#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <fstream>

using Matrix = std::vector<std::vector<double>>;

Matrix random_matrix(int n) {
    std::mt19937 gen(42);
    std::uniform_real_distribution<> dist(0.0, 1.0);
    Matrix m(n, std::vector<double>(n));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            m[i][j] = dist(gen);
    return m;
}

Matrix multiply(const Matrix& A, const Matrix& B) {
    int n = A.size();
    Matrix C(n, std::vector<double>(n, 0.0));
    for (int i = 0; i < n; ++i)
        for (int k = 0; k < n; ++k)
            for (int j = 0; j < n; ++j)
                C[i][j] += A[i][k] * B[k][j];
    return C;
}

int main() {
    std::vector<int> sizes = {64, 128, 256};

    std::ofstream file("cpp_bench.csv");
    file << "language,impl,n,time_s\n";

    for (int n : sizes) {
        Matrix A = random_matrix(n);
        Matrix B = random_matrix(n);

        auto start = std::chrono::high_resolution_clock::now();
        Matrix C = multiply(A, B);
        auto end = std::chrono::high_resolution_clock::now();

        double elapsed = std::chrono::duration<double>(end - start).count();

        std::cout << "[C++][n=" << n << "] time=" << elapsed << " s\n";
        file << "cpp,naive," << n << "," << elapsed << "\n";
    }

    file.close();
    return 0;
}
