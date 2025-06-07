# Module for adding clients

from storage.file_handler import read_json, write_json, append_to_json

def add_client(new_client):
    clients = read_json("storage/data/clients.json")
    clients.append(new_client)
    write_json("storage/data/clients.json", clients)
    print("Client added successfully")