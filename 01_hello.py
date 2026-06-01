# 第一个 Python 程序
# 功能：和电脑对话，学习变量、输入输出、条件判断

name = input("请输入你的名字：")
print(f"你好，{name}！欢迎来到 Python 世界！")

# 学问1：变量
age = int(input("你几岁了？"))
print(f"{age} 岁，正是学编程的黄金年龄！")

# 学问2：条件判断
if age >= 20:
    print("你是大学生了，可以开始投简历了！")
else:
    print("好好享受大学生活，提前学技术！")

# 学问3：循环
print("\n来数几个数：")
for i in range(1, 6):
    print(f"  第 {i} 个数：{i}")

print("\n恭喜你，Python 入门完成！")
