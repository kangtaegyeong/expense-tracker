from file_manager import create_file, select_file, load_expenses, save_expenses
# file_manager 파일 안에 있는 create_file() 함수를 가져와 main.py에서 사용한다는 의미
# 즉 파일끼리 연결되는 구조 생성 완료 
from expense_manager import add_expenses, show_expenses, show_total


def manage_expenses(filepath, expenses):
    modified = False

    while True:
        print("\n ===== 지출 관리 ===== ")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 저장")
        print("5. 이전 메뉴")

        sub_menu = int(input("메뉴를 선택하세요: "))

        if sub_menu == 1:
            expenses = add_expenses(expenses)

        elif sub_menu == 2:
            show_expenses(expenses)

        elif sub_menu == 3:
            show_total(expenses)

        elif sub_menu == 4:
            save_expenses(filepath, expenses)
            modified = False
            print("저장되었습니다.")

        elif sub_menu == 5:
            if modified:
                print('\n저장되지 않은 변경사항이 있습니다.')
                print('1. 저장 후 나가기')
                print('2. 저장하지 않고 나가기')
                print('3. 취소')

                choice = input('선택하세요:')

                if choice == '1':
                    save_expenses(filepath, expenses)
                    break
                elif choice == '2':
                    break
                elif choice == '3':
                    continue
                    #반복문의 처음으로 돌아감
                else:
                    print('1부터 3 중에서 선택해주세요.')
            else:    
                break
        else:
            print("1부터 5 중에서 선택해주세요.")


while True:
    print("\n ===== Expense Tracker ===== ")
    print("1. 기존 목록 불러오기")
    print("2. 새 목록 만들기")
    print("3. 종료 ")

    menu = input("메뉴를 선택하세요: ")

    if menu == "1":
        filepath = select_file()

        if filepath is not None:
            expenses = load_expenses(filepath)
            manage_expenses(filepath, expenses)

    elif menu == "2":   
        filepath = create_file()   
        expenses = []

        manage_expenses(filepath, expenses)

    elif menu == "3":
        print(" 프로그램을 종료합니다. ")
        break

    else:
        print(" 1, 2, 3 메뉴 중에서 선택하여 주세요. ")

    