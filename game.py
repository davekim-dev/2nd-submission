from quiz import load_data
# quiz.py 에서 load_data 함수를 가져와라 (except 부분에서 return 값이 DEFAULT_QUIZZES)
#from 파일이름 import 가져올 것(객체)

class QuizGame:
    def __init__(self):                   
        self.quizzes = load_data()     # QuizGame 에서 사용할 self.quizzes를 load_data()로 설정해 (객체 안에 내용을 넣는 것)
        self.score = 0               
                                           # 객체 받아올 때 하는 첫 초기화 : 그럼 얘는 왜 필요한가? 어차피 처음 받아오는데
                                           # !! 점수 초기화 보다는 'self.score' 라는 객체를 정의하는 것
    def play(self):                  
        if not self.quizzes:
            print("⚠️  퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return         #아무것도 없이 return = 함수 종료 (None값 반환) 
                           #아래 함수 실행X

        self.score = 0            # 게임 진행 시 초기화하는 것!!! 여러번 게임 진행할 수 있으니 점수를 리셋해주는 것!!

        for i, quiz in enumerate(self.quizzes):             # for i,quiz in range(len(quizzes))  인덱스 & 값
            print(f"\n[{i+1}/{len(self.quizzes)}]").           #print(i, quizzes[i])
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
        print(f"\n========== 결과 ==========")
        print(f"총 {total}문제 중 {self.score}문제 정답!")
        print(f"점수: {self.score}/{total}")
        print("==========================")




if __name__ == "__main__":
    game = QuizGame()
    game.play()