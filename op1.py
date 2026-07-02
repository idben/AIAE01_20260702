# bool 的運算
print(True * 10)

# 除法
# 被除數是零時會出錯 ZeroDivisionError
a = 10
b = 0
# print(a/b)
print("-"*20)

# 整除
a = 10
b = 3
print(a/b)
print(a//b)
print("-"*20)

# pass 放在判斷式後面當做暫時內容
# 一種條件的判斷
# 但是加上預設值，會變成 if-else 的變形
result_a = "奇數"
if a % 2 == 0:
    result_a = "偶數"
print(f"變數 a 是 {result_a}")

# 兩種結果的判斷
if b % 2 == 0:
   result_b = "偶數"
else:
   result_b = "奇數"
print(f"變數 b 是 {result_b}")

# 次方
print(2**3)
print(9**0.5)
print("-"*20)


x = 10
# x = x + 5
x += 5
print(f"x += 5 = {x}")