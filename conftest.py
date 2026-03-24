import pytest
from selenium import webdriver
import allure
import os
from datetime import datetime
from config.config import HEADLESS

# =========================
# FIXTURE: browser driver
# =========================

@pytest.fixture
def driver():
    """
    Acest fixture:
    - pornește browserul
    - îl oferă testului
    - îl închide după test
    """

    # 1️⃣ Configurăm opțiunile pentru Chrome
    options = webdriver.ChromeOptions()

    # Pornim browserul maximizat
    options.add_argument("--start-maximized")

    if HEADLESS:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    # 2️⃣ Pornim browserul cu aceste opțiuni
    driver = webdriver.Chrome(options=options)

    # 3️⃣ Trimitem driverul către test
    yield driver

    # 4️⃣ După ce testul s-a terminat → închidem browserul
    driver.quit()


# =====================================
# HOOK PYTEST: screenshot automat la FAIL
# =====================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Acest hook:
    - se execută după fiecare test
    - verifică dacă testul a eșuat
    - face screenshot
    - atașează screenshot-ul în Allure
    """

    # Pytest execută testul
    outcome = yield

    # Obținem rezultatul testului
    report = outcome.get_result()

    # Ne interesează doar execuția testului (nu setup/teardown)
    if report.when == "call" and report.failed:

        # Luăm driverul folosit de test
        driver = item.funcargs.get("driver", None)

        if driver:
            # Creăm folderul screenshots dacă nu există
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Creăm un timestamp (dată + oră)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Numele fișierului
            screenshot_path = os.path.join(
                screenshots_dir,
                f"{item.name}_{timestamp}.png"
            )

            # Facem screenshot
            driver.save_screenshot(screenshot_path)

            # Atașăm screenshot-ul în raportul Allure
            allure.attach.file(
                screenshot_path,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )
