import os
import pathlib
import configuration.config as config
import localization.texts as txt


def get_data_path(relative_path: str):
    """ Gets the absolute path to the resource. Needed for PyInstaller. """
    app_root = pathlib.Path(__file__).parents[1]
    resource_path = str(pathlib.Path(app_root, relative_path))

    return resource_path


def get_todo_list(filename: str = config.FILENAME):
    """ Reads the contents of a text file and returns a to-do list. """
    pathlib.Path(config.FILE_DIRECTORY).mkdir(exist_ok=True)
    filepath = pathlib.Path(config.FILE_DIRECTORY, config.FILENAME)
    todo_list = []

    if os.path.exists(filepath):
        with open(filepath) as file:
            todo_list = file.read().split("\n")
    else:
        with open(filepath, "w") as file:
            pass

    todo_list = list(filter(None, todo_list))

    return todo_list


def save_todo_list(todo_list: list, filename: str = config.FILENAME):
    """ Saves the contents of a to-do list in a text file. """
    filepath = pathlib.Path(config.FILE_DIRECTORY, config.FILENAME)

    with open(filepath, 'w') as file:
        file.write("\n".join(todo_list))


def display_todo_list(todo_list: list):
    """ Prints out to-do list items and their numbers in the console. """
    for index, todo_item in enumerate(todo_list, start=1):
        print(index, "-", todo_item)


def parse_todo_item(todo_item: str):
    """
    Formats and validates the to-do item. If valid, the formatted
    to-do item is returned. Otherwise, an exception is raised.
    """
    todo_item = todo_item.strip().title()

    if not todo_item:
        raise ValueError(txt.error_empty_string)

    return todo_item


def add_todo_item(todo_item: str):
    """
    Adds the to-do item to the end of the to-do list.
    """
    todo_item = parse_todo_item(todo_item)
    todo_list = get_todo_list()
    todo_list.append(todo_item)
    save_todo_list(todo_list)

    return todo_item


def edit_todo_item(index: int, todo_item: str):
    """
    Edits the to-do item at the given index by
    overwriting its value with the one provided.
    """
    todo_item = parse_todo_item(todo_item)

    todo_list = get_todo_list()
    todo_list[index] = todo_item
    save_todo_list(todo_list)


if __name__ == "__main__":
    current_module = pathlib.Path(__file__).stem.capitalize()
    defined_functions = list(filter(callable, globals().values()))

    print("\n" + current_module + " Module:")

    for defined_function in defined_functions:
        print()
        help(defined_function)
        print("-" * 80)
