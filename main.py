from clients.add import add_client
from clients.delete import delete_client
from clients.view import view_clients
from clients.update import update_client
from requests.log import log_request
from requests.history import client_history
from requests.update_status import update_status
from requests.view_requests import view_requests
from storage.file_handler import read_json
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


# def validate_priority(priority):
#     while True:
#         if priority == "high":
#             priority = "high"
#         elif priority == "low":
#             priority = "low"
#         elif priority =="medium":
#             priority = "medium"
#         else:
#             priority = str(input("Invalid priority. Enter low/high/medium")).lower().strip()
#         break

# def validate_status(status):
#     while True:
#         if status == "pending":
#             status = "pending"
#         elif status == "in-progress":
#             status = "in-progress"
#         elif status =="completed":
#             status = "completed"
#         else:
#             status = str(input("Invalid Status. Enter pending/in-progress/completed")).lower().strip()

def new_request():
    email = str(input("Enter the client's Email: "))
    type = str(input("Enter the type of Service: "))
    description = str(input("Enter the description of the service: "))
    priority = str(input("Enter the priority (low/high/medium)")).lower().strip()
    # validate_priority(priority)
    status = str(input("Enter the status (pending/in-progress/completed): ")).lower().strip()
    # validate_status(status)
        
    deadline = str(input("Enter the expected deadline"))

    new_request = {
        "email": email,
        "type": type,
        "description": description,
        "priority": priority,
        "status": status,
        "date_logged": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "deadline": deadline
    }

    log_request(new_request)

def update_status_():
    requests = read_json("storage/data/requests.json")
    email = str(input("Enter the Email: "))
    for request in requests:
        if request["email"] == email:
            print(f"The currnt status is {request["status"]}")
    status = str(input("Enter the new status"))
    update_status(email, status)


def history():
    email = str(input("Enter the Email: "))
    client_history(email)


def main():
    while True:
        main_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError as e:
            print(f"Invalid input: {e}")
        else:
            if choice == 1:
                client_menu()
                client_choice = int(input("Choose an option: "))
                if client_choice == 1:
                    view_clients()
                elif client_choice ==2:
                    new_client()
                elif client_choice == 3:
                    update_client_()
                elif client_choice == 4:
                    remove_client
                elif client_choice == 5:
                    pass
                else:
                    print("Invalid input")
                    break
                    
            elif choice == 2:
                request_menu()
                request_choice = int(input("Choose an option: "))
                if request_choice ==1:
                    view_requests()
                elif request_choice == 2:
                    new_request()
                elif request_choice == 3:
                    update_status_()
                elif request_choice == 4:
                    history()
                elif request_choice == 5:
                    pass
                else:
                    print("Invalid input") 
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid input")


if __name__ == "__main__":
    main()