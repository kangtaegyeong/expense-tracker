print("Expense-Tracker")

expenses = []



while True:
    name = input('지출 내역을 입력하세요: ')

    if name =='': 
        break
    price = int(input('지출 금액을 입력하세요: '))

    expense = [name, price]

    expenses.append(expense)

for expense in expenses:
    print(expense[0],'=', expense[1], '원')