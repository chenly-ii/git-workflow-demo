def greet(name):
    return f"Hello, {name}!"


def main():
    name = input("请输入你的名字：")
    print(greet(name))


if __name__ == "__main__":
    main()