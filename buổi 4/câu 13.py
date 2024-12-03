print("nguyen tien duc")
print("mssv 235752021610076")

chuoi = input('Nhập chuỗi các từ: ')
danh_sach_tu = chuoi.split()
danh_sach_tu.sort()

print("Các từ theo thứ tự từ điển:")
for tu in danh_sach_tu:
    print(tu)
