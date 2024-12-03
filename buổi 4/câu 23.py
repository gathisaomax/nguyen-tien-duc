print("nguyen tien duc")
print("mssv 235752021610076")

def count_letters_digits(sentence):
    letters = sum(char.isalpha() for char in sentence)
    digits = sum(char.isdigit() for char in sentence)
    print(f"Số chữ cái là: {letters}")
    print(f"Số chữ số là: {digits}")

input_sentence = input("Nhập một câu: ")
count_letters_digits(input_sentence)
