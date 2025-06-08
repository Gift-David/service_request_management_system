# 

from storage.file_handler import read_json, update_json_record

def update_status(email, new_status):
    requests = read_json("storage/data/requests.json")
    for request in requests:
        if request["email"] == email:
            update_json_record("storage/data/requsts.json", request["status"], request.get("status"), new_status)
            print(f"{email} status has been updated successfully to {new_status}")
