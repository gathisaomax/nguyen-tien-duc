print("nguyen tien duc")
print("235752021610076")
############################################
a, b = 1, 2
total = 0

print("Dãy số Fibonacci nhỏ hơn 4.000.000: ")
while a < 4000000:
    if a % 2 == 0:
        total += a
    print(a, end=", ")
    a, b = b, a + b
    
print("\nTổng các số chẵn trong dãy Fibonacci: ", total)