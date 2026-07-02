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

# 遍歷字典
scores = {"Alice": 95, "Bob": 88, "Charlie": 92}
for key in scores:
    print(f"{key} = {scores[key]}")