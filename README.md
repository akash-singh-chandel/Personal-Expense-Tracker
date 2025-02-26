# Personal Expense Tracker

## Overview
The **Personal Expense Tracker** is a Python-based application that helps users log and manage their daily expenses. It allows users to categorize expenses, set a monthly budget, and track their spending. Additionally, expenses can be saved to and loaded from a CSV file for future reference.

## Features
- Add an expense with date, category, amount, and description
- View all recorded expenses
- Set and track a monthly budget
- Save expenses to a CSV file
- Load expenses from a CSV file upon startup
- Interactive, menu-driven interface for ease of use

## Installation
To run this project, you need to have **Python 3** installed on your system.

1. Clone this repository or download the script.
2. Open a terminal or command prompt.
3. Run the script using:
   ```sh
   python expense_tracker.py
   ```

## Usage
Upon running the script, the interactive menu will be displayed with the following options:
1. Add expense
2. View expenses
3. Track budget
4. Save expenses
5. Exit

Users can select an option by entering the corresponding number.

## File Handling
- The program stores expense data in `expenses.csv`.
- When the program starts, it attempts to load previously saved expenses from the file.
- Expenses are saved automatically before exiting the application.

## Requirements
This project uses the built-in Python libraries:
- `csv` for handling file operations

## Future Improvements
- Add data visualization for expense trends
- Implement user authentication for multiple accounts
- Provide an option to edit or delete expenses

## License
This project is open-source and available for modification and distribution under the License.

