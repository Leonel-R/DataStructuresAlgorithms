#Big O Notation is used to measure the worst-case complexity of an algorithm 
#NOT measured in time or bytes (due to possible hardware differences)

#This is O(1) - constant
colors = ['green', 'yellow', 'blue', 'pink']

def constant(colors):
    print(colors[2])	

constant(colors)

#This is O(n) - linear 
colors = ['green', 'yellow', 'blue', 'pink']

def linear(colors):
    for color in colors:
        print(color)	

linear(colors)

#This is O(n2) - quadratic 
colors = ['green', 'yellow', 'blue']

def quadratic(colors):
    for first in colors:
        for second in colors:
            print(first,second)	

quadratic(colors)

#This is O(n3) - cubic 
colors = ['green', 'yellow', 'blue']

def cubic(colors):
    for color1 in colors:
        for color2 in colors:
            for color3 in colors:
                print(color1,color2,color3)	

cubic(colors)

#calculating Big O Notation
colors = ['green', 'yellow', 'blue','pink','black','white','purple'] # O(1)
other_colors = ['orange','brown'] # O(1)

def complex_algorithm(colors):
    color_count = 0               # O(1)

    for color in colors:
        print(color)              # O(n)
        color_count += 1          # O(n)
    
    for other_color in other_colors:
        print(other_color)        # O(m)
        color_count += 1          # O(m)
    
    print(color_count)            # O(1)
    
complex_algorithm(colors)         # O(4 + 2n + 2m)

# Simplifying Big O Notation

# 1) Remove constants
# O(4 + 2n + 2m) -> O(n + m)

# 2) Different variables for different inputs
# O(n + m)   was already done

# 3) Remove smaller terms
# for example: if we have O(n + n2) it becomes O(n2)