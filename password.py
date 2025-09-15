import random
import string

def password_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_lower, has_upper, has_digit, has_symbol])

    if length < 6:
        return "Weak"
    elif score >=3 and length >=8:
        return "Strong"
    else:
        return "Medium"

while True:
    length = int(input("Enter the desired password length:"))
    if length < 4:
        print("⚠️ Password length must be at least 4! Try again.")
    else:
        break

print("\nChoose password complexity level:")
print("1. Easy (letters + numbers)")
print("2. Intermediate (letters + numbers + uppercase)")
print("3. Strong (letters+numbers + uppercase + special characters)")

choice = int(input("Enter your choice(1/2/3): "))

if(choice==1):
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))

elif (choice==2):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))

elif (choice==3):
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation
    password+= [random.choice(characters)for _ in range(length-4)]
    random.shuffle(password)
    password=''.join(password)
else:
    print("Invalid choice! Defaulting to Strong level.")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

print("\n✅ Your generated password is:", password)

strength = password_strength(password)
print("🔒 Password Strength:", strength)