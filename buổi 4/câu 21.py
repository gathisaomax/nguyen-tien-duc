print("nguyen tien duc")
print("mssv 235752021610076")

def kiem_tra_chia_het_5(chuoi):
    danh_sach = chuoi.split(',')
    ket_qua = []
    for so in danh_sach:
        if int(so, 2) % 5 == 0:
            ket_qua.append(so)
    if ket_qua:
        print(' '.join(ket_qua))

chuoi_nhap = input("Nhập chuỗi các số nhị phân 4 chữ số (cách nhau bằng dấu phẩy): ")
kiem_tra_chia_het_5(chuoi_nhap)
