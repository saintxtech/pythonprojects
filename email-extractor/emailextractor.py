import re

# Load the text file
with open("emails.txt", "r") as file:
    content = file.read()

# Define the regex pattern for emails
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

# Find all email matches in the content
emails = re.findall(pattern, content)

# Remove duplicates
emails = list(set(emails))

# Display extracted emails
print("Extracted Emails:")
for email in emails:
    print(f" - {email}")

# Save to a file
with open("found_emails.txt", "w") as out:
    for email in emails:
        out.write(email + "\n")

print(f"\n {len(emails)} unique email(s) saved to 'found_emails.txt'")