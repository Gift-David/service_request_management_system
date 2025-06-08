# 

from storage.file_handler import read_json, write_json, append_to_json

def log_request(new_request):
    requests = read_json("storage/data/requests.json")
    requests.append(new_request)
    write_json("storage/data/requests.json", requests)
    print("Request logged successfully")