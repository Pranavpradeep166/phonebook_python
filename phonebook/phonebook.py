pb = {}

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Name")
    print("4. Update Email")
    print("5. Update Phone Number")
    print("6. Delete Contact")
    print("7. Exit")

    choice = int(input("Enter the choice: "))

    if choice == 7:
        print("---------Exiting----------")
        break

    if 1 <= choice <= 6:
        if choice == 1:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            count = int(input("Enter the count of phone numbers: "))
            ph = []

            for i in range(count):
                num = int(input("Enter phone number: "))
                ph.append(num)

            # contact_info = {"name": name, "email": email, "phno": ph}
            contact_info={}
            contact_info["name"]=name
            contact_info["email"]=email
            contact_info["phno"]=ph    
            pb[name] = contact_info
            print(f"Contact {name} added successfully.")

        elif choice == 2:
            if not pb:
                # pb empty aanonn nokkum
                print("No contacts available.")
            else:
                for contact_name, contact_info in pb.items():
                    print(f"Name: {contact_info['name']}")
                    print(f"Email: {contact_info['email']}")
                    print(f"Phone Numbers: {contact_info['phno']}")
                    print("-" * 40)

        elif choice == 3:
            name_to_update=input("enter the name")
            if name_to_update in pb:
                new_name=input("enter the new name")
                pb[name_to_update]["name"]=new_name
                a=pb.pop(name_to_update)     
                # confusion
                pb[new_name]=a
                print("-----Phone Book updated-----")
                print(pb)
            else:
                print("enter a valid name")   
                
        elif choice == 4:
            name_to_update=input("Enter the name for which you want to update the email: ")
            if name_to_update in pb:
                new_email=input("enter the new email")
                pb[name_to_update]["email"]=new_email
                print(f"Email updated for {name_to_update}")
                print("-----Phone Book updated-----")
                print(pb)
            else:
                print("enter the valid name for the email to be updated")

        elif choice == 5:
            name_to_update=input("Enter the name for which you want to update the phone no: ")
            if name_to_update in pb:
                phone_to_update=int(input("enter the number to bee updated: "))
                new_numeber=int(input("enter the new number: "))
                z=pb[name_to_update]["phno"]
                c=z.index(phone_to_update)
                z[c]=new_numeber
                pb[name_to_update]["phno"]=z
                print("-----Phone Book updated-----")
                print(pb)
            else:
                print("enter an existing name ")

        elif choice == 6:  
            name_to_update=input("Enter the name for which you want to delete the contact: ")
            if name_to_update in pb:
                delete_contact=pb.pop(name_to_update)
                print(f"Contact {name_to_update} deleted successfully.")
                print("-----Phone Book updated-----")
                print(pb)
            else:
                print("enter an existing name to delete")