# Python_project

## 프로젝트 소개
개인 과제용 프로젝트인 Up and Down 게임과 가위바위보 게임을 만들어 보았습니다.

파일명은 그대로 project_up_down과 rock, paper, scissors의 줄임말인 project_RPS입니다.

## 개발환경
Version : Python 3.10.11

## 프로젝트 기능
* **Up Down 게임**
  1. 컴퓨터가 뽑아주는 랜덤한 수는 random모듈의 randint함수로 해결했습니다.
  2. 플레이어가 숫자를 입력하면 유효한 숫자인지 판단합니다.(1~100사이의 정수)
  3. 숫자가 높은지 낮은지 판단하는 judge함수가 입력된 수를 판단하고 정확히 맞췄다면 시도 횟수를 보여줍니다.
  4. 게임의 지난 기록과 최소 시도횟수를 보여주고 플레이어가 게임을 계속할건지 묻습니다.
  5. n을 입력시 게임을 종료합니다.


* **가위바위보 게임**
  1. 플레이어가 가위바위보를 정하고 컴퓨터도 가위바위보가 담긴 리스트에서 랜덤으로 하나를 뽑습니다.
  2. 플레이어의 선택과 컴퓨터를 비교하여 player_vs_computer함수로 숫자를 비교하여 가위바위보 결과를 알려줍니다.
  3. 결과에 맞는 출력문을 출력해주고 게임의 지속여부를 묻습니다.
  4. n을 입력해 게임을 종료한다면 게임동안의 승리 횟수, 패배 횟수, 무승부 횟수를 출력해줍니다.

