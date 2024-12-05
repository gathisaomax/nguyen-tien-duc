print("nguyen tien duc")
print("mssv 235752021610076")
####
def benefit(t, n ,k):
    return n * (1 + t / 100) ** k
t = float(input("Nhập lãi suất hàng tháng (%): "))
n = float(input("Nhập số vốn ban đầu: "))
k = int(input("Nhập số tháng gửi: "))

tong_tien = benefit(t, n, k)
print("Số tiền nhận được sau", k, "tháng là:", tong_tien)