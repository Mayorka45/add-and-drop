# Add and Drop Web Scraper 📚

This Python project automates the process of checking seat availability for courses at AUI 🎓 and sends an email notification 📧 when a seat becomes available in a selected section. It uses Selenium for web scraping and smtplib for email notifications.

## #Features 🚀

- **Web Scraping**: Uses Selenium to scrape course section information and check for available seats 🔍.
- **Email Notification**: Sends an email to the user when a seat becomes available in the selected course section(s) 📩.
- **User Input**: The user selects which course sections they are interested in (from 1 to 4) 📝.
- **Continuous Monitoring**: The script continuously checks for seat availability and sends a notification when a spot is free 🔄.

## #Requirements 🛠️

- Python 3.x 🐍
- Selenium library
- smtplib for email sending
- A Chrome WebDriver for Selenium 🖥️
- Internet connection 🌐

## #Installation ⚙️

1. Install Python 3.x from the official website: [Python Downloads](https://www.python.org/downloads/).

2. Install Selenium:
    ```bash
    pip install selenium
    ```

3. Download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) for Selenium (Ensure it matches your Chrome browser version).

4. Place `chromedriver.exe` in a folder, and update the `chrome_driver_path` in the code to match your local path.

## #Usage 🏃‍♂️

1. **Start the Script**: Run the Python script after ensuring all dependencies are installed and the `chrome_driver_path` is correctly set.

2. **Select Sections**: When prompted, enter the section numbers you're interested in (from 1 to 4). For example:
    ```
    Enter the section you are interested in numbers from 1 to 4: 1 3
    ```
   The script will monitor the selected sections for seat availability 🎯.

3. **Email Notification**: If a seat becomes available in one of the selected sections, an email will be sent to the provided email address with the course and section details 📧.

## #Code Walkthrough 🔍

1. **Selenium Setup**: The script uses the Selenium WebDriver to open the AUI course schedules page and fetch data for each section 🖥️.

2. **Email Sending**: The `send_email()` function sends an email using the `smtplib` library whenever a seat becomes available 📤.

3. **Seat Availability Check**: The `check_seat_availability()` function scrapes each section (from 1 to 4) to check if there are available seats 🏫.

4. **User Input**: The script asks the user to select which sections to monitor. The script then checks availability for the selected sections ⚡.

5. **Looping & Sleeping**: The script waits 60 seconds before starting and continues to monitor the selected sections at 10-second intervals ⏳ until a seat is found.

## #Example Email ✉️

When a seat becomes available, an email with the following subject and body is sent to the specified recipient:

- **Subject**: Seat Available for [Course Code]
- **Body**: Seats available for [Course Code]: [Section Info]

## #Customization 🔧

- **Email Address**: The email sender and receiver addresses are hardcoded. Modify them to suit your needs 💌.
- **Course URL**: Modify the `url` variable if the course schedule link changes or if you're scraping a different webpage 🌐.
- **Section XPath**: If the HTML structure changes, you may need to update the XPaths for the course sections 🔄.

## #Disclaimer ⚠️

This script is meant for personal use and educational purposes 📚. Please ensure you're compliant with any applicable terms of service or rules for web scraping from AUI's website.

## #License 📜

This project is open-source. Feel free to modify and distribute it, but make sure to give appropriate credit 🙌.
