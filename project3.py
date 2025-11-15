import random

def play_game():
    a = 'rock'
    b = 'paper'
    c = 'scissors'
    
    choices = [a, b, c]

    print("Choose your move:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    user_input = input("Your choice: ").strip().lower()

    # Convert number to word if input is a digit
    if user_input == '1':
        user = a
    elif user_input == '2':
        user = b
    elif user_input == '3':
        user = c
    elif user_input in choices:
        user = user_input
    else:
        print("Invalid input. Please enter 1, 2, 3, or Rock, Paper, or Scissors.")
        return

    computer = random.choice(choices)
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == a and computer == c) or \
         (user == c and computer == b) or \
         (user == b and computer == a):
        print("You win!")
    else:
        print("Computer wins!")

# Run the game
if __name__ == '__main__':
    play_game()





# Binary Search Algorithm

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Create a sorted list
sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print("Sorted List:", sorted_list)

# Ask the user for a target value
try:
    target = int(input("Enter a number to search for: "))
    result = binary_search(sorted_list, target)

    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the list.")
except ValueError:
    print("Please enter a valid integer.")


# Email to one or multiple recipients
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipients, subject, body):
    # Set up the message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipients, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print("Error:", e)
    finally:
        server.quit()

# Example usage
if __name__ == '__main__':
    sender = input("Your email: ")
    password = input("Your email app password: ")  # Use an app password for Gmail

    recipients_input = input("Enter recipient emails (comma-separated): ")
    recipients = [email.strip() for email in recipients_input.split(",")]

    subject = input("Subject: ")
    message = input("Message: ")

    send_email(sender, password, recipients, subject, message)


#Zodiac Sign
import pandas as pd
from datetime import datetime

# Zodiac sign logic
def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 'Aquarius'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Pisces'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Aries'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Taurus'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Gemini'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return 'Cancer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Leo'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Virgo'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Libra'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Scorpio'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Sagittarius'
    else:
        return 'Capricorn'

# Input
name = input("Enter your name: ")
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

# Convert input to date
try:
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    day = birthdate.day
    month = birthdate.month
    zodiac = get_zodiac_sign(day, month)

    # Create and save data using pandas
    data = {'Name': [name], 'Birthdate': [birthdate_str], 'Zodiac Sign': [zodiac]}
    df = pd.DataFrame(data)

    # Save to file
    df.to_csv('zodiac_signs.csv', index=False, mode='a', header=not pd.read_csv('zodiac_signs.csv').empty if pd.io.common.file_exists('zodiac_signs.csv') else True)

    print(f"{name}, your Zodiac sign is: {zodiac}")
    print("Information saved to 'zodiac_signs.csv'.")

except ValueError:
    print("Invalid birthdate format. Please use YYYY-MM-DD.")

































