#!/usr/bin/env python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import warnings
from datetime import datetime, timedelta
import calendar

from dotenv import load_dotenv

load_dotenv()

#from crew import Ws
from src.ws.crew import Ws  

import pandas as pd

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
DEFAULT_EMAIL = os.getenv('DEFAULT_EMAIL', 'liedu03@gmail.com')
EMAIL_FILE_PATH = 'C:/Users/Lipi Inampudi/ws/src/ws/emailids.xlsx'
SHEET_NAME = 'Sheet1'
EMAIL_COLUMN = 'Email'
SPECIALTY_COLUMN = 'Specialty'

def get_specialties_and_emails():
    """Reads the Excel file and returns a dictionary {specialty: [emails]}"""
    try:
        df = pd.read_excel(EMAIL_FILE_PATH, sheet_name=SHEET_NAME)
        specialties = df[SPECIALTY_COLUMN].str.strip().str.lower().unique()
        specialty_emails = {}
        
        for specialty in specialties:
            filtered_df = df[df[SPECIALTY_COLUMN].str.strip().str.lower() == specialty]
            emails = filtered_df[EMAIL_COLUMN].dropna().tolist()
            specialty_emails[specialty] = [email.strip() for email in emails]
        
        return specialty_emails
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return {}
        
def get_next_three_months(start_month):
    try:
        start_date = datetime.strptime(start_month, "%B %Y")

        months = [start_date.strftime("%B %Y")]
        
        # Add the next two months
        for _ in range(2):
            next_month = start_date.month % 12 + 1
            next_year = start_date.year if next_month > start_date.month else start_date.year + 1
            start_date = datetime(next_year, next_month, 1)
            months.append(start_date.strftime("%B %Y"))
        
        return months
    except ValueError:
        print("Invalid month format. Please use 'Month YYYY' (e.g., 'March 2025').")
        return []

def run():
    """
    Run the crew for all specialties automatically.
    """
    print("Welcome to the Doctor Conference Web Scraper Crew!")
    
    start_month=input("Enter the starting month for conferences (e.g., 'March 2025'): ")
    months = get_next_three_months(start_month)
    if not months:
        print("Invalid month input. Exiting.")
        return
    specialty_emails = get_specialties_and_emails()
    if not specialty_emails:
        print("No specialties found in the Excel file. Exiting.")
        return
    
    for specialty, email_list in specialty_emails.items():
        print(f"Processing for specialty: {specialty.capitalize()} with {len(email_list)} recipients")
        
        inputs = {
            'months': months,
            'specialty': specialty,
            'email_list': email_list
        }
        
        try:
            Ws().crew().kickoff(inputs=inputs)
        except Exception as e:
            print(f"Error while running the crew for {specialty.capitalize()}: {e}")

if __name__ == "__main__":
    run()

    
    #specialty = input("Enter the doctor's specialty (e.g., Cardiology,Dermatology,Neurology,Rheumatology): ")
    #email_list = get_emails_from_excel(specialty_filter=specialty)
    # email_list = input("Enter recipient email addresses separated by commas: ").split(",").strip()
    # email_list = [email.strip() for email in input("Enter recipient email addresses separated by commas: ").split(",")]
    #print(f"Searching for conferences in: {', '.join(months)}")
 
