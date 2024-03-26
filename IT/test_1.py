class MyStringProcessor:
    def __init__(self, line):
        self.line = line

    def __str__(self):
        words = self.line.strip().split(' ')
        name = ' '.join([word.capitalize() for word in words])
        return name

# Пример использования
my_string_processor = MyStringProcessor("hello world")
result = str(my_string_processor)
print(result)