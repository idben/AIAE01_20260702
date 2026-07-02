s = "hello world"
print(s.find("world1"))
# print(s.index("world1"))
# find/index 都會回傳索引值
# find 找不到回傳 -1
# index 找不到回傳錯誤
print("-"*20)

s2 = "今天是陰天，我最喜歡陰天，我常常在陰天出去玩。"
print(s2.find("陰天", s2.find("陰天")+1))