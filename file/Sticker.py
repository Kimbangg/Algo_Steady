test_case  = int(input())
for i in range(test_case):
  dp = []
  each_test = int(input())
  for k in range(2):
    dp.append(list(map(int, input().split())))
  dp[0][1] += dp[1][0]
  dp[1][1] += dp[0][0]
  for j in range(2, each_test):
    dp[0][j] += max(dp[1][j - 1], dp[1][j - 2])
    dp[1][j] += max(dp[0][j - 1], dp[0][j - 2])
  print(max(dp[0][each_test - 1], dp[1][each_test - 1]))
