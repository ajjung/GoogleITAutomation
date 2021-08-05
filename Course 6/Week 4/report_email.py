#!/usr/bin/env python3
import reports
import emails
import os
from datetime import date

source_dir = "supplier-data/descriptions"

def get_data(file_path):
    summary = []
    for file in os.listdir(source_dir):
        if not file.startswith("."):
            with open(os.path.join(source_dir, file), "r") as f:
                fruit_name = f.readline().strip()
                fruit_weight = f.readline().strip()
            entry_name = "name: {}".format(fruit_name)
            entry_weight = "weight: {}<br/>".format(fruit_weight)
            summary.append(entry_name)
            summary.append(entry_weight)
    return summary

def get_date():
    today = date.today()
    current_date = today.strftime("%B %d, %Y")
    return current_date

if __name__ == "__main__":
    #Generate PDF report
    paragraph = "<br/>".join(get_data(source_dir))
    title = "Processed Update on {}".format(get_date())
    reports.generate_report("/tmp/processed.pdf", title, paragraph)
    #Generate email message
    sender = "automation@example.com"
    recipient = "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    attachment_path = "/tmp/processed.pdf"
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)
