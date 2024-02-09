import os

if __name__ == "__main__":
    print("Welcome to Espeak Robot 0.1 \n")

    while True:  
        word = input("Enter the word you want the Robot to say: ")
        if word == "q":
            os.system("espeak-ng goodbye")
            break
        
        command = f"echo {word} | espeak-ng"
        os.system(command)
        