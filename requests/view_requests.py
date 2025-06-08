# 

from storage.file_handler import read_json

def view_requests():
    requests = read_json("storage/data/requests.json")
    for request in requests:
        print(f"Email: {request["email"]}, Type: {request["type"]}, Description: {request["description"]}, Priority: {request["priority"]}, Status: {request["status"]}, Date Logged: {request["date_logged"]}, Deadline: {request["deadline"]}")
        