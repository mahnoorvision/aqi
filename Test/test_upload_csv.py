import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

@pytest.mark.usefixtures("driver")
def test_file_upload_and_process(driver):
    # 1️⃣ Open the app
    driver.get("http://127.0.0.1:8000")  # Replace with your actual URL

    # 2️⃣ Set the CSV path
    csv_file_path = os.path.abspath(r"C:\Users\admin\Downloads\contacts.csv")
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found at: {csv_file_path}")

    # 3️⃣ Click the Browse label (optional, just to simulate user click)
    dropzone_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Browse']"))
    )
    dropzone_label.click()

    # 4️⃣ Send file path to hidden file input
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(csv_file_path)

    # 5️⃣ Click the Process button
    process_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Process')]"))
    )
    process_button.click()
    time.sleep(5)  # Wait for processing (adjust as needed)
    # 6️⃣ Optional: Wait for confirmation / result
    result_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'CSV processed successfully')]"))
    )
    assert "CSV processed successfully" in result_msg.text
