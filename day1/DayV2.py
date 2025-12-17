currentlocation = 50

counter = 0


def left_turn(currentlocation, turn_value):
        new_location = currentlocation - turn_value
        return new_location

def right_turn(currentlocation, turn_value):
    new_location = currentlocation + turn_value
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
            elif currentlocation < 0:
                while currentlocation < 0:
                    print(f"currentlocation vs previouslocation: 100 - {currentlocation} ")
                    if (previouslocation != 0) and (currentlocation <= 0):
                        counter += 1
                    print(f" counter incremented due to LEFT turn crossing zero. New counter: L{counter}")
                    currentlocation = 100 + currentlocation
                    print(f"currentlocation vs previouslocation: 100 - {currentlocation} ")
                    
                
        # Check for 'R' (Right Turn)
        elif "R" in line:
            rightvalue = int(line.strip("R"))
            previouslocation = currentlocation
            currentlocation = right_turn(currentlocation, rightvalue)
            print(f" RIGHT turn from {previouslocation} to {currentlocation}!")
            if currentlocation == 0:
                counter += 1
                print(f" counter incremented due to RIGHT turn to zero. New counter: R{counter}")
            elif currentlocation > 99:
                while currentlocation > 99:
                    print(f" right currentlocation vs previouslocation: {currentlocation} - 100 ")
                    if (previouslocation != 0) and (currentlocation > 99):
                        counter += 1
                    print(f" counter incremented due to RIGHT turn crossing zero. New counter: R{counter}")
                    currentlocation = currentlocation - 100
                    print(f"currentlocation vs previouslocation: {currentlocation} - 100 ")
                
print(f"Final counter value: {counter}")
        