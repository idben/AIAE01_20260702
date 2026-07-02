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

# 進階的 match-case
# case score if score >= 90: 如果 score 符合而且大於等於 90 分 
# case _ if score >= 90: 不管值是什麼, 先讓它通過來判斷是不是大於等於 90 分
match score:
    case score if score >= 90:
        grade = "甲"
    case score if score >= 80:
        grade = "乙"
    case score if score >= 70:
        grade = "丙"
    case score if score >= 60:
        grade = "丁"
    case _:
        grade = "戊"

print(f"你的分數是 {score}，你的等級是 {grade} 等")

status = 402

match status:
    case 200:
        print("請求成功")
    case 400:
        print("請求錯誤")
    case 404:
        print("找不到網頁")
    case _:
        print("未知狀態碼")


is_member = True
total = 2200

if is_member:
    if total >= 2000:
        print(f"是會員，滿 2000 打八折: {total * 0.8}")
    else:
        print(f"是會員，未滿 2000 打九五折: {total * 0.95}")
else:
    print(f"非會員，原價 {total} 購入")