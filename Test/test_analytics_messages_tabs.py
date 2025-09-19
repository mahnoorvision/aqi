import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestTabsXPath:

    def test_messages_tab_xpath(self, driver):
        driver.get("http://localhost:8000")  # Make sure your Laravel server is running

        try:
            # Wait for the button to be visible by XPath
            messages_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/button[2]"))
            )
            messages_button.click()
            time.sleep(2)

            # Check content of the Messages tab
            page_text = driver.page_source
            print("Messages tab content preview:\n", page_text[:500])

            assert "Customize messages" in page_text or "Message" in page_text

        except Exception as e:
            print("❌ Error while opening Messages tab:", str(e))
            assert False, "Failed to open Messages tab with XPath"
