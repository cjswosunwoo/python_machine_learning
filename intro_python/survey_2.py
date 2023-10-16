
import sqlite3

conn = sqlite3.connect("survey.db")

cursor = conn.cursor()


while True: 
    #survey 데이터베이스에 저장된 선택지(음식 종류)를 불러옴
    choice_list = []
    cursor.execute("SELECT * from survey")
    row = cursor.fetchall()
    for i in range(len(row)):
        choice_list.append(row[i][1])

    print('1. 설문 참여하기')
    print('2. 설문 현황보기')
    print('3. 설문 종료')
    survey = int(input("선택: "))
    if survey ==1:
        #선택지 리스트를 출력
        for i in range(len(choice_list)):
            print(f'{i+1}. {choice_list[i]}')
        print('0. 기타(직접입력)')
        choice = int(input("선택: "))
        if choice == 0:
            #리스트에 없는 선택지를 추가
            try: 
                etc = input("음식 추가: ")
                cursor.execute("INSERT INTO survey (food, count) VALUES (?,?)", (etc,0))
                conn.commit()
            except Exception as e:
                print(e)
                continue
        for j in range(len(choice_list)):
            #투표를 한 선택지에 투표수가 DB에 1씩 증가하게끔 설정
            if choice == j+1:
                cursor.execute(f'UPDATE survey SET count = count+1 WHERE NO={j+1}')
                conn.commit()
    
    elif survey == 2:
        # 설문 현황 출력
        for i in range(len(choice_list)):
            print(f'{row[i][1]} ===> {row[i][2]}')

    elif survey ==3:
        print("설문종료")
        break

    

    

cursor.close()
conn.close()