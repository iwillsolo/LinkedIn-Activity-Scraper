import argparse
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

Usage='''

'''

# Define and parse the command line arguments
parser = argparse.ArgumentParser(description='Scrape recent activity from a LinkedIn profile.')
parser.add_argument('-U', '--username', type=str, required=True, help='LinkedIn username')
parser.add_argument('-P', '--password', type=str, required=True, help='LinkedIn password')
parser.add_argument('-l', '--profile-link', type=str, required=True, help='LinkedIn profile link')
args = parser.parse_args()

# Configure the webdriver
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# Login to LinkedIn
driver.get('https://www.linkedin.com/login')
username = driver.find_element(By.NAME,'session_key')
username.send_keys(args.username)
password = driver.find_element(By.NAME,'session_password')
password.send_keys(args.password)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

# Navigate to the activities page
url = args.profile_link
if not url.endswith('/recent-activity/'):
    url += '/recent-activity/'
driver.get(url)

# Load more activities
# Click on a "Load more" button or link if it exists
time.sleep(2)
# Scroll down to load more activities
prev_num_activities = 0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    curr_num_activities = len(driver.find_elements(By.CSS_SELECTOR, '.occludable-update'))
    if curr_num_activities == prev_num_activities:
        break
    prev_num_activities = curr_num_activities

# Extract the activities
activities = driver.find_elements(By.CSS_SELECTOR, '.occludable-update')
activity_list = []
for activity in activities:
    activity_text = activity.text
    activity_dict = {'text': activity_text}
    activity_list.append(activity_dict)

# Save as JSON file
with open('activities.json', 'w') as f:
    json.dump(activity_list, f)

# Close the webdriver
driver.quit()
