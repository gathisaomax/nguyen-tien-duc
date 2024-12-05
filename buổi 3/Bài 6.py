print("nguyen tien duc")
print("235752021610076")
###########################################
def get_sum(*num):
    tmp = 0
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print(result)