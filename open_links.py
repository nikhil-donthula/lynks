import csv
import webbrowser

def open_links(csv_file):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists

        for row in reader:
            link = row[0]  # Assuming the links are in the first column
            webbrowser.open_new_tab(link)

# Example usage
csv_file_path = 'links.csv'
open_links(csv_file_path)