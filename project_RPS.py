from random import choice

def player_vs_computer(player, computer): #플레이어 승패 결정 함수
    if (player == '가위' and computer == '보') | (player == '바위' and computer == '가위') | (player == '보' and computer == '바위'):
        return 'win'
    elif player == computer:
        return 'draw'
    else:
        return 'lose'

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
        player_choice = input("가위 바위 보를 선택하세요 : ")
        if player_choice == "바위" or player_choice == "보" or player_choice == "가위":
            break
        else:
            print("가위, 바위, 보 중에서 입력해야 합니다")

    computer_choice = choice(['가위', '바위', '보'])
    if player_vs_computer(player_choice, computer_choice) == 'win':
        win_count += 1
        print("플레이어 WIN")
    elif player_vs_computer(player_choice, computer_choice) == 'draw':
        draw_count += 1
        print("비겼습니다")
    else:
        lose_count += 1
        print("컴퓨터 WIN")
    game = game_continue()
    if game == 0:
        break
    elif game == 1:
        continue

print("게임을 종료합니다.")
print(f"승리 : {win_count}, 패배 : {lose_count}, 무승부 : {draw_count}")