print("nguyen tien duc")
print("mssv 235752021610076")

def fibonacci_list(n):
    a, b = 0, 1
    fib_list = []
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

p = tuple(x for x in range(2, 1000000) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)))

n = int(input("Nhập số nguyên n: "))
print("Danh sách các số Fibonacci nhỏ hơn n:")
print(fibonacci_list(n))
