print("nguyen tien duc")
print("mssv 235752021610076")

def filter_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers

input_numbers = input("Nhập các số, cách nhau bởi dấu phẩy: ")
numbers_list = [int(num) for num in input_numbers.split(',')]
odd_numbers = filter_odd_numbers(numbers_list)

print(",".join(map(str, odd_numbers)))
