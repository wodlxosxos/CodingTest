import sys

N = int(sys.stdin.readline().rstrip())

num_list = [0,]*(N+1)

for i in range(1, N + 1):
    if i > 2:
        num_list[i] = num_list[i-1] + num_list[i-2]
    elif i == 1:
        num_list[i] = 1
    elif i == 2:
        num_list[i] = 2

print(num_list[N]%10007)