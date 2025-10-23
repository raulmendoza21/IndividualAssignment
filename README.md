# 🧮 Individual Assignment — Matrix Multiplication Benchmark

This repository compares the performance of **matrix multiplication** implemented in **Python**, **Java**, and **C++**, using professional benchmarking tools and following best software engineering practices.

## 📂 Project Structure
```
IndividualAssignment/
│
├── paper/
│   ├── main.tex               # LaTeX source
│   └── paper.pdf              # Final report (ready for submission)
│
├── python/
│   ├── matrix.py
│   ├── bench.py
│   ├── core.py
│   └── tests/                 # Unit tests for correctness
│
├── java/
│   ├── pom.xml
│   └── src/                   # Source and JMH benchmarks
│
├── cpp/
│   ├── matrix.cpp             # Optimized native implementation
│
├── results/
│   ├── python_bench.csv
│   ├── java_bench.csv
│   ├── cpp_bench.csv
│   └── combined_bench.csv     # Aggregated results
│
└── tools/
    └── merge_benchmarks.py    # Merges CSV results into one file
```

## ⚙️ How to Run

### 🐍 Python
```bash
cd python
python bench.py --sizes 64 128 256 --runs 7 --csv ../results/python_bench.csv
```

### ☕ Java (JMH)
```bash
cd java
mvn clean package
java -jar target/benchmarks.jar -rf csv -rff ../results/java_bench.csv
```

### 💻 C++
```bash
cd cpp
cl /O2 matrix.cpp
matrix.exe > ../results/cpp_bench.csv
```

### 📊 Combine Results
```bash
python tools/merge_benchmarks.py results/python_bench.csv results/java_bench.csv results/cpp_bench.csv -o results/combined_bench.csv
```

## 🧪 Methodology
- Separation of production code, testing, and benchmarking.
- Several runs for each experiment to compute mean and deviation.
- Parametrized matrix sizes (64, 128, 256).
- Profiling performed using:
  - `cProfile` (Python)
  - `JMH` (Java)
  - `std::chrono` (C++)

## 📈 Example Results
| Size (n) | Python (ms) | Java (ms) | C++ (ms) |
|-----------|--------------|-----------|----------|
| 64        | 14.2         | 1.3       | 0.9      |
| 128       | 112.0        | 8.6       | 7.4      |
| 256       | 875.0        | 67.9      | 59.3     |

## 🧾 Paper
The complete report (LaTeX + PDF) is located in the `/paper` folder and includes:
- Methodology
- Experimental setup
- Profiling analysis
- Discussion and conclusions

## 🧠 Author
**Raúl Mendoza**  
Universidad de Las Palmas de Gran Canaria (ULPGC)

📎 Repository: [github.com/raulmendoza21/IndividualAssignment](https://github.com/raulmendoza21/IndividualAssignment)
