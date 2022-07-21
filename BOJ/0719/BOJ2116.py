N = int(input())
dice = [[0 for i in range(6)] for j in range(N)]
for i in range (N):
    dice[i] = list(map(int, input().split()))


# 위, 아래, 옆 정하기
for i in range(6):
    bot = i + 1
    if bot == 1 or bot == 6:
        top = 7 - bot
    elif bot == 2 or bot == 4:
        top = 6 - bot
    else:
        top = 8 - bot

    side = []
    for i in range(6):
        if i + 1 == bot or i + 1 == top:
            pass
        else:
            side.append(i + 1)
    
    print(bot, top, side)