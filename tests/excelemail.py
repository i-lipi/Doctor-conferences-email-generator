import pandas as pd

def get_emails_from_excel(file_path='C:/Users/Lipi Inampudi/ws/src/ws/emailids.xlsx', sheet_name='Sheet1', email_column='Email',name_column='Name'):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        #email_list = df[email_column].dropna().tolist()
        email_list = df[[email_column, name_column]].dropna().to_dict('records')
        #return [email.strip() for email in email_list]
        return(email_list)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []
    
email_list = get_emails_from_excel()

print(email_list)