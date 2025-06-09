from clients.add import add_client
from clients.delete import delete_client
from clients.view import view_clients
from clients.update import update_client
from requests.log import log_request
from requests.history import client_history
from requests.update_status import update_status
from requests.view_requests import view_requests

from datetime import datetime




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

def new_client():
    name = str(input("Enter clients name: "))
    email = str(input("Enter clients email: "))
    phone = str(input("Enter clients phone number: "))
    address = str(input("Enter clients address: "))

    new_client = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }

    add_client(new_client)

def update_client_():
    email = str(input("Enter clients email: "))
    key = str(input("Enter the information you want to update: "))
    value = str(input("Enter the current {key}"))
    update_value = input("Enter the new {key}")
    update_client(email, key, value, update_value)

def remove_client():
    email = str(input("Enter clients email: "))
    delete_client(email)

def new_request():

    new_request = {
        "email": email,
        "type": type,
        "description": description,
        "priority": priority,
        "status": status,
        "date_logged": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "deadline": deadline
    }



def main():
    while True:
        main_menu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            client_menu()
            client_choice = int(input("Choose an option: "))
            if client_choice == 1:
                view_clients()
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