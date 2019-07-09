def greet(player):
    if player == "Shia":
        return "Welcome, Mr. LeBouf. Nice job on Transformers."
    else:
        return "Welcome, " + player

name1 = input("Enter player 1's name")
print(greet(name1)) # Notice that we're passing a variable as the argument for our greet function.

name2 = input("Enter player 2's name")
print(greet(name2))


# What datatype will be in the variable called name1 when we run this program?

# How did writing a greet function actually end up saving us time?