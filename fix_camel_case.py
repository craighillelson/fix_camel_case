"""
Import a csv of email addresses, modify addresses so that each email address is
rendered in all lower case. Export the resulting addresses to a csv.
"""

import csv
from collections import namedtuple


def open_csv_and_populate_list():

    lst = []

    with open("email_addresses.csv", "r") as csv_file:
        f_csv = csv.reader(csv_file)
        headings = next(f_csv)
        assembled_tuple = namedtuple('assembled_tuple', headings)
        for detail in f_csv:
            row = assembled_tuple(*detail)
            lst.append(row.email)

    return lst


def make_lowercase():

    lst = []

    for email in addresses:
        lst.append(email.lower())

    return lst


def write_email_addresses_to_csv(file_name):

    with open(file_name, "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["email"])
        for email in lowercase_addresses:
            out_csv.writerow([email])

        print(f'\n"{file_name}" exported successfully\n')


addresses = open_csv_and_populate_list()
lowercase_addresses = make_lowercase()
write_email_addresses_to_csv("updated_addresses.csv")
