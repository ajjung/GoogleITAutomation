#!/usr/bin/env python3

import sys
import csv
import re
import operator

def search_csv():
    per_user = {}
    error = {}
    with open("sys.txt", "r") as file:
        for line in file.readlines():
            search_user = re.search(r"\(([\w.]*)\)", line)
            search_error = re.search(r"ticky: ERROR ([\w ']*) ", line)
            search_info = re.search(r"ticky: INFO ([\w ]*) ", line)
            if search_user and search_user[1] not in per_user:
                per_user[search_user[1]]={"Info":0,"Error":0}
            if search_error and search_error[1] not in error:
                error[search_error[1]]=0
            if search_info:
                per_user[search_user[1]]["Info"]+=1
            if search_error:
                error[search_error[1]]+=1
                per_user[search_user[1]]["Error"]+=1
    return per_user, error

def sort_dictionary(per_user, error):
    error_sorted = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
    per_user_sorted = sorted(per_user.items())
    return per_user_sorted, error_sorted

def write_csv(per_user_sorted, error_sorted):
    keys = ["Error", "Count"]
    with open("error_message.csv", "w") as by_error:
        writer = csv.DictWriter(by_error, fieldnames=keys)
        writer.writeheader()
        writer = csv.writer(by_error)
        writer.writerows(error_sorted)

    keys = ["Username", "INFO", "ERROR"]
    with open("user_statistics.csv", "w") as by_user:
        writer = csv.DictWriter(by_user, fieldnames=keys)
        writer.writeheader()
        writer = csv.writer(by_user)
        for i in range(len(per_user_sorted)):
            writer.writerow([per_user_sorted[i][0], per_user_sorted[i][1]["Info"], per_user_sorted[i][1]["Error"]])

user, error = search_csv()
user_sorted, error_sorted = sort_dictionary(user, error)
write_csv(user_sorted, error_sorted)
