#############################################
# Sanitize input data before rendering HTML.
import bleach

user_input = "<script>alert('hack')</script>"
safe_input = bleach.clean(user_input)
print(safe_input)  # Output: alert('hack')

#############################################
# Malware scanning service for a web server
from queue import Queue

MALWARE_PATTERNS = ["eval(", "base64_decode(", "exec(", "import os"]

def scan_file(filepath):
    with open(filepath, "r") as file:
        for line in file:
            for pattern in MALWARE_PATTERNS:
                if pattern in line:
                    return f"Malware found in {filepath}: {pattern}"
    return f"{filepath} is clean."

def worker(queue):
    while not queue.empty():
        filepath = queue.get()
        print(scan_file(filepath))

# Simulate a queue system
file_queue = Queue()
file_queue.put("test_file.py")
worker(file_queue)

#############################################
#Data Handling and Processing
import csv

def process_large_file(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

process_large_file("large_dataset.csv")

#############################################
# Automated Testing
# my_functions.py
def add(a, b):
    return a + b

# test_my_functions.py
from my_functions import add

def test_add():
    assert add(2, 3) == 5

#pytest test_my_functions.py

