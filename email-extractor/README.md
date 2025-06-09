# 📬 Email Extractor - Python CLI Project

A Python script that reads a `.txt` file, extracts all valid email addresses using regular expressions, and saves them into a new file.

---

## 🎯 Features

- Reads from any plain-text file
- Extracts all email addresses using regex
- Removes duplicates automatically
- Saves results to a new file (`found_emails.txt`)
- Shows a count of total emails found

---

## 🧠 Concepts Practiced

- `re.findall()` → extract pattern-matching text (email format)
- Regex pattern for matching emails:
  ```python
  [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

File reading: with open("file.txt", "r")

File writing: with open("output.txt", "w")

Deduplication: set() to remove duplicates

Loops: for loop to process each result

How to Run:
Add text to emails.txt

Run the script:
python email_extractor.py

Check the output file:
found_emails.txt contains one email per line

