class ContactBook:
    def __init__(self, id, last_name, first_name, middle_name, organization, work_phone, personal_phone):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone


fields = ['last_name', 'first_name', 'middle_name', 'organization', 'work_phone', 'personal_phone']


def read_file(file: str) -> list:
    contact_data = []
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split("|")
            contact = ContactBook(*data)
            contact_data.append(contact)
    return contact_data


def write_file(contacts: list, file: str) -> None:
    with open(file, 'w') as file:
        for contact in contacts:
            line = "|".join([
                str(contact.id),
                contact.last_name,
                contact.first_name,
                contact.middle_name,
                contact.organization,
                contact.work_phone,
                contact.personal_phone
            ])
            file.write(line + '\n')


def display_contacts(contacts: list, page_size: int, page: int) -> None:
    if not isinstance(page_size, int) or not isinstance(page, int) or page_size <= 0 or page <= 0:
        raise ValueError("Please enter correct data!")
    page_amount = -(-len(contacts) // page_size)
    if page > page_amount:
        page = page_amount
    start = page_size * (page - 1)
    end = start + page_size
    for i in contacts[start:end]:
        for key, value in i.__dict__.items():
            print(f"{key}: {value}")
        print('\n')


def insert_contact(contacts: list, file_path: str) -> None:
    try:
        max_id = max([int(contact.id) for contact in contacts])
    except ValueError:
        max_id = 0
    data = {"id": max_id + 1}
    for field in fields:
        value = input(f"{field.replace('_', ' ')}: ")
        data[field] = value.strip()
    new_contact = ContactBook(**data)
    validate_numbers(new_contact)
    contacts.append(new_contact)
    write_file(contacts, file_path)


def validate_numbers(contact: ContactBook) -> None:
    try:
        int(contact.work_phone)
        int(contact.personal_phone)
    except ValueError:
        raise ValueError("Phone numbers must be numbers!")


def update_contact(contacts: list, id: int, file_path: str) -> None:
    ids = [int(contact.id) for contact in contacts]
    if id not in ids:
        raise ValueError("Please enter correct id!")

    contact = contacts[id - 1]
    print(f"Updating contact: \n{contact.last_name}, {contact.first_name}, {contact.middle_name}")
    contact.last_name = input("Last Name: ")
    contact.first_name = input("First Name: ")
    contact.middle_name = input("Middle Name: ")
    contact.organization = input("Organization: ")
    contact.work_phone = input("Work Phone: ")
    contact.personal_phone = input("Personal Phone: ")
    validate_numbers(contact)
    write_file(contacts, file_path)


def search_contact(contacts: list, search_word: str) -> None:
    search_word = str(search_word)
    for contact in contacts:
        if (
                search_word.lower() in contact.last_name.lower()
                or search_word.lower() in contact.id
                or search_word.lower() in contact.first_name.lower()
                or search_word.lower() in contact.middle_name.lower()
                or search_word.lower() in contact.organization.lower()
                or search_word.lower() in contact.work_phone.lower()
                or search_word.lower() in contact.personal_phone.lower()
        ):
            for key, value in contact.__dict__.items():
                print(f"{key}: {value}")
            print('\n')


def main():
    file_path = 'db.txt'
    contacts = read_file(file_path)

    while True:
        print("\nAction list:")
        print("1. Display contacts")
        print("2. Add contact")
        print("3. Edit contact")
        print("4. Search contacts")
        print("5. Exit")
        choice = input("Choice: ")

        if choice == '1':
            page_size = input("Page size: (default 5): ")
            page = input("Page: (default 1): ")
            try:
                page = int(page)
                page_size = int(page_size)
            except ValueError:
                page = 1
                page_size = 5
            display_contacts(contacts, page_size, page)
        if choice == '2':
            insert_contact(contacts, file_path)
        if choice == '3':
            id = int(input("Enter the id of the contact you want to edit: "))
            update_contact(contacts, id, file_path)
        if choice == '4':
            searching_word = input("Enter searching word: ")
            search_contact(contacts, searching_word)
        if choice == '5':
            break
        else:
            print("Choose only one from the list!")


if __name__ == "__main__":
    main()
