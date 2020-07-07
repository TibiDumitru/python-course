
# 1. Starting from a list of numbers, how can we calculate their sum using one-liner ?
# Can you find a second way to do that ?


# 2. Find out how can you rewrite the next `for` statement using an elegant way:
my_list = ["orange", "apple", "strawberry", "blueberry", "banana"]
for index in range(len(my_list)):
    print(f"The element from index {index} is {my_list[index]}")


# 3. Find out how can you rewrite the next nested `for` loop using one-liner:
flat_list = []
nested_lists = [[1, 43, 54, 23, 5], [101, 32, 54, 85]]
for inner_list in nested_lists:
    for element in inner_list:
        flat_list.append(element)
print(flat_list)


# 4. Starting from an input string, create all permutations and all combinations.
# Example:
#   input: 'abc' =>
#                 ('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ... etc.
#                 ('a'), ('b'), ('c')
#                 ('a', 'b'), ('a', 'c'), ('b', 'c')


# 5. Write a Python function that retrieves 2 lists of numbers A and B from the user input
# and returns a tuple that contains the Union, Intersection, A \ B and B \ A of the two lists.


# 6. Create a file and fill it with random text. Write a Python function that reads the text,
# remove all stop words and write the new text in another file.


# 7. Rewrite the previous exercise using a Thread that does the work.


# 8. Write a Python script that make creates two Threads in order to communicate between them.
# The first one has to send a message (a string) to the other one and the latter has to print
# it to stdout. Use a safe way to send data from one thread to another.


# 9. Create 4 classes named Shape, Sphere, Pyramid and Cylinder. The first one is the
# base (super) class and the other ones extends Shape. The classes has to implement the
# next 2 methods: `calculate_area()` and `calculate_volume()`. Use the "power" of
# Abstract Classes/Methods.


# 10. Create a Binary Tree. It needs to have a method that prints the entire
# tree from right to left (descending order).
