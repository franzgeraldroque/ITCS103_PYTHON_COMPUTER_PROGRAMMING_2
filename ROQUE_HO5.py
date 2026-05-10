import os

def dream_file():
    filename = "Dream.txt"

    while True:
        print("\n===== DREAMS FILE MANAGER =====\n")
        print("1. Read inspriring messages.")
        print("2. Add a new inspiring message.")
        print("3. Rewrite the entire inspiring message.")
        print("4. Exit the program.")

        choice = input("\nPlease select a number ----> ")

        if choice == '1':
            os.system("cls")
            print("===== Inspiring Messages =====")

            if os.path.exists(filename):
                file = open("Dream.txt", "r")
                content = file.read()
                file.close()
                print(content)
            else:
                print("File does not exist!!")
            continue
                
        elif choice == "2":
            os.system("cls")
            new_message = input("Enter a new inspiring message ----> ")
            file = open("Dream.txt", "a")
            file.write("\n" + new_message)
            file.close()
            print("\nNew inspiring message added!")
            continue

        elif choice == "3":
            os.system("cls")
            print("\nWARNING!!! This will overwrite all the inspiring messages in the file.")
            confirmation = input("type YES to continue ----> ").upper()

            if confirmation == "YES":
                new_set = input("Write your new set of inspiring messages ---->")
                file = open("Dream.txt", "w")
                file.write(new_set)
                file.close()
                print("File has overwritten.")
            else:
                print("Action cancelled.")
            continue
        
        elif choice == "4":
            print("Closing the program.....")
            break

        else:
            print("Invalid input, Please try again")
            continue

dream_file()
