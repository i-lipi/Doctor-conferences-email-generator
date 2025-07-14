import pandas as pd

from composio_crewai import ComposioToolSet
import os
from dotenv import load_dotenv

import composio



# Load environment variables
load_dotenv()

# Initialize Composio toolset
composio_toolset = ComposioToolSet(api_key=os.getenv('COMPOSIO_API_KEY'))
tools = composio_toolset.get_tools(actions=['GMAIL_SEND_EMAIL'])
gmail_tool = tools[0] if tools else None

# Read Excel file
file_path = r'C:\Users\Lipi Inampudi\ws\src\ws\emailids.xlsx'
df = pd.read_excel(file_path)

# Get specialty input
specialty = input("Enter the doctor's specialty (Cardiologist, Dermatology, Neurology, Rheumatology): ").strip().lower()
filtered_doctors = df[df['Specialty'].str.strip().str.lower() == specialty]
emails = filtered_doctors[['Name', 'Email']].to_dict('records')

# Check if doctors are found
if not emails:
    print(f"No doctors found with the specialty: {specialty}")
    exit()

print(f"Sending emails to {len(emails)} {specialty} doctors...")

# Send emails using Composio
for doctor in emails:
    name = doctor['Name']
    email = doctor['Email']
    subject = f"Invitation to {specialty.capitalize()} Conference"
    body = f"Dear Dr. {name},\n\nWe are pleased to invite you to an exclusive {specialty.capitalize()} conference. Looking forward to your participation.\n\nBest regards,\nYour Team"

    # Correct method to execute the Gmail tool
    response = gmail_tool.call(inputs={
        'to': email,
        'subject': subject,
        'body': body
    })

    print(f"Email sent to: {name} ({email}), Response: {response}")

print("Email sending process completed.")
