# Voter Eligibility Checker

This Python script checks voter eligibility based on country, age, and gender (where applicable), specifically for the year 2014. It covers Singapore, Nigeria, Austria, North Korea, England, and Saudi Arabia.

## Features

*   **Country Selection:** Presents a list of countries and asks the user to select one.  Handles invalid input.
*   **Input Validation:**  Uses loops to ensure the user provides valid input (Yes/No, correct country name, Male/Female).
*   **Age Check:** Prompts for age and checks if the user meets the voting age requirement for the selected country.
*   **Gender Check (Saudi Arabia):**  For Saudi Arabia, it considers gender, as women were not allowed to vote in 2014.
*   **Special Cases:** Handles England (no voting, Prime Minister appointed) and North Korea (voting occurs, but is not considered free or fair) separately.
*   **Clear Output:** Provides clear messages indicating whether the user is eligible to vote and the reason for ineligibility (age or gender).
*   **User-Friendly Prompts:** Uses descriptive prompts to guide the user through the process.

## Requirements

*   Python 3.x (should work on most versions)

## How to Use

1.  Save the Python code as a `.py` file (e.g., `voter_eligibility.py`).
2.  Open a terminal or command prompt and navigate to the directory where you saved the file.
3.  Run the script using the command: `python voter_eligibility.py`
4.  Follow the prompts to select your country, gender, enter your name and age. The script will then tell you if you are eligible to vote based on the 2014 rules.

## Example

```bash
$ python voter_eligibility.py

====To check voter's eligibility in the following countries as of 2014:====
=== SINGAPORE
=== NIGERIA
=== AUSTRIA
=== NORTH KOREA
=== ENGLAND
=== SAUDI ARABIA

Are you from any of these countries, Yes or No: yes

Which Country do you reside in? Singapore

Are you a Male(M) or Female(F): m
Please use your REAL name? John Doe
How old are you? 25

Mr John Doe is legally eligible to vote
