print("nguyen tien duc")
print("maev 220752021610076")

chuoi = input("Nhập một dãy các từ: ")
danh_sach_tu = chuoi.split()
do_dai_max = max(len(tu) for tu in danh_sach_tu)
tu_dai_nhat = [tu for tu in danh_sach_tu if len(tu) == do_dai_max]

print("Từ dài nhất:", " ".join(tu_dai_nhat))
