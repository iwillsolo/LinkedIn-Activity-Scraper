# LinkedIn Activity Scraper
This is a Python script that allows you to scrape the recent activity feed of a LinkedIn profile and save it as a JSON file.

## Prerequisites
```py3
Python 3.x
Selenium package
ChromeDriver executable
LinkedIn account
Installation
```

Clone this repository to your local machine.

Install the required packages by running pip install -r requirements.txt.

Download the ChromeDriver executable from the official website (https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project directory.

## Usage
To run the script, open a terminal and navigate to the project directory. Then run the following command:

```python3
python Activity.py -U your_username -P your_password -l profile_link
```

Replace your_username and your_password with your LinkedIn credentials, and profile_link with the link to the profile whose activity you want to scrape.

The script will open LinkedIn login page, login to LinkedIn, navigate to the profile's activity page, scroll down to load all the activities, and save them as a JSON file named activities.json in the project directory.

## Disclaimer
This script is intended for educational and research purposes only. Use it at your own risk. The developer is not responsible for any legal or ethical issues that may arise from the use of this script.
