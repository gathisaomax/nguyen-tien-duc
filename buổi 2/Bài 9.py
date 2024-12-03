print("nguyen tien duc")
print("235752021610076")
############################################
str_input = input("Nhập vào một chuỗi: ")
char_count = {}

for n in str_input:
    keys = char_count.keys()
    if n in keys:
        char_count[n] += 1
    else:
        char_count[n] = 1

print(char_count)