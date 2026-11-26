import os
import csv


def create_file(filename):
    filepath = os.path.join(
        "data",
        filename + ".csv"
    )
    # os.path.join()은 경로를 안전하게 이어주는 기능
    # data + 파일명.csv를 합쳐서 경로를 만들어 줌

    if os.path.exists(filepath):
        return None
        # 경로에 이미 파일이 존재하는지 확인

    # 실제 파일 생성 부분
    with open(
        filepath,
        "w",
        encoding="utf-8",
        newline=""
    ):
        pass

    return filepath
    # 사용자가 파일 이름을 입력하면 data/파일명.csv를 돌려줌


def select_file():
    # data 폴더 안에 있는 파일 이름들을 가져온다.
    files = os.listdir("data")

    csv_files = []

    for file in files:
        # 파일 이름이 .csv로 끝나는지 확인 후 리스트에 추가
        if file.endswith(".csv"):
            csv_files.append(file)

    if len(csv_files) == 0:
        print("저장된 목록이 없습니다.")
        return None

    print("\n===== 저장된 목록 =====")

    # 실제 리스트 번호는 0부터 시작하지만
    # 사용자에게는 1부터 보여준다.
    for i in range(len(csv_files)):
        print(i + 1, ".", csv_files[i])

    while True:
        try:
            choice = int(input("불러올 목록 번호를 선택하세요: "))

            if 1 <= choice <= len(csv_files):
                break

            else:
                print("목록에 있는 번호를 선택해주세요.")

        except ValueError:
            print("숫자로 입력해주세요.")

    # 사용자가 1번을 선택하면 실제 리스트에서는 0번
    selected_file = csv_files[choice - 1]

    filepath = os.path.join("data", selected_file)

    print(selected_file, "을(를) 선택했습니다.")

    return filepath


def load_expenses(filepath):
    expenses = []

    # r = 읽기
    # a = 뒤에 추가
    # w = 새로 쓰기
    # utf-8 = 한글 등이 깨지지 않도록 인코딩 지정
    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            # 최소한 이름과 금액은 있어야 함
            if len(row) < 2:
                continue

            name = row[0]
            price = int(row[1])

            # 예전 CSV에는 카테고리가 없을 수 있으므로
            # 세 번째 값이 있으면 불러오고,
            # 없으면 자동으로 "기타" 처리
            if len(row) >= 3:
                category = row[2]
            else:
                category = "기타"

            expense = [name, price, category]
            expenses.append(expense)

    return expenses


def save_expenses(filepath, expenses):
    with open(
        filepath,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)

        # 여러 줄을 한꺼번에 CSV에 저장한다.
        writer.writerows(expenses)


def get_file_list():
    files = os.listdir("data")

    csv_files = []

    for file in files:
        if file.endswith(".csv"):
            csv_files.append(file)

    return csv_files