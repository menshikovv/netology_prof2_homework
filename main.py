import re
import csv

def format_phone(phone):
    phone = re.sub(r'\D', '', phone)
    if len(phone) == 11:
        return f'+7({phone[1:4]}){phone[4:7]}-{phone[7:9]}-{phone[9:11]}'
    else:
        return ''

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

unique_contacts_dict = {}

for contact in contacts_list:
    if len(contact) >= 6:
        if len(contact[0].split()) == 1:
            lastname, firstname, surname = contact[0], '', ''
        else:
            parts = contact[0].split()
            lastname = parts[0]
            firstname = parts[1]
            surname = parts[2] if len(parts) > 2 else ''

        contact[5] = format_phone(contact[5])

        key = (lastname, firstname, surname)

        if key in unique_contacts_dict:
            for i in range(len(contact)):
                if not unique_contacts_dict[key][i]:
                    unique_contacts_dict[key][i] = contact[i]
        else:
            unique_contacts_dict[key] = contact

unique_contacts = list(unique_contacts_dict.values())

with open("phonebook.csv", "w", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(unique_contacts)
