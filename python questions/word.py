def to_uppercase(text: str):
    return text.upper()

def to_lowercase(text: str):
    return text.lower()

if __name__ == "__main__":
    s = input()

    count_upper = 0
    count_lower = 0

    for i in s:
        if i.isupper():
            count_upper += 1
        else:
            count_lower += 1

    if count_lower > count_upper:
        print(to_lowercase(s))
    elif count_lower == count_upper:
        print(to_lowercase(s))
    else:
        print(to_uppercase(s))





