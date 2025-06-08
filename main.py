from clients.add import add_client
from clients.delete import delete_client




def main_menu():
    main_menu = ["clients", "requests", "exit"]
    i = 1
    for item in main_menu:
        print(f"{i}. {item.title()}")
        i += 1

def client_menu():
    client_menu = ["view client", "add client", "update client", "delete client", "main menu"]
    i = 1
    for item in client_menu:
        print(f"{i}. {item.title()}")
        i += 1

def request_menu():
    request_menu = ["view requests", "log requests", "update requests", "client history", "main menu"]
    i = 1
    for item in request_menu:
        print(f"{i}. {item.title()}")
        i += 1

# name = str(input("Enter clients name: "))
#     email = str(input("Enter clients email: "))
#     phone = str(input("Enter clients phone number: "))
#     address = str(input("Enter clients address: "))

#     new_client = {
#         "name": name,
#         "email": email,
#         "phone": phone,
#         "address": address
#     }

#     add_client(new_client)
#     delete_client(email)



def main():
    while True:
        main_menu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            client_menu()
            client_choice = int(input("Choose an option: "))
            if client_choice == 1:
                pass
            elif client_choice ==2:
                pass
            elif client_choice == 3:
                pass
            elif client_choice == 4:
                pass
            elif client_choice == 5:
                pass
                
        elif choice == 2:
            request_menu()
        elif choice == 3:
            break
        else:
            print("Invalid input")

    

main()