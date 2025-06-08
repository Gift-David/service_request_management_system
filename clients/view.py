# 

from storage.file_handler import read_json

def view_clients():
    clients = read_json("storage/data/clients.json")
    for client in clients:
        print(f"Name: {client["name"]}, Email: {client["email"]}, Phone: {client["phone"]}, Address: {client["address"]}")