

# 기존 expenses 리스트 함수를 받아온다.
def add_expenses(expenses):
    while True:
        name = input(" 지출 내역을 입력하세요: ")

        if name == "":
            break

        #우선 숫자로 변환을 시도해보고 후에 숫자가 아닌 값을 넢으면 프로그램을 종료하지 않고 다시 입력하게 만드는 코드
        while True:
            try:
                price = int(input("지출 금액을 입력하세요: ")) 
                break
            except ValueError:
                print("금액은 숫자로 입력하세요.")   

        expense = [name, price]
        expenses.append(expense)

        print("\n===== 현재 지출 목록 =====")

        for expense in expenses:
            print(expense[0], '=', expense[1], '원')


        while True:
            print('\n1. 계속 지출 추가')
            print('2. 이전 메뉴로 돌아가기')

            choice = input('선택하세요: ')

            if choice == '1':
                break #현재 반복문만 종료
            elif choice == '2':
                return expenses #add_expenses()함수 자체를 끝내면서 expenses를 main.py로 돌려줌

            else:
                print('1 또는 2만 입력해주세요.')

    return expenses


def show_expenses(expenses):
    if len(expenses) == 0:
        print("등록된 지출이 없습니다.")
        return

    for expense in expenses:
        print(expense[0], "=", expense[1], "원")

def show_total(expenses):
    total = 0

    for expense in expenses:
        total += expense[1]

    print("총 지출 금액: ", total, "원")