import random
import string

def generate_password(length, use_special_chars, use_numbers, use_uppercase):
    # Define character sets based on user preferences
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    special_chars = string.punctuation if use_special_chars else ''
    numeric_chars = string.digits if use_numbers else ''

    # Combine character sets
    all_chars = lowercase_chars + uppercase_chars + special_chars + numeric_chars

    # Ensure the password length is at least 8 characters
    length = max(length, 8)

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def get_user_preferences():
    length = int(input("Enter the desired password length: "))
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    return length, use_special_chars, use_numbers, use_uppercase

def main():
    print("Password Generator")

    # Get user preferences
    length, use_special_chars, use_numbers, use_uppercase = get_user_preferences()

    # Generate the password
    password = generate_password(length, use_special_chars, use_numbers, use_uppercase)

    # Display the generated password
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
