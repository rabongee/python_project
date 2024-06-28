import random

def judge(player_num,answer_number):
    if player_num > answer_number:
        print('Down')
        return 'Down'
    elif player_num < answer_number:
        print('Up')
        return 'Up'
    elif player_num == answer_number:
        return 'correct'


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
    print('다시 하시겠습니까? (Y/N)', end=' ')
    player_choice = input()
    player_choice = player_choice.upper()
    if player_choice == 'N':
        break
    elif player_choice == 'Y':
        continue

print("게임을 종료합니다.")




