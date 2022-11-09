def mul(*number):
    s = 1
    for i in number:
        s = s * i
    return s


num = {2, 3, 4}  # ()/[]/{}均可
mul(*num)  # 要带“*”