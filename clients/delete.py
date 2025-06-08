# 

from storage.file_handler import read_json, delete_json_record

def delete_client(email):
    
    clients = read_json("storage/data/clients.json")
    """
    for client in clients:
        if not client.get("email").lower() == email.lower():
            print(f"Error: {email} not found")
            # return False
            break
    """      
    
    for client in clients:
        if client["email"] == email:
            while True:
                print(f"{client["name"]:<8} | {client["email"]:<25} | {client["phone"]:<11} | {client["address"]:<10}")
                confirm_msg = input("You're about to delete this product. Confirm (yes/no)").lower().strip()
                if confirm_msg == "no":
                    break
                elif confirm_msg == "yes":
                    delete_json_record("storage/data/clients.json", key="email", value=email)
                    print(f"{client["name"]} deleted successfully")
                else:
                    print(f"Invalid input. Enter Yes or No")
        
    
