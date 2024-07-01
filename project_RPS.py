from random import randint
from enum import Enum

class Win_or_Lose(Enum): #가위바위보도 0,1,2라 가위바위보와 구별하기 위해 만든 열거형 타입
    Draw = 0 #경우의 수가 3가지라 else를 쓰면 안 만들어도 되지만 혼동을 주지 않기 위해 만듬
    Win = 1
    Lose = 2

def player_vs_computer(num1, num2): #플레이어 승패 결정 함수
    if (num1 == 0 and num2 == 2) | (num1 == 1 and num2 == 0) | (num1 == 2 and num2 == 1):
        return Win_or_Lose.Win.value
    elif (num1 == 0 and num2 == 1) | (num1 == 1 and num2 == 2) | (num1 == 2 and num2 == 0):
        return Win_or_Lose.Lose.value
    elif num1 == num2:
        return Win_or_Lose.Draw.value

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

win_count = 0
lose_count = 0
draw_count = 0
print('-----------가위바위보 게임 입니다-----------')
while True:
    while True: #플레이어 가위바위보 선택
        player = input("가위 바위 보를 선택하세요 : ")
        if player == "바위":
            player = 0
            break
        elif player == "보":
            player = 1
            break
        elif player == "가위":
            player = 2
            break
        else:
            print("가위, 바위, 보 중에서 입력해야 합니다")
    computer = randint(0, 2) # 주먹은 0, 보는 1, 가위는 2
    if player_vs_computer(player, computer) == Win_or_Lose.Win.value:
        win_count += 1
        print("플레이어 WIN")
    elif player_vs_computer(player, computer) == Win_or_Lose.Lose.value:
        lose_count += 1
        print("컴퓨터 WIN")
    else:
        draw_count += 1
        print("비겼습니다")
    player_choice = game_continue()
    if player_choice == 0:
        break
    elif player_choice == 1:
        continue

print("게임을 종료합니다.")
print(f"승리 : {win_count}, 패배 : {lose_count}, 무승부 : {draw_count}")