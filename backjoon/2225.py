import sys 
N, K = map(int, sys.stdin.readline().split()) 
mod = 1000000000 
table = [1] 
table += [0] * N 

for i in range(1, K+1): 
    for idx in range(1, N+1): 
        table[idx] = (table[idx] + table[idx-1])%mod 
print(table[N])

