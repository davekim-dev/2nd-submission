import os
import json
from quiz import load_data
# quiz.py 에서 load_data 함수를 가져와라 (except 부분에서 return 값이 DEFAULT_QUIZZES)
#from 파일이름 import 가져올 것(객체)

def load_high_score():
    if not os.path.exists("score.json"):
        return 0

    try:
        with open("score.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        return data["high_score"]      #dict에서 value 꺼내는 것

    except json.JSONDecodeError:
        print("⚠️  점수 파일이 손상되었습니다. 최고 점수를 0으로 초기화합니다.")
        return 0


def save_high_score(score):
    data = {"high_score": score}

    with open("score.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def show_high_score():
    if not os.path.exists("score.json"):       #json 파일이 없는 경우: 다른 환경에서 실행하거나, 처음 실행하는 경우
        print("⚠️  아직 퀴즈를 풀지 않았습니다.")
        return

    quizzes = load_data()
    total = len(quizzes)
    high_score = load_high_score()

    if high_score > total:
        high_score = total

    print(f"최고 점수: {high_score}/{total}")

#high_socre을 class로 묶는다면?  >> 가능은 하나.. 오랫동안 저장해야 할 객체가 없기 때문에 굳이?

class QuizGame:
    def __init__(self):                   
        self.quizzes = load_data()     # QuizGame 에서 사용할 self.quizzes를 load_data()로 설정해 (객체 안에 내용을 넣는 것)
        self.score = 0     #초기값 설정 + 객체 정의 self.score 가 있다.
        self.high_score = load_high_score()   #최고 점수도 객체 안에 넣어주는 것 (게임이 끝났을 때 최고 점수와 비교하기 위해)          

        # 게임 진행하면서 그 값이 변동되는 애들을 객체로 넣음                                
                                          
    def play(self):                  
        if not self.quizzes:
            print("⚠️  퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return         #아무것도 없이 return = 함수 종료 (None값 반환) 
                           #아래 함수 실행X

        self.score = 0            # 게임 진행 시 초기화하는 것!!! 여러번 게임 진행할 수 있으니 점수를 리셋해주는 것!!

        for i, quiz in enumerate(self.quizzes):             # for i,quiz in range(len(quizzes))  인덱스 & 값
            print(f"\n[{i+1}/{len(self.quizzes)}]")           #print(i, quizzes[i])
            #[1/5] [2/5] 이런식으로 순서를 출력
            quiz.display()
            answer = self.get_answer()      #def get_answer() 함수의 값을 answer에 저장
                                            # 즉, 문제를 보여주고 답을 받는 것
            if quiz.is_correct(answer):
                print("✅ 정답입니다!")
                self.score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")

        self.show_result()

    def get_answer(self):                   
        while True:
            choice = input("정답을 입력하세요 (1~4): ").strip()

            if choice == "":
                print("⚠️  입력값이 없습니다.")
                continue

            try:
                number = int(choice)
            except ValueError:
                print("⚠️  숫자를 입력해주세요.")
                continue

            if number < 1 or number > 4:
                print("⚠️  1~4 사이의 숫자를 입력해주세요.")
                continue

            return number     #choice 로 시작해서 number(int)로 바꾸는 과정

    def show_result(self):
        total = len(self.quizzes)
        high_score = load_high_score()

        if high_score > total:     #상한선 정해주는 것! 5문제밖에 없는데 7점이 나올 수는 없으니까
            high_score = total

        if self.score > high_score:       #게임이 끝났을 때 현재 점수가 최고 점수보다 높으면 기록 갱신 (json 파일에 저장))
            high_score = self.score
            save_high_score(high_score)

        print(f"\n========== 결과 ==========")
        print(f"총 {total}문제 중 {self.score}문제 정답!")
        print(f"점수: {self.score}/{total}")
        print(f"최고 점수: {high_score}/{total}")
        print("==========================")





if __name__ == "__main__":
    game = QuizGame()
    game.play()