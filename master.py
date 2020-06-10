import random, sys

default_shapes = ["rock", "paper", "scissors"]
user_commands = ["!exit", "!rating"]

# Opens and reads previous ratings into a dictionary
rating_file = open("rating.txt", "r")
rating_list = [list(name_score.split()) for name_score in rating_file.readlines()]
rating_dict = {key:int(value) for key, value in rating_list}
rating_file.close()

name = input("Enter your name: ")
print(f"Hello, {name}")
if name not in rating_dict:
    rating_dict[name] = 0

shapes = input("Enter a list of possible shapes separated only by a comma: ").split(",")
if shapes == ['']:
    shapes = default_shapes
print(shapes)
print("Okay, let's start")

def lose_against(user_input):
        input_index = shapes.index(user_input)
        n_losing_shapes = int((len(shapes) -1) / 2) # How many shapes should lose against the input?
        lose_list = []
        shape_index = input_index - 1
        while len(lose_list) < n_losing_shapes: # Loops through the list backwards, adding losing shapes.
            lose_list.append(shapes[shape_index])
            shape_index -= 1
        return lose_list

# The game loop
while True:
    user_input = input()
    comp_shape = random.choice(shapes)

    # Input validation and commands
    if user_input not in user_commands and user_input not in shapes:
        print("Invalid input")
        continue
    if user_input == "!exit":
        print("Bye!")
        sys.exit()
    if user_input == "!rating":
        print(f"Your rating: {rating_dict[name]}")
        continue

    # Win and loss conditions
    lose_list = lose_against(user_input)
    if comp_shape == user_input:
        print("There is a draw ({})".format(comp_shape))
        rating_dict[name] += 50
    elif comp_shape in lose_list:
        print("Well done. Computer chose {} and failed".format(comp_shape))
        rating_dict[name] += 100
    else:
        print("Sorry, but computer chose {}".format(comp_shape))
