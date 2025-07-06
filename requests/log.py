# 

from storage.file_handler import read_json, write_json, append_to_json

def log_request(new_request):
    requests = read_json("storage/data/requests.json")
    clients = read_json("storage/data/clients.json")
    for client in clients:
        if not client["email"] == new_request["email"]:
            print("The email you entered is not a registered client, register client to continue")
            return
        else:
            requests.append(new_request)
            write_json("storage/data/requests.json", requests)
            print("Request logged successfully")
            return

    
        
    
    