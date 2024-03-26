
def first(size, *topics):
    size = size + len(topics)
    return size


def second(size, **name):
    size = size + len(name)
    return size


print(first(5, "first", "second", "third"))
print(second(3, comment_one="first", comment_two="second", comment_third="third"))
