import string

def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    length = len(password)
    if length < 6:
        return "Weak", "Password too short! Try adding more characters."
    elif has_lower and has_upper and has_digit and has_special:
        return "Strong", "Strong password! Great job!"
    elif has_lower and has_upper and has_digit:
        return "Medium","Try adding a special character for a stronger password."
    else:
        return "Weak", "Password should include uppercase, lowercase, numbers, and special characters."

def main():
    password_history = []
    while True:
        password = input("Enter your password: ")
        password_history.append(password)
        strength, feedback = check_password_strength(password)
        print(feedback)
        if strength == "Strong":
            break  

if __name__ == "__main__":
    main()
