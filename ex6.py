#establish and assign variable, establish and seed in new string variable
types_of_people = 10
x = f"There are {types_of_people} types of people."

#establish string variables and seed both in new string variable
binary  = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print both new string variables
print(x)
print(y)

#duh
print(f"I said: {x}")
print(f"I also said: '{y}'")

#establish variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#print joke evaluation
print(joke_evaluation.format(hilarious))

#establish string variables
w = "This is the left side of..."
e = "a string with a right side."

#print concatenated strings
print(w + e)
