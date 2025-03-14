# 기본 라이브러리라 파이썬 설치시 자동으로 설치됩니다!
# random 모듈은 랜덤한 숫자를 생성할 때 사용합니다.
import random
import os

# 행맨 그림
hangman_pics = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\
     |
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\
     |   /
     |
    ---""",
    """
     ------
     |    |
     |    O
     |   /|\
     |   / \
     |
    ---""",
]

# 게임에 사용될 단어 목록
words = ["apple", "banana", "orange", "grape", "lemon"]

#화면 지우는 함수
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class HangmanGame:

    # 게임 시작 초기화 함수
    def __init__(self):

        # 단어 가져오기.
        self.word = random.choice(words)

        # 단어 숨기기
        self.hidden_word = ["_"] * len(self.word)

        # 목숨 기회
        self.life = 6

        # 사용자가 적은 글자 저장
        self.guessed_letters = []


    # 화면 함수
    def display(self):

        clear_screen()
        print(hangman_pics[6 - self.life])
        print("현재 단어", " ".join(self.hidden_word))
        print("입력한 글자들:", ", ".join(self.guessed_letters))



    # 진행 함수
    def play(self):
        # 게임 진행.
        while self.life > 0 and "_" in self.hidden_word:


            # 현재 상태 출력.
            self.display()

            # 사용자 입력
            guess = input("글자를 입력하세요.").lower()

            # 예외처리
            if len(guess) != 1 or not guess.isalpha():
                print("한글자 또는 알파벳으로 입력해주세요.")
                continue

            # 예외처리 2
            elif guess in self.guessed_letters:
                print("이미 입력된 알파벳입니다.")
                continue

            # 입력된 단어 저장
            self.guessed_letters.append(guess)

            # 글자 확인
            self.check_guess(guess)
        
        self.game_over()

    # 검사 함수
    def check_guess(self, guess):
        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.hidden_word[i] = guess
            print("정답입니다")
        else:
            self.life -= 1
            print(f"틀렸습니다. 남은 기회: {self.life}")

    # 종료 함수
    def game_over(self):
        if "_" not in self.hidden_word:
            print("축하합니다! 정답을 맞혔어요!")
        else:
            print(f"게임 오버! 정답은 '{self.word}'였습니다.")

# 메인
if __name__ == "__main__":

    while True:
        game = HangmanGame()
        game.play()

        restart = input("다시 시작 하시겠습니까? (y/n)").lower()
        
        if restart == "n":
            print("게임을 종료합니다.")
            break
