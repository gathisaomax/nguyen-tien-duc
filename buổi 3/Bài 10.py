print("nguyen tien duc")
print("mssv 235752021610076")
####
import math

def Tinh(R):
    if R > 0:
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R**2
        return chu_vi, dien_tich
    else:
        return "Bán kính không hợp lệ. Vui lòng nhập một số dương."

R = float(input("Nhập bán kính R: "))
result = Tinh(R)

if isinstance(result, tuple):
    chu_vi, dien_tich = result
    print("Chu vi hình tròn:", chu_vi)
    print("Diện tích hình tròn:", dien_tich)
else:
    print(result)