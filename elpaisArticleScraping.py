#!/usr/bin/env python
# coding: utf-8
# import os
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googletrans import Translator  # For translation

# Setup Selenium WebDriver
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# Create translator instance
translator = Translator()

# Create a directory for saving images
os.makedirs("article_images", exist_ok=True)

# Define a function to scrape articles
def scrape_articles():
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
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

    try:
        for index in range(5):  # Limit to first 5 articles
            # Re-fetch the headlines after each navigation
            headlines = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//h2[contains(@class, 'c_t c_t-i')]"))
            )
            
            # Click on the current headline
            try:
                headline = headlines[index]
                headline_text = headline.text
                print(f"Processing Editorial {index + 1}: {headline_text}")
                
                # Scroll the element into view and click
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", headline)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"(//h2[contains(@class, 'c_t c_t-i')])[{index + 1}]"))).click()

                # Wait for the new page to load and fetch the cover image and content
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "img"))
                )
                img_element = driver.find_element(By.TAG_NAME, "img")
                img_url = img_element.get_attribute("src")

                img_path = None
                if img_url:
                    try:
                        img_response = requests.get(img_url)
                        img_response.raise_for_status()
                        img_path = os.path.join("article_images", f"cover_{index + 1}.jpg")
                        with open(img_path, "wb") as img_file:
                            img_file.write(img_response.content)
                        print(f"Saved cover image for Editorial {index + 1} at {img_path}")
                    except Exception as e:
                        print(f"Failed to save cover image for Editorial {index + 1}: {e}")

                # Fetch article content
                paragraphs = driver.find_elements(By.TAG_NAME, "p")
                content_text = " ".join([p.text for p in paragraphs])

                articles_data.append({"headline": headline_text, "content": content_text, "image": img_path})
            except Exception as e:
                print(f"Failed to process Editorial {index + 1}: {e}")
            finally:
                # Navigate back to the Opinion section
                driver.back()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//h2[contains(@class, 'c_t c_t-i')]"))
                )
    except Exception as e:
        print("Failed to fetch headlines, contents, or images:", e)

    driver.quit()
    return articles_data

# Function to translate headers and analyze them
def translate_and_analyze(articles):
    translated_headers = []
    word_count = {}

    for article in articles:
        translated_title = translator.translate(article["headline"], src="es", dest="en").text
        translated_headers.append(translated_title)
        
        # Count words in the translated title
        for word in translated_title.split():
            word = word.lower().strip(".,!?\")")
            word_count[word] = word_count.get(word, 0) + 1

    # Identify repeated words
    repeated_words = {word: count for word, count in word_count.items() if count > 2}

    return translated_headers, repeated_words

# Main execution
if __name__ == "__main__":
    # Scrape articles
    articles = scrape_articles()

    # Convert articles to DataFrame
    if articles:
        df = pd.DataFrame(articles)
        print("\nDataFrame of Editorials:")
        print(df)

        # Translate titles and analyze
        translated_headers, repeated_words = translate_and_analyze(articles)

        # Print translated headers
        print("\nTranslated Titles:")
        for header in translated_headers:
            print(header)

        # Print repeated words
        print("\nRepeated Words:")
        for word, count in repeated_words.items():
            print(f"{word}: {count}")
    else:
        print("No articles found. DataFrame is empty.")

# In[10]:


df


# In[ ]:




