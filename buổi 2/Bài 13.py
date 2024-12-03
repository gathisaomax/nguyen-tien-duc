print("nguyen tien duc")
print("235752021610076")
############################################
import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương vô nghiệm.")
    else:
        x = -c / b
        print(f"Phương trình có một nghiệm duy nhất: x = {x}")
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sprt(delta)) / (2*a)
        x2 = (-b - math.sprt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        print("Phương trình vô nhiệm.")