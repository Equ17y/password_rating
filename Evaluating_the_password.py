

def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(flag.isdigit() for flag in password)


def has_upper_letters(password):
    return any(flag.isupper() for flag in password)


def has_lower_letters(password):
    return any(flag.islower() for flag in password)


def has_symbols(password):
    return any(not flag.isalnum() for flag in password)


def main():
    password = input("Введите пароль: ")

    checks = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]


    score = sum(check(password) for check in checks) * 2

    if not (has_upper_letters(password) or has_lower_letters(password)):
        score = 0

    print("Рейтинг пароля:", score)

if __name__ == '__main__':
    main()