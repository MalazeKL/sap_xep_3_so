def swap(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
    return a, b
num1 = int(input("Nhập số thứ 1: "))
num2 = int(input("Nhập số thứ 2: "))
num3 = int(input("Nhập số thứ 3: "))
num1, num2 = swap(num1, num2)
num2, num3 = swap(num2, num3)
num1, num2 = swap(num1, num2)
print("3 số sau khi được sắp xếp: ", num1, num2, num3)
