# start-"car is running", stop-"car has stop", help-print the commands, quit-program terminate

command_start = str("start")
# is_started boolean is checking the engine state (started/stopped)
is_started = False
command_stop = str("stop")
command_help = str("help")
command_quit = str("quit")
enter_command = ""

while True: 
    enter_command = input(">").lower()
    if enter_command == command_help:
        print(command_start)
        print(command_stop)
        print(command_help)
        print(command_quit)
    elif enter_command == command_start:
        if is_started == True:
            print("The car is already running.")
        elif is_started == False:
            is_started = True
            print("The car has started.")
    elif enter_command == command_stop:
        if is_started == False:
            print("The car has already stopped.")
        elif is_started == True:
            is_started = False
            print("The car stopped.")
    elif enter_command == command_quit:
        print("Program terminated.")
        break
    else:
        print("Sorry, don't understand...")
