import csv #지출 항목을 csv파일로 저장

print("Expense-Tracker")

expenses = [] #while문 안으로 들어갈 경우 메뉴를 한 번 선택할 때마다 빈리스트로 초기화 시킴, 즉 2번 출력 안 됨

while True:
    print("=====메뉴=====")
    print("1. 지출 추가")
    print("2. 지출 목록 보기")
    print("3. 총 지출 보기")
    print("4. 종료")

    menu = int(input('메뉴를 입력하세요: '))

    if menu == 1:
        while True:
            name = input('지출 내역을 입력하세요: ')
            if name == "":
                break
            price = int(input('지출 금액을 입력하세요: '))

            expense = [name, price]

            expenses.append(expense)

            #expenses.csv라는 파일을 연다.
            with open("expenses.csv", "a", newline="", encoding="utf-8") as file:
                #CSV 형식으로 파일에 쓰기 위한 도구를 만듦
                writer = csv.writer(file)
                #리스트 한 줄을 CSV에 점심,12000와 같은 형태로 저장
                writer.writerow(expense)

    elif menu == 2:
        for expense in expenses:
            print(expense[0],'=', expense[1], '원')

    elif menu == 3:
        total = 0 #for문으로 작성 안 하면 마지막 값만 계산됨
        for expense in expenses:
            total += expense[1]
        print("총 지출 금액: ", total,"원")


    elif menu == 4:
        print("프로그램을 종료합니다.")
        break


"""
total = 0

for expense in expenses:
    print(expense[0],'=', expense[1], '원')
    total += expense[1]
    #print("총 지출 금액: ", total,"원") 이렇게 작성하면 지출 목록마다 계산된 총액 출력


print("총 지출 금액: ", total,"원")
"""
