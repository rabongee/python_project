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


answer_number = random.randint(1, 100)

while True:
    player_num = int(input("숫자를 입력해 주세요 : "))
    if player_num < 1 or player_num > 100 :
        print('1~100 사이의 숫자를 입력해 주세요.')
        continue
    if judge(player_num, answer_number) == 'correct':
        break
print('정답입니다!!! 게임을 종료합니다.')






