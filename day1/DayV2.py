currentlocation = 50

counter = 0


def left_turn(currentlocation, turn_value):
        new_location = currentlocation - turn_value
        while new_location < 0:
            new_location = 100 + new_location
        return new_location

def right_turn(currentlocation, turn_value):
    new_location = currentlocation + turn_value
    while new_location > 99:
        new_location = new_location - 100
    return new_location

with open("day1/sampledata.txt", "r") as file:

    for line in file:
        
        # Check for 'L' (Left Turn) 
        if "L" in line:
            leftvalue = int(line.strip("L"))
            previouslocation = currentlocation
            currentlocation = left_turn(currentlocation, leftvalue)
            print(f" LEFT turn from {previouslocation} to {currentlocation}!")
            if currentlocation == 0:
                counter += 1
                print(f" counter incremented due to LEFT turn to zero. New counter: {counter}")
                
        # Check for 'R' (Right Turn)
        elif "R" in line:
            rightvalue = int(line.strip("R"))
            previouslocation = currentlocation
            currentlocation = right_turn(currentlocation, rightvalue)
            print(f" RIGHT turn from {previouslocation} to {currentlocation}!")
            if currentlocation == 0:
                counter += 1
                print(f" counter incremented due to RIGHT turn to zero. New counter: {counter}")
                
print(f"Final counter value: {counter}")
        