from random import randint

def result(num1, num2):
    if (num1 == 0 and num2 == 2) | (num1 == 1 and num2 == 0) | (num1 == 2 and num2 == 1):
        return 1
    elif (num1 == 0 and num2 == 1) | (num1 == 1 and num2 == 2) | (num1 == 2 and num2 == 0):
        return 2
    elif num1 == num2:
        return 0

def game_continue():
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
    if result (player, computer) == 1:
        win_count += 1
        print("플레이어 WIN")
    elif result (player, computer) == 2:
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