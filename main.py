from database import add_entry, get_entries

menu = """
Please select one of the following option:
1. Add new entry
2. View entries
3. Exit

Your selection: """


def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter date: ")
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}")


welcome = "Welcome to your diary!"
print(welcome)
user_input = input(menu)

while user_input != "3":
    if user_input == "1":
        prompt_new_entry()
    elif user_input == "2":
        view_entries(get_entries())
    else:
        print("Invalid options, please try again")

    user_input = input(menu)
