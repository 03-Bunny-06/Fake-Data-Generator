**Fake Data Generator**

Project Overview:

This script generates and displays structured fake data using the Faker library, leveraging the rich library for a visually appealing tabular output. It is ideal for developers and testers needing placeholder data for testing applications or mockups.

<hr/>

Features:

* Fake Data Generation: Uses the Faker library to generate realistic-looking fake data such as names, phone numbers, email addresses, credit card details, and more.
* Dynamic Data Output: Displays data in a styled table format with columns for various attributes.
* User Input: Prompts the user to specify the number of fake data entries to generate.
* Customizable Layout: Structured output with flexible formatting using the rich.table module.

<hr/>

Requirements:

* Python 3.x
* Installed dependencies:
  * rich for rendering styled console output
  * faker for generating fake data
* Install the required libraries using: pip install rich faker

<hr/>

How It Works:

1. Data Generation:
  * The Faker library creates fake values for fields like full name, date of birth, phone number, email, company, and more.
2. Table Creation:
  * The rich.table module is used to define a table structure, including column names and formatting.
3. User Input:
  * Prompts the user to enter the number of fake data records they want to generate.
4. Data Display:
  * Each generated data entry is added as a row in the table and printed to the console.

<hr/>

How to Use:

1. Save the script in a .py file.
2. Run the script: python script_name.py
3. Enter the number of fake data entries you need when prompted.
4. View the styled output in the console.

<hr/>

Notes:

1. Be cautious when using fake credit card data in demonstrations, as they are for mock purposes only and do not represent valid financial information.
2. This script is designed for development and testing environments and should not be used in production without proper safeguards.
