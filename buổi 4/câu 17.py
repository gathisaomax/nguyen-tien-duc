print("nguyen tien duc")
print("mssv 235752021610076")

def fibonacci_list(n):
    a, b = 0, 1
    fib_list = []
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

n = int(input("Nhập số nguyên n: "))
print("Danh sách các số Fibonacci nhỏ hơn n:")
print(fibonacci_list(n))
