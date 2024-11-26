import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_create():
    default_url = "http://localhost:5000"
    url = os.getenv("EMPLOYEES_URL", default_url)

    driver_type = os.getenv("SELENIUM_DRIVER", "ChromeDriver")
    if driver_type == "ChromeDriver":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if driver_type == "EdgeDriver":
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
        )
    elif driver_type == "RemoteWebDriver":
        command_executor = os.getenv("SELENIUM_HUB_URL", "http://localhost:4444/wd/hub")
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote(command_executor=command_executor, options=options)
    else:
        raise ValueError(f"Invalid driver: {driver_type}")
    driver.get(url)
    sleep(3)
    driver.find_element(By.ID, "name").send_keys("John Doe")
    sleep(3)
    driver.find_element(By.ID, "submit-input").click()
    sleep(3)

    message = driver.find_element(By.ID, "message-paragraph").text
    assert message == "Employee has been created"

    driver.quit()
