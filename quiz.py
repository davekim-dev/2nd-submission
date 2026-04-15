def load_data():
    if not os.path.exists("state.json"):    # 파일 없으면(os.path:운영체제 라이브러리에서 경로 존재하는지 확인 )
        return DEFAULT_QUIZZES              # 기본 데이터 사용

    try:
        with open("state.json", "r", encoding="utf-8") as f:     #utf-8: 기본 내장된 인코딩 방식(세계 표준) 확실히 선언
            return json.load(f)             #open- 파일 열기  / state.json - 열 파일 / 'r' - read / 
                                            #encoding='utf-8' - 한글깨짐 방지(다국어) / f - 열린 파일 /
                                            #with open ()as f - 열린 파일을 자동으로 닫아줌
                                            #json.load(f) - 열린 파일 f 를 python으로 변경
                                                '''
                                                 open()으로 파일 열기
                                                    └── as f 로 파일을 f 변수에 담기
                                                        └── json.load(f) 로 파이썬 데이터로 변환
                                                            └── return 으로 반환
                                                                └── with 블록 끝나면 파일 자동으로 닫힘
                                                
                                                #f = open("state.json", "r")
                                                #data = json.load(f)
                                                #f.close() <-- 직접 닫아주어야!             
                                                '''
   

    except json.JSONDecodeError:            # 파일 손상됐으면
        print("⚠️  데이터 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
        return DEFAULT_QUIZZES              # 기본 데이터로 복구
    



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