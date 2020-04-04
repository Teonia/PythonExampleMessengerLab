import random


def get_limit():
    return 10


def main_fun():
    name = "Jack"
    print("Hello world, " + name)
    text = f"Annie and {name}"
    print(type(text))

    l = [1, 3, text, [100, -100]]
    print(l[-1][1])

    s = 'ijcatjfsdj0'
    print(s)
    print(s[-3])
    print(s[2:-6])

    sum = 0
    for value in l:
        if type(value) == int:
            sum += value
    print(f"sum is {sum}")

    [100, 'hi', '']
    d = {"key": "value", "other": 2}
    print(d['other'])

    a = 0
    b = get_limit()
    i = 0
    while a < b:
        print(f"index = {i}")
        i += 1
        if a < b / 2:
            a += 3
            print(a)
        elif a == b / 2:
            a += 2
            print(a)
            break
        else:
            a += 1
            print(a)
    print(f"result is {a}")

    value1 = None
    value2 = []
    if value1 == value2:
        print("Equal")

    if value2 is None:
        print("None")
    print(type(value1))
    print(type(value2))

    print(100 // 3)
    magic_number = random.randint(0, 100)

    while guess_number(magic_number, input("guess what is it!")):
        continue


def guess_number(magic_number: object, input_value: object) -> object:
    number = int(input_value)
    if number == magic_number:
        print("boom!")
        return False
    elif number > magic_number:
        print("woof!")
        return True
    else:
        print("woof! woof!")  # returns False by default O_o


main_fun()
