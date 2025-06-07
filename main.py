from clients.add import add_client

def main():
    name = str(input("Enter clients name: "))
    email = str(input("Enter clients email: "))
    phone = str(input("Enter clients phone number: "))
    address = str(input("Enter clients address: "))

    new_client = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }

    add_client(new_client)

main()