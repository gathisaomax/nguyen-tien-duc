print("nguyen tien duc")
print("mssv 235752021610076")
####
import math

pos = [0, 0]
while True:
    s = input("Nhập lệnh di chuyển  (hoặc ấn Enter để thoát): ")
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0].upper()
    steps = int(movement[1])
    
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps

distance = int(round(math.sqrt(pos[1]**2 + pos[0]**2)))
print("Khoảng cách từ vị trí ban đầu đến vị trí hiện tại là: ", distance)