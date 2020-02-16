import csv

from tabulate import tabulate


def convert(file_obj, tablefmt):
    reader = csv.DictReader(file_obj)
    table = (row.values() for row in reader)
    return tabulate(table, reader.fieldnames, tablefmt=tablefmt)
