# Module for adding clients

from storage.file_handler import read_json, write_json, append_to_json

def add_client(new_client):
    clients = read_json("storage/data/clients.json")
    for client in clients:
        if client["email"] == new_client["email"]:
            print(f"{new_client["email"]} already exists, enter a new client")
            return
    clients.append(new_client)
    write_json("storage/data/clients.json", clients)
    print("Client added successfully")