import csv
import re

def format_phone(phone):
    phone = re.sub(r'(\+7|8)?[\s\(\)-]*(\d{3})[\s\(\)-]*(\d{3})[\s\(\)-]*(\d{2})[\s\(\)-]*(\d{2})[\s\(\)-]*(доб\.\s*\d+)?', r'+7(\2)\3-\4-\5 \6', phone)
    return phone

def merge_duplicates(contacts_list):
    contacts_dict = {}
    
    for contact in contacts_list:
        key = (contact[0], contact[1], contact[2], format_phone(contact[5]))
        if key not in contacts_dict:
            contacts_dict[key] = contact
        else:
            existing_contact = contacts_dict[key]
            for i in range(3, 6):
                if not existing_contact[i]:
                    existing_contact[i] = contact[i]
    
    merged_contacts = list(contacts_dict.values())
    
    return merged_contacts

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for contact in contacts_list:
    contact[0] = contact[0].strip()
    contact[1] = contact[1].strip()
    contact[2] = contact[2].strip()
    contact[5] = format_phone(contact[5])

contacts_list = merge_duplicates(contacts_list)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
