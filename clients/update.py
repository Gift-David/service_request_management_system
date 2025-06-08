# 

from storage.file_handler import read_json, update_json_record

def update_client(email, key, value, update_value):
    clients = read_json("storage/data/clients.json")
    for client in clients:
        if client["email"] == email:
            update_json_record("storage/data/clients.json", key, value, update_value)
            print(f"Clients {key} updated successfully to {update_value}")
        else:
            print("Email not found")