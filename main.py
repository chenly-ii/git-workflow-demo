def greet(name, age):
    return f"Hello, {name}! You are {age} years old."


def main():
    name = input("请输入你的名字：")
    age = input("请输入你的年龄：")
    print(greet(name, age))


if __name__ == "__main__":
    main()