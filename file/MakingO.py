N = int(input())
dp = [0] * (N + 1)
card = [0] + list(map(int, input().split()))
dp[1] = card[1]
for i in range(2, N + 1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + card[j]:
            dp[i] = dp[i - j] + card[j]
print(dp[N])
