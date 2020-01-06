print("Its a car game. Give it a try")

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("car started..")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("car stopped..")
    elif command == "quit":
        break
    else:
        print("HELP: ")
        print("""""
start ---
stop ---
quit ---
        """)