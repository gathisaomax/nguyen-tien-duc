print("nguyen tien duc")
print("mssv 235752021610076")

def calculate_balance(transactions):
    balance = 0
    for transaction in transactions:
        action, amount = transaction.split()
        amount = int(amount)
        if action == 'D':
            balance += amount
        else:
            balance -= amount
    return balance

transactions = input("Nhập nhật ký giao dịch (D/W và số tiền, cách nhau bởi dấu phẩy): ").split(',')
balance = calculate_balance(transactions)

print(f"Số dư cuối cùng là: {balance}")
