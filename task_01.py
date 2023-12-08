class NoContactsError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide a name."
        except NoContactsError:
            return "No contacts found."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner


def parse_input(user_input, expected_args=None):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def hello():
    return "How can I help you?"

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError
        
@input_error
def show_phone(args, contacts):
    name = args[0]

    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        raise NoContactsError
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    
    return result
    
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError as e:
                print(f"Error: {e}")
        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except ValueError as e:
                print(f"Error: {e}")
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()