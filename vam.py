from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import sys

WEBPAGE = "https://nswhvam.health.nsw.gov.au/vam"

driver = webdriver.Chrome()

driver.get(WEBPAGE)
# manual login then go to reschedule page
days = [
    "day_1",
    "day_2",
    "day_3",
    "day_4",
    "day_5",
    "day_6",
    "day_7",
    "day_8",
]
days_vera = ["day_30", "day_31"]
print("LOGIN")
time.sleep(200)
print("STARTING")
while True:
    for day in days:
        driver.find_element_by_id(day).click()
        try:
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.ID, "appointmentInfoEmpty"))
            )
        except TimeoutException:
            driver.find_element_by_xpath("//*[@class='btn appointmentSlot']").click()
            driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
            driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            driver.find_element_by_xpath(
                "(//div[@id='appointmentInfo'])[2]//*[@class='btn appointmentSlot']"
            ).click()
            driver.find_element_by_tag_name("body").send_keys(Keys.END)
            time.sleep(0.5)
            driver.find_element_by_id("submitBtn").click()
            print("SUCCEED")
            time.sleep(240)
            driver.close()
            sys.exit(0)
        # sanity wait
        time.sleep(1)
