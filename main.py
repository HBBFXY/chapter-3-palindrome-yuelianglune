def syetem_huiwen(number):
    num_str = str(number)

    if len(num_str) != 5:
        return False
    
    return num_str == num_str[::-1]

try:
    input_num = int(input("请输入一个5位数："))
    if 10000 <= input_num <= 99999:
        if syetem_huiwen(input_num):
            print(f"{input_num}是回文数")
        else:
            print(f"{input_num}不是回文数")
    else:
        print("输入错误，请确保输入的是一个5位数")
except ValueError:
    print("输入错误，请输入一个整数")# 这里编写你的代码
