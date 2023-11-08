import csv
import json

if __name__ == '__main__':
    with open("data/rosenheim_contacts.json") as f:
        contacts_raw = json.load(f)

    headlines = set()
    unique_contacts = []
    for contact in contacts_raw:
        headline = contact["headline"]
        url = contact["url"]
        if headline not in headlines and "/en/" not in url:
            unique_contacts.append(contact)
        headlines.add(headline)
    filename = 'output.csv'

    headers = contacts_raw[0].keys()

    with open(filename, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        writer.writeheader()

        for entry in unique_contacts:
            writer.writerow(entry)
