# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here
    students = ['Raul', 'Chris', 'Jordan']
    first_student = students[1]
    last_student = students[2]

    return[first_student,last_student]

# Call the function and print the result
print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    # your code here
    foods = ('spaghetti','burgers','tacos')
    meal = ''
    for food in foods:
        meal += food
    return meal

# Call the function and print the result
print('Exercise 2:', combine_foods())


# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # your code here
    foods = ('spaghetti','burgers','tacos')
    last_two_foods = foods[-2:]
    return last_two_foods


# Call the function and print the result
print('Exercise 3:', slice_foods())


# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    # your code here
    home_town = {
        'city': 'Manhattan',
        'state': 'New York',
        'population': 1646000,
    }

    return (f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')
# Call the function and print the result
print('Exercise 4:', hometown_info())
