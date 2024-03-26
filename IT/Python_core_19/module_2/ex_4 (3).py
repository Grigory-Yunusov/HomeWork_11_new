# swap
baz = int(input("Enter a number: "))
foo = int(input("Enter a number: "))


if baz < foo:
    temp = baz
    baz = (baz + foo) / 2
    foo = temp * foo
else:
    temp = foo
    foo = (foo + baz) / 2
    baz = temp * baz
#
# print(foo, baz)
# Enter a number: 3
# Enter a number: 11
# 33 7.0

if baz < foo:
    baz, foo = (baz + foo) / 2, baz * foo
else:
    foo, baz = (foo + baz) / 2, foo * baz
#
# print(foo, baz)
# Enter a number: 3
# Enter a number: 11
# 33 7.0

a = 4
b = 6

# temp = a
# a = b
# b = temp
a, b = b, a
print(f'a: {a}, b: {b}')