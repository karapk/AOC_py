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
                print(f" COUNTER incremented due to LEFT turn ON ZERO. New counter: L{counter}")
            elif currentlocation < 0:
                # Calculate how many times we crossed zero
                crossings = abs(currentlocation) // 100 + 1
                counter += crossings
                print(f" COUNTER incremented by {crossings} due to LEFT turn crossing zero. New counter: L{counter}")
                # Adjust position to be within range
                currentlocation = currentlocation % 100
                    
                
        # Check for 'R' (Right Turn)
        elif "R" in line:
            rightvalue = int(line.strip("R"))
            previouslocation = currentlocation
            currentlocation = right_turn(currentlocation, rightvalue)
            if currentlocation == 0:
                counter += 1
                print(f" COUNTER incremented due to RIGHT turn ON ZERO. New counter: R{counter} position {currentlocation}")
            elif currentlocation > 99:
                while currentlocation > 99:
                    if (currentlocation > 99):
                        print(f" COUNTER incremented due to RIGHT turn crossing zero. New counter: R{counter} position {currentlocation}")
                        currentlocation = currentlocation - 100
                        print(f"New right turn position after adjustment: {currentlocation}")
                        counter += 1
                        print(f" COUNTER incremented due to RIGHT turn crossing zero. New counter: R{counter} position R{currentlocation}")
                
print(f"Final counter value: {counter}")
        