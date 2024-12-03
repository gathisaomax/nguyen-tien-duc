print("nguyen tien duc")
print("mssv 235752021610076")

even_numbers = []
for num in range(1000, 3001):
    num_str = str(num)
    if all(int(digit) % 2 == 0 for digit in num_str):
        even_numbers.append(num_str)

result = ",".join(even_numbers)
print(result)
