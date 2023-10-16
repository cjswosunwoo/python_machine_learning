
import sqlite3

conn = sqlite3.connect("survey.db")

cursor = conn.cursor()
# 기존 존재하는 데이터 베이스 삭제
cursor.execute("DROP TABLE IF EXISTS survey")
# survey라는 데이터 베이스 생성
cursor.execute("""CREATE TABLE IF NOT EXISTS survey(
               NO INTEGER PRIMARY KEY AUTOINCREMENT,
                food TEXT(20) UNIQUE NOT NULL,
               count INTEGER NOT NULL)""")

# 기존 존재하는 설문 선택지 생성
choice = ['한식', '중식', '일식', '양식']

#설문 선택지를 데이터베이스에 저장
for i in range(len(choice)):
    print(f'{i+1}. {choice[i]}')
    cursor.execute("INSERT INTO survey (food, count) VALUES (?,?)", (choice[i],0))
    conn.commit()

cursor.close()
conn.close()