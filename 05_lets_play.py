import numpy as np

num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    M = np.array([list(map(int, input().split())) for _ in range(N)])

    D = np.trace(M)
    R = sum(len(set(r)) < N for r in M)
    C = sum(len(set(c)) < N for c in M.T)
    print(D, R, C)
    print(D+R+C)