# Define information for three people
person1 = {
    'Name': 'John Doe',
    'Email': 'johndoe@example.com',
    'Phone': '555-123-4567',
    'Address': '123 Main Street, Cityville'
}

person2 = {
    'Name': 'Jane Smith',
    'Email': 'janesmith@example.com',
    'Phone': '555-987-6543',
    'Address': '456 Elm Street, Townsville'
}

person3 = {
    'Name': 'Bob Johnson',
    'Email': 'bob@example.com',
    'Phone': '555-555-5555',
    'Address': '789 Oak Street, Villagetown'
}

# Print the information for each person
for person in [person1, person2, person3]:
    print(f"Name: {person['Name']}")
    print(f"Email: {person['Email']}")
    print(f"Phone: {person['Phone']}")
    print(f"Address: {person['Address']}")
    print()

