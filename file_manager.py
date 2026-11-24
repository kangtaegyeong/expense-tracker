import os
import csv

def create_file():
    while True:
        filename = input("새 목록을 입력하세요: ")

        filepath = os.path.join("data", filename + ".csv")
        #os.path.join()은 경로를 안전하게 이어주는 기능으로, data + 9월 생활비.csv를 합쳐서 경로를 만들어 줌

        if os.path.exists(filepath):
            print('이미 같은 이름의 목록이 존재합니다.')
            continue
        break
        #경로에 이미 파일이 존재하는지 확인

    # 실제 파일 생성 부분
    with open(filepath, "w", encoding="utf-8", newline=""):
        pass

    print(filename + ".csv 파일이 생성되었습니다.")

    return filepath
    # 사용자가 파일 이름을 입력하면 data/파일명.csv를 main.py로 돌려줌


def select_file():
    # data 폴더 안에 있는 파일 이름들을 가져온다.
    files = os.listdir("data")

    csv_files = []

    for file in files:
        # 파일 이름이 .csv로 끝나는지 확인 후 빈 리스트에 추가
        if file.endswith(".csv"):
            csv_files.append(file)

    if len(csv_files) == 0:
        print(" 저장된 목록이 없습니다. ")
        # main.py에 선택된 파일이 없음을 알려준다. 
        return None

    print("\n ===== 저장된 목록 ===== ")

    # i는 실제로 0번부터 시작이지만 사용자에게 보여지는 것은 1부터 시작하는 것이 좋음
    for i in range(len(csv_files)):
        print(i + 1, ".", csv_files[i])


    while True:
        try:
            choice = int(input(" 불러올 목록 번호를 선택하세요: "))

            if 1 <= choice <= len(csv_files):
                break
            else:
                print('목록에 있는 번호를 선택해주세요.')
        
        except ValueError:
            print('숫자로 입력해주세요.')

    #사용자가 입력한 값보다 실제 리스트 번호는 1작으므로 다시 1을 빼주면 된다.
    select_file = csv_files[choice - 1]

    filepath = os.path.join("data", select_file)

    print(select_file, "을(를) 선택했습니다.")


    # 사용자가 선택한 csv 파일을 main.py로 돌려준다. -> main.py 파일의 is not None 부분에서 이 부분을 받고 있음.
    return filepath

# 어떤 파일을 읽을지 외부에서 알려줘야 하므로 filepath 명시
def load_expenses(filepath):
    expenses = []

    # r은 읽기, a는 뒤에 추가하기, w는 새로 쓰기 / encoding="utf-8"은 한글 같은 문자가 깨지지 않도록 인코딩 방식을 저장
    # 즉, filepath에 있는 파일을 읽기 모드로 열고, UTF-8 방식으로 읽고 그 파일 객체를 file이라는 이름으로 사용한다.
    # with는 파일을 다 쓰고 나면 자동으로 닫아준다.
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) < 2:
                continue

            name = row[0]
            
            price = int(row[1])

            expense = [name, price]
            expenses.append(expense)
    
    return expenses


def save_expenses(filepath, expenses):
     with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # 여러 줄을 한꺼번에 csv에 저장한다.
        writer.writerows(expenses)