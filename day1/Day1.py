currentlocation = 50

counter = 0


def left_turn(currentlocation, turn_value):
        new_location = currentlocation - turn_value
        while new_location < 0:
            new_location = 100 + new_location
        print(f"Adjusted location after Left turn: {new_location}")
        return new_location

def right_turn(currentlocation, turn_value):
    new_location = currentlocation + turn_value
    while new_location > 99:
        new_location = new_location - 100
    print(f"Adjusted location after Right turn: {new_location}")
    return new_location

with open("day1/sampledata.txt", "r") as file:

    for line in file:
        # Check for 'L' (Left Turn) 
        if "L" in line:
            # print(f"**Left turn detected** for command: {line}")
            leftvalue = int(line.strip("L"))
            print(f"Turn value after stripping 'L': {leftvalue}")
            currentlocation = left_turn(currentlocation, leftvalue)
            if currentlocation == 0:
                counter += 1
                print(f"Counter incremented to: {counter}")
        # Check for 'R' (Right Turn)
        elif "R" in line:
            # print(f"**Right turn detected** for command: {line}")
            rightvalue = int(line.strip("R"))
            print(f"Turn value after stripping 'R': {rightvalue}")
            currentlocation = right_turn(currentlocation, rightvalue)
            if currentlocation == 0:
                counter += 1
                print(f"Counter incremented to: {counter}")
print(f"Final counter value: {counter}")
        