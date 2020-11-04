N = int(input())

def hanoi(n, start, to, end) :
    if n == 1 :
        print(start,end)
    else :
        hanoi(n-1, start, end, to)
        print(start, end)
        hanoi(n-1, to, start, end)

sum = 1
for i in range(N-1) :
    sum = sum * 2 + 1
print(sum)
hanoi(N,1,2,3)
