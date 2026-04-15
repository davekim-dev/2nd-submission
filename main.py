#json 이란? - JavaScript Object Notation, 데이터를 저장하거나 전달하기 위한 텍스트 형식
#왜 json을 사용하는가? - 데이터 교환이 쉽고, 다양한 언어에서 지원되며, 사람이 읽기 쉽기 때문 => 구조적으로 해결해주기 때문에
#json 으로 저장하려면? - json module 사용해서 저장 (객체 > 딕션어리 > json) / json.load() - json > 딕션어리 > 객체 
#json은 주석을 달 수 없음..

from quiz import add_quiz
from quiz import show_quizzes
from game import show_high_score



def show_menu():
    print("\n===== 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("====================")

def run():
    while True:
        show_menu()
        choice = input("번호를 선택하세요: ").strip()  # .strip() => input의 공백 삭제

        if choice == "":    #밑에 int(choice) 있으므로 필요X 
            print("⚠️  입력값이 없습니다. 번호를 입력해주세요.")
            continue

        try:
            number = int(choice)        # ← 숫자 변환 시도  문자 & 빈칸 모두 잡아줌!! only int만 받기 때문에
        except ValueError:
            print("⚠️  숫자를 입력해주세요.")
            continue                    # ← 다시 while 처음으로

        if number < 1 or number > 5:      #밑의 else 와 같은 의미
            print("⚠️  1~5 사이의 숫자를 입력해주세요.")
            continue

        if choice == "1":
            print("[퀴즈 풀기] - 아직 구현 전")
        elif choice == "2":
            print("[퀴즈 추가]")
            add_quiz()
        elif choice == "3":
            print("[퀴즈 목록]")
            show_quizzes()
        elif choice == "4":
            print("[점수 확인]")
            show_high_score()4
        elif choice == "5":
            print("게임을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("⚠️  잘못된 입력입니다. 1~5 중에서 선택해주세요.")

if __name__ == "__main__":   #실행할 파일의 이름이 main 일때만 실행해라
    run()

