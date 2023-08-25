class PhonebookEntry:
    def __init__(self, last_name, first_name, middle_name, organization, work_phone, personal_phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone


def read_entries_from_file(file_path):
    entries = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(';')
            entry = PhonebookEntry(*data)
            entries.append(entry)
    return entries


def write_entries_to_file(entries, file_path):
    with open(file_path, 'w') as file:
        for entry in entries:
            line = ';'.join([
                entry.last_name,
                entry.first_name,
                entry.middle_name,
                entry.organization,
                entry.work_phone,
                entry.personal_phone
            ])
            file.write(line + '\n')


def display_entries(entries, page_size, page_number):
    start_idx = (page_number - 1) * page_size
    end_idx = start_idx + page_size
    for idx, entry in enumerate(entries[start_idx:end_idx], start=start_idx):
        print(f"{idx + 1}. {entry.last_name}, {entry.first_name} {entry.middle_name}")
        print(f"   Organization: {entry.organization}")
        print(f"   Work Phone: {entry.work_phone}")
        print(f"   Personal Phone: {entry.personal_phone}")
        print("-" * 30)


def add_entry(entries):
    last_name = input("Last Name: ")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    organization = input("Organization: ")
    work_phone = input("Work Phone: ")
    personal_phone = input("Personal Phone: ")
    new_entry = PhonebookEntry(last_name, first_name, middle_name, organization, work_phone, personal_phone)
    entries.append(new_entry)
    print("Entry added successfully!")


def edit_entry(entries, entry_idx):
    if entry_idx < 0 or entry_idx >= len(entries):
        print("Invalid entry index.")
        return
    entry = entries[entry_idx]
    print(f"Editing entry: {entry.last_name}, {entry.first_name} {entry.middle_name}")
    entry.last_name = input("Last Name: ")
    entry.first_name = input("First Name: ")
    entry.middle_name = input("Middle Name: ")
    entry.organization = input("Organization: ")
    entry.work_phone = input("Work Phone: ")
    entry.personal_phone = input("Personal Phone: ")
    print("Entry edited successfully!")


def search_entries(entries):
    search_term = input("Enter search term: ")
    results = []
    for entry in entries:
        if search_term.lower() in entry.last_name.lower() or \
                search_term.lower() in entry.first_name.lower() or \
                search_term.lower() in entry.middle_name.lower() or \
                search_term.lower() in entry.organization.lower() or \
                search_term in entry.work_phone or \
                search_term in entry.personal_phone:
            results.append(entry)
    return results


def main():
    file_path = 'phonebook.txt'
    entries = read_entries_from_file(file_path)
    page_size = 5
    current_page = 1

    while True:
        print("\nPhonebook Menu:")
        print("1. Display Entries")
        print("2. Add Entry")
        print("3. Edit Entry")
        print("4. Search Entries")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_entries(entries, page_size, current_page)
        elif choice == '2':
            add_entry(entries)
            write_entries_to_file(entries, file_path)
        elif choice == '3':
            entry_idx = int(input("Enter the index of the entry to edit: ")) - 1
            edit_entry(entries, entry_idx)
            write_entries_to_file(entries, file_path)
        elif choice == '4':
            search_results = search_entries(entries)
            if search_results:
                display_entries(search_results, page_size, 1)
            else:
                print("No matching entries found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
