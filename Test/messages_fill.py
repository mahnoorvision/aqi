import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

@pytest.mark.usefixtures("driver")  # Assumes driver fixture is defined in conftest.py
def test_fill_custom_aqi_messages(driver):
    # 1️⃣ Open the app
    driver.get("http://127.0.0.1:8000")  # Replace with your URL

    # 2️⃣ Click the Messages tab
    messages_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Messages']"))
    )
    messages_tab.click()

    # 3️⃣ Prepare random messages for each AQI range
    def random_message(length=20):
        return ''.join(random.choices(string.ascii_letters + string.digits + " ", k=length))

    aqi_fields = {
        "//input[@placeholder='Good (0-50)']": random_message(),
        "//input[@placeholder='Moderate (51-100)']": random_message(),
        "//input[@placeholder='Unhealthy Sensitive (101-150)']": random_message(),
        "//input[@placeholder='Unhealthy (151-200)']": random_message(),
        "//input[@placeholder='Very Unhealthy (201-300)']": random_message(),
        "//input[@placeholder='Hazardous (301+)']": random_message()
    }

    # 4️⃣ Fill each input field
    for xpath, msg in aqi_fields.items():
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        input_field.clear()
        input_field.send_keys(msg)

    # 5️⃣ Click Save Messages
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save Messages']"))
    )
    save_button.click()

    # 6️⃣ Verify success message appears
    success_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'saved') or contains(text(),'success')]")
        )
    )
    assert "saved" in success_msg.text.lower() or "success" in success_msg.text.lower()
