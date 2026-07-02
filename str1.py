s = "hello world"
print(s.find("world1"))
# print(s.index("world1"))
# find/index 都會回傳索引值
# find 找不到回傳 -1
# index 找不到回傳錯誤
print("-"*20)

s2 = "今天是陰天，我最喜歡陰天，我常常在陰天出去玩。"
print(s2.find("陰天", s2.find("陰天")+1))
print("-"*20)

# 成員判斷 in / not in
print("晴天" in s2)
print("晴天" not in s2)
print("-"*20)

# startswith / endswith
filename = "photo.JpG"
print(filename.lower().endswith(".jpg"))
print("-"*20)

# count 計次
print(f"陰天在這個句子中共出現 {s2.count("陰天")} 次")
print("-"*20)

# 取代, replace
print(s2.replace("陰天", "晴天", 1))
print("-"*20)

# 切成 list
list1 = s2.split("，")
print(list1[1])

date_str = "2026-07-02"
date_list = date_str.split("-")
print(date_list)
print(f"今天是 {date_list[0]} 年 {int(date_list[1])} 月 {date_list[2][1]} 日")