# 簡單判斷式與縮排強調
is_raining = False

if is_raining:
    print("外面正在下雨。")
    print("記得帶傘再出門。")
print("程式結束。")
print("-"*20)


num = 17
if num % 2 == 0:
    print(f"{num} 是偶數")
else:
    print(f"{num} 是奇數")

# if-elif-else
score = 51
grade = "戊"

if score >= 90:
    grade = "甲"
elif score >= 80:
    grade = "乙"
elif score >= 70:
    grade = "丙"
elif score >= 60:
    grade = "丁"
# else:
#     grade = "戊"

print(f"你的分數是 {score}，你的等級是 {grade} 等")