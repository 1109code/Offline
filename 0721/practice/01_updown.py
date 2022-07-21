import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    #여기부터 코드를 작성하세요.
    user_input = 0
    while user_input < 1 or user_input > 10000:
        user_input = int(input('1 이상 10000이하의 숫자를 입력하세요. : '))
        if user_input < 1 or user_input > 10000:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.\n')
            continue

    if user_input > answer:
        print('Up!!!')
    else:
        print('Down!!!')