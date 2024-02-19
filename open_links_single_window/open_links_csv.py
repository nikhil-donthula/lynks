import csv
import webbrowser
import platform
import subprocess

def open_urls_in_chrome(csv_file):
    """
    Opens URLs from a CSV file in Chrome across Linux and Windows.

    """

    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            url = row[0]
            if url:  # Check for empty URLs
                try:
                    if platform.system() == "Windows":
                        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                        subprocess.Popen([chrome_path, "--new-tab", url])
                        #webbrowser.get('chrome').open(url)
                    else:  #Linux (e.g., Ubuntu)
                        webbrowser.get('x-www-browser').open(url)
                except webbrowser.exceptions.webbrowseropenerror as e:
                    print(f"Error opening '{url}': {e}")
                else:
                    print(f"Opened '{url}' in Chrome")

if __name__ == "__main__":
    csv_file_path = "./links.csv"
    open_urls_in_chrome(csv_file_path)