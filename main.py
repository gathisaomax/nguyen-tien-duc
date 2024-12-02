print("ngueyn tien duc")
print("mssv 235752021610076")
#####
input_file = open('C:/a.txt', 'r')

for line in input_file:
    l = len(line) 
    s = ''         
    while l > 0:
        s += line[l - 1]  
        l -= 1          
    print(s.strip())      

input_file.close()
