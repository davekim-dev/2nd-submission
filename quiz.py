import os   #파일 있는지 확인 (os.path.exists 사용하기 위해)
import json     #json(파일 내용을 파이썬으로 바꾸는 도구) 확인



class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer
        
    def display(self):
        print(f"\n{self.question}")    #\n 으로 시작하니까 한 줄 띄고 시작
        for choice in self.choices:  
            print(choice)            #문제 객체에서 선택지들을 반복적으로 출력한다는 것임

    def is_correct(self, user_answer):
        return self.answer == user_answer    #usesr가 고른 정답이 문제 객체 정답과 같은가 확인


# Quiz 인스턴스 (객체) ...  jason이 안 읽히면 얘를 return해라 

DEFAULT_QUIZZES = [      #index(순서), 수정 자유로운 list로 객체 관리       #dic도 관리 가능 BUT 순서대로 quiz를 내보내기에는 더 적합 & value값을 list로 다시 변환해야 할 수도
    Quiz(          
        question="파이썬에서 주석을 나타내는 기호는?",          #quiz 안의 내용들은 바꾸지 않을 것이기에 튜플로 저장
        choices=["1. //", "2. ##", "3. #", "4. **"],          #index 있는 튜플, 리스트 모두 가능
        answer=3
    ),
    Quiz(
        question="파이썬에서 리스트를 만들 때 사용하는 괄호는?",
        choices=("1. ()", "2. []", "3. {}", "4. <>"),     # tuple 도 가능하니까~
        answer=2
    ),
    Quiz(
        question="파이썬에서 함수를 정의할 때 사용하는 키워드는?",
        choices=["1. func", "2. function", "3. define", "4. def"],
        answer=4
    ),
    Quiz(
        question="파이썬에서 무한 루프를 만들 때 사용하는 코드는?",
        choices=["1. while True", "2. for True", "3. loop True", "4. repeat True"],
        answer=1
    ),
    Quiz(
        question="파이썬에서 아무것도 없음을 나타내는 값은?",
        choices=["1. null", "2. undefined", "3. None", "4. empty"],
        answer=3
    ),
]




