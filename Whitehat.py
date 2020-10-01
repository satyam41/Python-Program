# Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
def radius_circle(x):
    inner_area_square = x**2
    outer_area_square = 2*x**2
    diff = outer_area_square - inner_area_square
    return diff
radius = float(input("Enter radius of the circle : "))
print(f"Difference between outer square and inner square {radius_circle(radius)}")


# Create a function that takes a word and returns the new word without including the first character. Examples new_word("apple") ➞ "pple" new_word("cherry") ➞ "herry" new_word("plum") ➞ "lum"
def new_word(x):
    print(x[1:])
new_word('satyam')

# Create a function to count spaces.
def space(x):
    for i in range(len(x)):
        if x[i] == " ":
            return True
        else:
            return False
space('satyam krishna')