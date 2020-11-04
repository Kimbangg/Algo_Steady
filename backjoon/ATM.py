N = int(input())
each_wait = list(map(int, input().split()))
if N == 1 :
    print(each_wait[0])
else :
    each_wait.sort()
    each_sum = 0
    total_sum = 0

    for i in range(N) :
        total_sum += (each_sum + each_wait[i])
        each_sum += each_wait[i]
    print(total_sum)

