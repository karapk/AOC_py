initial_location = 50
#With opens the file in read mode and ensures it is properly closed after its suite finishes
with open("day1/sampledata.txt", "r") as data:
    
    # Iterate through each line in the file
    for line in data:
        
        # Remove any leading/trailing whitespace (like the newline character) for clean checking
        # line = line.strip("RL")
        # print(f"Processing command: {line}")
        # Check for 'L' (Left Turn)
        if "L" in line:
            print(f"**Left turn detected** for command: {line}")
            leftStrip = line.strip("L")
            print(f"After stripping 'L': {leftStrip}")
            print(type(leftStrip))
            current_location = initial_location - int(leftStrip)
            print(f"New location after left turn: {current_location}")
            if current_location < 0:
                current_location = 100 + current_location
                print(f"Location on dial: {current_location}")
        # Check for 'R' (Right Turn)
        elif "R" in line:
      
            print(f"**Right turn detected** for command: {line}")

        else:
           print(f"Unknown command: {line}")

# print(data)

# lines =data.split("\n")
# print("Lines:", lines)

# def L_turn(data):
#     lines = data.split("\n")
#     result = []
#     for line in lines:
#         if line:
#             direction, value = line[0], int(line[1:])
#             if direction == 'L':
#                 result.append(('Left', value))
#             elif direction == 'R':
#                 result.append(('Right', value))
#     return result

# print(L_turn(data))