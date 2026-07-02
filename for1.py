# for 基本迴圈
# 遍歷list
fruits = ["蘋果", "香蕉", "橘子"]

for fruit in fruits:
    print(fruit)
print("-"*20)

# 遍歷字元
word = "Python"
for char in word:
    print(char)
print("-"*20)

# 遍歷字典 key-value pair 鍵值對
scores = {"Alice": 95, "Bob": 88, "Charlie": 92}
for key in scores:
    print(f"{key} = {scores[key]}")

# 字典專屬方法 .items() 把字典的 key-value 轉成 tuple
print(scores.items())

# list 的解構前的習慣性用法
score1 = ["Alice", 95]
print(score1[0])
print(score1[1])
user1_name = score1[0]
user1_score = score1[1]
print(user1_name)
print(user1_score)

# list 的解構
user2_name, user2_score = ["Bob", 88]
print(user2_name)
print(user2_score)

# .items() 與 list 的解構在迴圈中的組合技
print("-"*30)
for user_name, user_score in scores.items():
    print(f"{user_name} 的分數是 {user_score}")