'''
Made by Kartikeya Vakharia. 
4/21/2023
This program is a simple guessing high/low challenge game that saves high scores in a file named High-Scores.txt. 
Anyway, people were using ChatGPT so I just decided to give my best shot at beating their scripts. 
'''
# Libraries
import random
import getpass
import json
import os
from cryptography.fernet import Fernet

# Initialize the high score list
high_scores = []

# Generate the encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)


# Read the encrypted login credentials file
login_creds = {}
if os.path.isfile('login-creds.key'):
    try:
        with open('login-creds.key', 'rb') as f:
            encrypted_login_creds = f.read()
            # Generate the key from the saved key data
            key = b'...'
            cipher_suite = Fernet(key)
            decrypted_login_creds = cipher_suite.decrypt(encrypted_login_creds)
            login_creds = json.loads(decrypted_login_creds.decode())
    except (ValueError, TypeError, Fernet.InvalidToken):
        pass
    # If the key is invalid or the data is corrupted, delete the file
    os.remove('login-creds')

# Generate the encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Variables
playAgain = "yes"
totalRounds = 0
totalWins = 0
maxGuesses = 5

# Login Loop
while True:
    print("1. Login")
    print("2. Create account")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        # Login
        while True:
            username = input("Enter your username: ")
            if username in login_creds:
                password = getpass.getpass("Enter your password: ")
                if login_creds[username] == password:
                    print("Login successful!")
                    break
                else:
                    print("Invalid password. Please try again.")
            else:
                print("Invalid username. Please try again.")
    elif choice == "2":
        # Create account
        while True:
            username = input("Enter a new username: ")
            if username in login_creds:
                print("Username already taken. Please choose a different one.")
            else:
                password = getpass.getpass("Enter a password: ")
                login_creds[username] = password
                print("Account created successfully!")
                break
    else:
        print("Invalid choice. Please try again.")
        continue
    
    # Encrypting and saving the login credentials file
    encrypted_login_creds = cipher_suite.encrypt(json.dumps(login_creds).encode())
    with open('login-creds', 'wb') as f:
        f.write(encrypted_login_creds)
    
    break

# Main Loop
while playAgain.lower() == "yes":
    # Ask the user if they want to play the game.
    playGame = input(f"Hi {username}, do you want to play the high/low game? (Say Yes/No) \n")

    if playGame.lower() == "yes":
        # Initialize the game.
        numberGuesses = 0
        secretNumber = random.randint(0, 100)
        while numberGuesses < maxGuesses:
            # Get the users guess
            try:
                userGuess = int(input("Guess a number between 1-100 \n"))
            except ValueError:
                print("Invalid input. Please enter a number between 1-100.")
                continue

            # Checking to see if the guess is correct
            if userGuess == secretNumber:
                numberGuesses += 1
                print(f"Nice job {username}! You guessed the correct number in {numberGuesses} times!")
                totalRounds += 1
                totalWins += 1
                break
            elif userGuess < secretNumber:
                print("That's too low!")
            else:
               
                print("That's too high!")
            numberGuesses += 1

        # Checks if the user ran out of guesses
        if numberGuesses == maxGuesses:
            print(f"Sorry {username}. You ran out of guesses The number was {secretNumber}.")

        # Adding the scores to the high scores list
        score = (username, totalWins)
        high_scores.append(score)

        # Sorting through the high scores list in descending order by score
        high_scores = sorted(high_scores, key=lambda x: x[1], reverse=True)

        # Writing the top 5 scores

        with open ('High-Scores.txt', 'w') as f:
            for username, totalWins in high_scores[:5]:
                f.write(f"{username},{totalWins}\n")

      # Encrypting and saving the login credentials file
        login_creds = {username: password}
        encrypted_login_creds = cipher_suite.encrypt(json.dumps(login_creds).encode())
        with open(r'C:\Users\karti\OneDrive\Desktop\Programming and Robotics\login-creds', 'wb') as f:
            f.write(encrypted_login_creds)

        playAgain = input("Do you want to play again? (yes/no)  ")
    else:
        playAgain = 'no'

print(f"Thanks for playing {username}! You won {totalWins} out of {totalRounds} rounds.")