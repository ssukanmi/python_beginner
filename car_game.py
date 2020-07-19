"""
A simple car start and stop game engine
Have fun trying the various commands
"""

command = ""
car_started = False
while True:
    command = input("> ").lower()
    if command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit
    """)
    elif command == "start":
        if not car_started:
            car_started = True
            print("Car started... Ready to go!")
        else:
            print("Car already started before")
    elif command == "stop":
        if car_started:
            car_started = False
            print("Car stopped")
        else:
            print("Car already stopped before")
    elif command == "quit":
        print("Thank you for playing")
        break
    else:
        print("I don't understand")
