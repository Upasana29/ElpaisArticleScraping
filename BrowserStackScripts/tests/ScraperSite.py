import os
import requests
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googletrans import Translator

# Setup Selenium WebDriver with BrowserStack capabilities
options = Options()
options.set_capability('browserstack.user', os.getenv("BROWSERSTACK_USERNAME", "<your_username>"))  # Use environment variable
options.set_capability('browserstack.key', os.getenv("BROWSERSTACK_ACCESS_KEY", "<your_access_key>"))  # Use environment variable
options.set_capability('sessionName', 'Web Scraping Test')
options.set_capability('buildName', 'Scraping Project Build')
driver = webdriver.Remote(
    command_executor="https://hub-cloud.browserstack.com/wd/hub",
    options=options
)

# Create translator instance
translator = Translator()

# Create a directory for saving images
os.makedirs("article_images", exist_ok=True)

def save_image(img_element, index):
    try:
        img_url = img_element.get_attribute("srcset")
        if img_url:
            img_url = img_url.split(",")[-1].split(" ")[0]
        else:
            img_url = img_element.get_attribute("src")

        print(f"Downloading image for Editorial {index}: {img_url}")
        img_response = requests.get(img_url)
        img_response.raise_for_status()

        img_path = os.path.join("article_images", f"cover_{index}.jpg")
        with open(img_path, "wb") as img_file:
            img_file.write(img_response.content)

        print(f"Saved image for Editorial {index} at {img_path}")
        return img_path
    except Exception as e:
        print(f"Failed to save image for Editorial {index}: {e}")
        return None

def scrape_articles():
    try:
        driver.get("https://elpais.com/")

        # Accept cookies
        try:
            accept_cookies_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "didomi-components-button.didomi-button.didomi-dismiss-button.didomi-components-button--color.didomi-button-highlight.highlight-button"))
            )
            accept_cookies_button.click()
            print("Cookies accepted successfully.")
        except Exception as e:
            print("Cookies acceptance failed:", e)

        # Navigate to the Opinion section
        try:
            opinion_section = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Opinión')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", opinion_section)
            driver.execute_script("arguments[0].click();", opinion_section)
            print("Navigated to the Opinion section.")
        except Exception as e:
            print("Failed to locate or click on the Opinion section:", e)

        articles_data = []

        for index in range(5):
            try:
                headlines = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//h2[contains(@class, 'c_t c_t-i')]"))
                )

                headline = headlines[index]
                headline_text = headline.text
                print(f"Processing Editorial {index + 1}: {headline_text}")

                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", headline)
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f"(//h2[contains(@class, 'c_t c_t-i')])[{index + 1}]"))
                ).click()

                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//img[contains(@class, 'a_m-h')]"))
                )
                img_element = driver.find_element(By.XPATH, "//img[contains(@class, 'a_m-h')]")
                img_path = save_image(img_element, index + 1)

                paragraphs = driver.find_elements(By.TAG_NAME, "p")
                content_text = " ".join([p.text for p in paragraphs])

                articles_data.append({"headline": headline_text, "content": content_text, "image": img_path})
            except Exception as e:
                print(f"Failed to process Editorial {index + 1}: {e}")
            finally:
                driver.back()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//h2[contains(@class, 'c_t c_t-i')]"))
                )

        return articles_data
    except Exception as e:
        raise e

# Main execution
try:
    # Set session name using BrowserStack Executor
    executor_object = {
        'action': 'setSessionName',
        'arguments': {
            'name': 'Web Scraping Test'
        }
    }
    driver.execute_script('browserstack_executor: {}'.format(json.dumps(executor_object)))

    # Scrape articles
    articles = scrape_articles()

    # Mark test as passed if articles are successfully scraped
    if articles:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Articles scraped successfully."}}'
        )
    else:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "No articles were scraped."}}'
        )
except Exception as e:
    # Handle exceptions and mark test as failed
    reason = json.dumps(str(e))
    driver.execute_script(
        f'browserstack_executor: {{"action": "setSessionStatus", "arguments": {{"status":"failed", "reason": {reason}}}}}'
    )
finally:
    # Quit the driver
    driver.quit()
