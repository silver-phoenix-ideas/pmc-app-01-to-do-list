# Configuration
filename = "to_do_list.txt"


def get_todo_list(filename=filename):
    """ Reads the contents of a text file and returns a to-do list. """
    with open(filename) as file:
        todo_list = file.read().split("\n")
    return todo_list


def save_todo_list(todo_list, filename=filename):
    """ Saves the contents of a to-do list in a text file. """
    with open(filename, 'w') as file:
        file.write("\n".join(todo_list))


def display_todo_list(todo_list):
    """ Prints out to-do list items and their numbers in the console. """
    for index, todo_item in enumerate(todo_list, start=1):
        print(index, "-", todo_item)
