

def start_guide():
    print("--- Welcome to my Linux Tool ---")
    print("Options: 1 for File list, 2 for Path, 3 to Exit")

while True:
    start_guide()
    user_input = input("Choose something: ")
    
    if user_input == '1':
        print("Command: 'ls' - usage: list files in folder")
    elif user_input == '2':
        print("Command: 'pwd' - usage: shows where you are right now")
    elif user_input == '3':
        print("Bye Bye! Thanks for using.")
        break
    else:
        print("Galat input! Try again.") 
