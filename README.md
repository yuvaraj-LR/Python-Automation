# Python-Automation
Built a automation tool for web scrapping using python.

Web Scrapping and Automation Using Python

Overview

This Python script is designed to perform web scraping and data extraction from an Excel file and an external API. It retrieves student details from an Excel sheet, makes API calls for each student, and extracts specific information from the API response.

Requirements

    1. Python (version 3.x recommended)
    2. Required Python packages: requests, beautifulsoup4, pandas
        2.1. Install these packages using: pip install requests beautifulsoup4 pandas

Instructions

    1. Clone the Repository
        Clone the repository to your local machine:
          git clone https://github.com/your-username/your-repository.git
          cd your-repository
          
    2. Install Dependencies
        Install the required Python packages:
          pip install requests beautifulsoup4 pandas

    3. Prepare Excel File
        Ensure you have an Excel file named demo.xlsx in the same directory as the script. The Excel file should have the following columns: name, roll no, dob.

    4. Update API URL
        Update the API URL in the script with the actual API endpoint. Modify the api_url variable in the script.

    5. Run the Script
        Execute the script:
          python3 script.py

    6.Check Output
        The script will create a new Excel file named solution.xlsx containing the final results with columns: name, roll no, dob, Credits Earned, and Grade Point Average.

