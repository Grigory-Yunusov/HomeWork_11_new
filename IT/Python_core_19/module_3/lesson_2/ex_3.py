# Функція приймає рядок, а повертає словник, де ключ це символ рядка, а значення код ASCII
# {'key': 'value'}

# hello world

def codes_of_string(string: str) -> dict:
    codes = {}
    for ch in string:
        if not ch in codes:
            codes[ch] = ord(ch)  #  {'h': 104}
    return codes


print(codes_of_string('hello world'))
