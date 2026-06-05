with open('day5.in') as file:
    # .splitlines() puts every line it reads into a list. Using \n\n to check when there is a line with nothing in it, hence displayed as \n\n
    stack_strings, instructions = [i.splitlines() for i in file.read().strip("\n").split('\n\n')]       

# Makes every digit on the bottom line of the stacks instructions an int, replaces all the spaces with nothing (note: not using .strip() because it is a list)
# Learned also that you can just print an empty list without making it a string. Able to use ":" without any quotes to because remember, it's a dictionary
stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ", "")}

# Stores where all the values on the bottom row are in the line in a list called indexes. Uses enumerate
# Can specify 2 variables when using a for loop with enumerate to get number (index) and character
# Skips all characters that are spaces
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]



# Displays each stack in the stacks dict. /n used several times for formatting
def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print('\n')


def loadStacks():
    # stack_strings[:-1] - Checking all lines up to the last line in stack_strings
    # Remember, string here is still a list because we used .splitlines() 
    for string in stack_strings[:-1]:
        stack_num = 1
        # Checking each number on the bottom row
        # Inserting the letter to the front of the list with .insert()
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

# Clearing all data in the stacks with .clear()
def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()


def getStackEnds():
    answer = ""
    # For each stack, add the last letter from the stack to the answer. Adding works here because "answer" is equal to a string, and not an int
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

loadStacks()


# == PART 1 ==

# Storing each 3 number set into a list, and making all of the variables into inputs
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from", "").replace("to", "").strip().split(" ")
    instruction = [int(i) for i in instruction if i != ""]

    # Assigning each value to a variable
    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    # Moves the amount of crates specified from one stack to another.
    for crate in range(crates):
        # .pop() eliminates a specific item from a list. Putting nothing inside .pop() defaults it to deleting the last item in the list
        crate_removed = stacks[from_stack].pop()
        # Adding the removed crate to the new stack
        stacks[to_stack].append(crate_removed)

print("Answer for part 1:", getStackEnds())
