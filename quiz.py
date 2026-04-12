def load_data():
    if not os.path.exists("state.json"):    # 파일 없으면
        return DEFAULT_QUIZZES              # 기본 데이터 사용

    try:
        with open("state.json", "r", encoding="utf-8") as f:
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
#f = open("state.json", "r")
#data = json.load(f)
#f.close() <-- 직접 닫아주어야!             

    except json.JSONDecodeError:            # 파일 손상됐으면
        print("⚠️  데이터 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
        return DEFAULT_QUIZZES              # 기본 데이터로 복구