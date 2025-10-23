# test code / runner: parametrized, multi-run, CSV, optional profiling
import argparse, csv, statistics, timeit, cProfile, pstats, os
from matrixmul import generate_random_matrix, matmul_naive

def run_once(n: int, seed: int | None):
    A = generate_random_matrix(n, seed=seed)
    B = generate_random_matrix(n, seed=(None if seed is None else seed+1))
    def thunk():
        matmul_naive(A, B)
    return timeit.timeit(thunk, number=1)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--sizes", type=int, nargs="+", default=[64,128,256,512])
    p.add_argument("--runs", type=int, default=5)
    p.add_argument("--seed", type=int, default=123)
    p.add_argument("--csv", default="results/python_bench.csv")
    p.add_argument("--profile", action="store_true")
    args = p.parse_args()

    os.makedirs(os.path.dirname(args.csv), exist_ok=True)
    with open(args.csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["language","impl","n","run","time_s"])

        for n in args.sizes:
            times = []
            if args.profile and n <= 256:  # keep profile small
                pr = cProfile.Profile()
                A = generate_random_matrix(n, seed=args.seed)
                B = generate_random_matrix(n, seed=args.seed+1)
                pr.enable()
                _ = matmul_naive(A,B)
                pr.disable()
                ps = pstats.Stats(pr).strip_dirs().sort_stats("tottime")
                ps.print_stats(15)

            for r in range(args.runs):
                t = run_once(n, args.seed + r)
                w.writerow(["python","naive",n,r,t])
                times.append(t)
            print(f"[Python][n={n}] mean={statistics.mean(times):.3f}s ± {statistics.stdev(times):.3f}s over {args.runs} runs")

if __name__ == "__main__":
    main()
    