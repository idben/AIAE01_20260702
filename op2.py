# 連鎖比較
age = input("請輸入年紀")
print(18 <= int(age) < 65)

if 18 <= int(age) < 65:
    message = "歡迎光臨"
else:
    message = "下次再來"

print(message)
print("-"*20)

# 邏輯運算子 and: 把上面的連鎖比較換成邏輯運算子
if int(age) >= 18 and int(age) < 65:
    message = "在年齡區間內"
else:
    message = "區間外"
print(message)
print("-"*20)

# 邏輯運算子 or: 只要有一個條件達成就為 True
s1 = "apple, banana, orange"
f1 = "apple"
f2 = "pieapple"
f3 = "orange"

message = "沒有在賣"
if f1 in s1 or f2 in s1:
    message = "有在賣"
print(message)


# 邏輯運算子 not:
message = "f2 有在 s1 中"
if f2 not in s1:
    message = "f2 沒有在 s1 中"
    pass
print(message)