def has_digit(password): return any(char.isdigit() for char in password)

def has_upper_letters(password): return any(char.isupper() for char in password)

def has_lower_letters(password): return any(char.islower() for char in password)

def has_symbols(password): return any(not char.isalnum() for char in password)

def password_rating(password): checks = [ has_digit, has_upper_letters, has_lower_letters, has_symbols, ]

score = sum(2 for check in checks if check(password))

if len(password) > 12:
    score += 2

return score

def main(): password = input("Введите пароль: ") print("Рейтинг пароля: " + str(password_rating(password)))

if name == "main": main()






