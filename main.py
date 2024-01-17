import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

# Function to extract necessary data from API response
def extract_necessary_data(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use try-except to handle NoneType error
        try:
            # Extract Credits Earned and Grade Point Average
            credits_earned = re.search(r'Credits Earned:(\d+)', response.text).group(1).strip()
            gpa = re.search(r'Grade Point Average:([\d.]+)', response.text).group(1).strip()
        except AttributeError:
            print("Credits Earned or Grade Point Average not found in the HTML.")
            return None

        return {
            'Credits Earned': credits_earned,
            'Grade Point Average': gpa
        }
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# File path to read the data.
excel_file_path = 'demo.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Create a class to represent a student object
class Student:
    def __init__(self, name, roll_no, dob):
        self.name = name
        self.roll_no = roll_no
        self.dob = dob

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, DOB: {self.dob}"

# Create a list to store Student objects
students = []

# Iterate through each row in the DataFrame and create Student objects
for index, row in df.iterrows():
    dob_formatted = row['dob'].strftime('%d/%m/%Y')  # Format the date as DD/MM/YYYY
    student = Student(name=row['name'], roll_no=row['roll no'], dob=dob_formatted)
    students.append(student)

# Iterate through the list of students and make API calls
for index, student in enumerate(students):
    api_url = f'https://bhc.edu.in/coe_office/result_process_call.php?rollno={student.roll_no}&dob={student.dob}&exam=UG_2_3_ESE_April_2023'

    print(student.name,"'s data fetching...")

    # Extract necessary data from API response
    necessary_data = extract_necessary_data(api_url)

    if necessary_data:
        # Update the DataFrame with the necessary data
        df.at[index, 'Credits Earned'] = necessary_data['Credits Earned']
        df.at[index, 'Grade Point Average'] = necessary_data['Grade Point Average']

# Create a new DataFrame with specific columns
result_df = df[['name', 'roll no', 'dob', 'Credits Earned', 'Grade Point Average']]

# Save the DataFrame to a new Excel file
result_df.to_excel('solution.xlsx', index=False)

# Display the updated DataFrame
print(result_df)