def load_data():
    if not os.path.exists("state.json"):    # 파일 없으면(os.path:운영체제 라이브러리에서 경로 존재하는지 확인 )
        return DEFAULT_QUIZZES              # 기본 데이터 사용

    try:
        with open("state.json", "r", encoding="utf-8") as f:     #utf-8: 기본 내장된 인코딩 방식(세계 표준) 확실히 선언
            data= json.load(f)             #open- 파일 열기  / state.json - 열 파일 / 'r' - read / 
                                            #encoding='utf-8' - 한글깨짐 방지(다국어) / f - 열린 파일 /
                                            #with open ()as f - 열린 파일을 자동으로 닫아줌
                                            #json.load(f) - 열린 파일 f 를 python으로 변경(jason 사용해서)

                                            # open()으로 파일 열기
                                            #   -> as f 로 파일을 f 변수에 담기
                                            #   -> json.load(f) 로 파이썬 데이터로 변환
                                            #   -> return 으로 반환
                                            #   -> with 블록 끝나면 파일 자동으로 닫힘
                                            #
                                            # f = open("state.json", "r")
                                            # data = json.load(f)
                                            # f.close()  # 직접 닫아주어야 함
        quizzes = []
        for item in data:
            quiz = Quiz(item["question"], item["choices"], item["answer"])   #item은 dict에서 내용을 꺼내 객체로 전환하는 것
            quizzes.append(quiz)

        return quizzes      #json 파일을 객체 리스트 qkuizzes 반환

    except json.JSONDecodeError:            # 파일 손상됐으면
        print("⚠️  데이터 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
        return DEFAULT_QUIZZES              # 기본 데이터로 복구
    

#퀴즈 생성 및 저장 

def get_text_input(message):
    while True:
        value = input(message).strip()   #입력값 양쪽 공백 제거 (사용자 실수 방지) main.py의 choice처럼 아예 안되게 하려는 것이 아님! 

        if value == "":
            print("⚠️  입력값이 없습니다.")
            continue

        return value   #return = 함수 종료
    

def get_answer_input(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("⚠️  입력값이 없습니다.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("⚠️  숫자를 입력해주세요.")
            continue

        if number < 1 or number > 4:
            print("⚠️  1~4 사이의 숫자를 입력해주세요.")
            continue

        return number
    
    #while True:
        #value = input("정답 번호 입력: ").strip()

        #if not value.isdigit():        #isdigit() - 문자열이 숫자(0~9)로만 이루어져 있는지 확인 (음수, 소수는 False)
            #print("숫자를 입력하세요.")
            #continue

        #num = int(value)

        #if 1 <= num <= 4:
            #return num
        #else:
        #    print("1~4 사이 숫자 입력")

def save_data(quizzes):
    data = []

    for quiz in quizzes:    #quiz 객체들을 하나씩 꺼내서
        item = {                    
            "question": quiz.question,          #dic 형태로 만듦 (json 형식 따라가기)  
            "choices": quiz.choices,
            "answer": quiz.answer
        }
        data.append(item)        #list data에 dic item 추가

    with open("state.json", "w", encoding="utf-8") as f:   # 'a' - add라면... 기존 데이터에 추가하는 것 (덮어쓰기X) 밑에 기존 데이터를 불러와야 할까?
                                                           # 'a'로 추가하면... 그냥 dic만 하나 붙이는거!! json은 list 안의 dic 형태임!!! 때문에 list 안에 dic을 넣기 위해서는 'w'가 불가피!
        json.dump(data, f, ensure_ascii=False, indent=4)
            #dump(data,f) - 파이썬 데이터를 json 파일로 저장
            #ensure_ascii=False - 한글 깨짐 방지
            # indent=4 - json 파일을 보기 좋게 들여쓰기  




def add_quiz():
    question = get_text_input("문제를 입력하세요: ")
    choice1 = get_text_input("1번 선택지를 입력하세요: ")
    choice2 = get_text_input("2번 선택지를 입력하세요: ")
    choice3 = get_text_input("3번 선택지를 입력하세요: ")
    choice4 = get_text_input("4번 선택지를 입력하세요: ")
    answer = get_answer_input("정답 번호를 입력하세요 (1~4): ")

    choices = [
        f"1. {choice1}",
        f"2. {choice2}",
        f"3. {choice3}",
        f"4. {choice4}"
    ]                       #display가 choices 리스트를 받아서 출력하기 때문에 1. 2. 3. 4. 형식으로 만들어주는 것

    new_quiz = Quiz(question, choices, answer)   #new_quiz 객체 생성... 내용 바뀌지 않을 것이니 Tuple 사용

    quizzes = load_data()    #기존 데이터를 안 불러오면... 새로 만든 질문만 저장되고 기존 질문들은 사라짐 
             #밑에 save_data(quizzes) 할 때 기존 정보들하고 같이 저장해야... new_quiz만 quizzes에 저장하면.. 기존 애들은 사라지는 것
             #load_data는 list임!!! 
    quizzes.append(new_quiz)
    save_data(quizzes)      #새로운 퀴즈가 추가된 quizzes 리스트 저장


def show_quizzes():
    quizzes = load_data()    #퀴즈 목록... json에 추가된 함수들도 볼 수 있게!
    if not quizzes:
        print("⚠️  저장된 퀴즈가 없습니다.")     #DEFALT_QUIZZES가 있지만... 만일을 대비한 것..
        return
    print("\n===== 퀴즈 목록 =====")
    for index, quiz in enumerate(quizzes, start=1):  #index를 1부터 시작
        print(f"{index}. {quiz.question}")

    #print("\n===== 퀴즈 목록 =====")
    #for index, quiz in enumerate(quizzes):
    #    print(f"{index+1}. {quiz.question}")