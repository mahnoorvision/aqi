import time

def test_homepage_loads(driver):
    driver.get("http://127.0.0.1:8000")  # Replace with actual port if needed
    time.sleep(5)  # Let page load

    print("Page Source:\n", driver.page_source[:500])  # Print for debugging
    assert "Pakistan AQI Dashboard" in driver.page_source

