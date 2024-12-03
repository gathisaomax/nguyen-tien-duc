print("nguyen tien duc")
print("mssv 235752021610076")

def count_upper_lower(sentence):
    upper_case = sum(char.isupper() for char in sentence)
    lower_case = sum(char.islower() for char in sentence)
    print(f"Chữ hoa (uppercase): {upper_case}")
    print(f"Chữ thường (lowercase): {lower_case}")

input_sentence = input("Nhập một chuỗi: ")
count_upper_lower(input_sentence)
