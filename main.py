prompt = "Enter to do item: "
todo_list = []

while True:
    user_input = input(prompt)
    todo_list.append(user_input.title())
    print(todo_list)
