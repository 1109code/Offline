N = int(input())
bulb = list(map(int, input().split()))
students = int(input())
info = []

for i in range(students):
    info.append(list(map(int, input().split())))

for i in range(students):
    if info[i][0] == 1:
        for j in range(N//info[i][1]):
            if bulb[info[i][1]*(j+1)-1] == 0:
                bulb[info[i][1]*(j+1)-1] = 1
            else:
                bulb[info[i][1]*(j+1)-1] = 0

    elif info[i][0] == 2:
        k= 0
        while True:
            if info[i][1]-1+k>=N or info[i][1]-1-k<0:
                break;
            if bulb[info[i][1]-1+k] == bulb[info[i][1]-1-k]:
                if bulb[info[i][1]-1+k] == 0:
                    bulb[info[i][1]-1+k] = 1
                else:
                    bulb[info[i][1]-1+k] = 0
                if k!=0:
                    if bulb[info[i][1]-1-k] == 0:
                        bulb[info[i][1]-1-k] = 1
                    else:
                        bulb[info[i][1]-1-k] = 0
            else:
                break;
            k+=1

width = 0
for s in bulb:
    print(s, end = ' ')
    width += 1
    if width == 20:
        print()
        width = 0