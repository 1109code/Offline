N = int(input())
dice = [[0 for i in range(6)] for j in range(N)]
for i in range (N):
    dice[i] = list(map(int, input().split()))
print(dice)