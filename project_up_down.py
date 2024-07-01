import random

def judge(player,answer): # 숫자를 비교하는 함수
    if player > answer:
        print('Down')
        return 'Down'
    elif player < answer:
        print('Up')
        return 'Up'
    elif player == answer:
        return 'correct'

def game_continue(): #게임을 계속할건지 물어보는 함수
    choice = input('다시 하시겠습니까? (Y/N) ')
    choice = choice.upper()
    if choice != 'Y' and choice != 'N':
        while True:
            choice = input('Y나 N만 입력해주세요. (Y/N) ')
            choice = choice.upper()
            if choice == 'Y' or choice == 'N':
                break
    if choice == 'N':
        return 0
    elif choice == 'Y':
        return 1

last_count = 0
min_count = 1000
player_choice = ''
print('-----------Up Down 게임 입니다-----------')

while True:
    answer_number = random.randint(1, 100)
    count = 0
    while True:
        player_num = int(input("숫자를 입력해 주세요 : "))
        if player_num < 1 or player_num > 100 :
            print('1~100 사이의 숫자를 입력해 주세요.')
            continue
        count += 1
        if judge(player_num, answer_number) == 'correct':
            break
    print(f'{count}회로 맞추셨습니다!!!')
    if min_count > count:
        min_count = count
    if last_count != 0:
        print(f'이전 횟수 : {last_count}, 최고 기록 : {min_count}')
    else:
        print(f'최고 기록 : {min_count}')
    last_count = count
    player_choice = game_continue()
    if player_choice == 0:
        break
    elif player_choice == 1:
        continue

print("게임을 종료합니다.")
