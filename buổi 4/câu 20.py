print("nguyen tien duc")
print("mssv 235752021610076")

def in_tam_giac_pascal(n):
    pascal = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
        row.append(1)
        pascal.append(row)
    for row in pascal:
        print(row)

n = int(input("Nhập số dòng của tam giác Pascal: "))
in_tam_giac_pascal(n)
