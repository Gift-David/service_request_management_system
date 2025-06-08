# 

from storage.file_handler import read_json

def client_history(email):
    requests = read_json("storage/data/requests.json")
    for request in requests:
        if request["email"] == email:
            print(f"Email: {request["email"]}, Type: {request["type"]}, Description: {request["description"]}, Priority: {request["priority"]}, Status: {request["status"]}, Date Logged: {request["date_logged"]}, Deadline: {request["deadline"]}")