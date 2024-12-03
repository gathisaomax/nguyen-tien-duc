print("nguyen tien duc")
print("mssv 235752021610076")

def tong_uoc_so(n):
    tong = 1
    for i in range(2, (n// 2) + 1):
        if n % i == 0 :
            tong += i
            return tong
n = int(input("nhập số n: "))
print(f"các số nguyên ương nhỏ hơn (n) có tổng các ước số lớn hơn chính nó")
for i in range(2, n):
    if tong_uoc_so(i) >i:
        print(i)
