type MyList = list[int]

example: MyList = []


def add_item(list: MyList, num: int) -> None:
    list.append(num)
    return

add_item(example, 5)
print(example)
add_item(example, 6)
print(example)
add_item(example, 7)
print(example)

# Lists and Objects are pass by reference in Python, while ints floats are pass by value

