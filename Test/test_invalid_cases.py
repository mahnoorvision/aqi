import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.usefixtures("driver")
def test_empty_csv_upload(driver):
    driver.get("http://127.0.0.1:8000")  # Your app URL
    FILE_PATH = r"C:\Users\admin\Downloads\e.csv"
    time.sleep(5) 
    browse_label = driver.find_element(By.XPATH, "//label[normalize-space()='Browse']")
    browse_label.click()
    time.sleep(5)
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(FILE_PATH)
    time.sleep(3)
    name_header = driver.find_element(By.XPATH, "//div[@id='file-error']")
    assert name_header.is_displayed(), "'Name' header not found after processing."
     # Let page load
    # # Ensure file exists
    # if not os.path.exists(FILE_PATH):
    #     raise FileNotFoundError(f"CSV file not found: {FILE_PATH}")

    # # Locate the hidden file input
    # file_input = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    # )

    # # Send the file path directly
    # file_input.send_keys(FILE_PATH)

    # # Click the Process button
    # process_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Process')]"))
    # )
    # process_button.click()

    # # Wait for the empty file error message
    # error_message = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//*[contains(text(),'No data found') or contains(text(),'Ensure CSV headers')]")
    #     )
    # )

    # # Assert the error message is displayed
    # assert error_message.is_displayed(), "Empty CSV error message not shown"
