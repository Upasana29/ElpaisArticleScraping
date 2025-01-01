# ElpaisArticleScraping

# Selenium Web Scraper for El País Opinion Section

This project is a Python-based web scraper that uses Selenium to fetch articles, cover images, and content from the **Opinion** section of [El País](https://elpais.com/). It also translates article headlines from Spanish to English and identifies repeated words in the headlines.

## Features

- Automatically accepts cookies and navigates to the Opinion section.
- Fetches the first 5 articles, their headlines, content, and cover images.
- Saves cover images locally in the `article_images/` directory.
- Translates headlines from Spanish to English using Google Translate.
- Analyzes translated headlines to identify repeated words.

Prerequisites
Before running the script, ensure the following:

Python 3.8 or higher is installed on your system.
Google Chrome is installed.
ChromeDriver is downloaded and compatible with your Chrome version.
Install required Python libraries using requirements.txt.

Installation
Clone this repository:

# Web Scraping and Cross-Browser Testing with BrowserStack

This project demonstrates web scraping, API integration, text processing, and cross-browser testing using Selenium. Below is a breakdown of the tasks completed and their implementation.

## Overview
The script performs the following:

1. **Web Scraping:**
   - Scrape articles from the Opinion section of the El País website.
   - Extract the title, content, and cover image of the first five articles.

2. **API Integration:**
   - Use a translation API to translate article titles from Spanish to English.

3. **Text Analysis:**
   - Identify words that are repeated more than twice across all translated titles.

4. **Cross-Browser Testing:**
   - Validate functionality locally.
   - Run tests on BrowserStack across 5 parallel threads on a combination of desktop and mobile browsers.

---

## Setup
### Prerequisites
- Python 3.8+
- Selenium WebDriver
- BrowserStack account
- API key for the chosen translation API (e.g., Google Translate API)
- Required Python packages (install using `requirements.txt`):
  ```plaintext
  selenium
  requests
  googletrans==4.0.0-rc1  # Example for Google Translate
  ````

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Upasana29/ElpaisArticleScraping.git
   cd ElpaisArticleScraping
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables for:
   - Translation API Key
   - BrowserStack username and access key

---

## Implementation
### Web Scraping
1. **Target Website:** El País (https://elpais.com).
2. **Steps:**
   - Navigate to the Opinion section.
   - Scrape the first five articles for:
     - Titles
     - Content
     - Cover images (saved locally).

### Translation
1. **API Used:** (e.g., Google Translate API or Rapid Translate Multi Traduction API).
2. **Steps:**
   - Send titles to the API for translation.
   - Print translated titles in English.

### Text Analysis
1. Combine all translated titles.
2. Count occurrences of each word across the titles.
3. Identify and print words repeated more than twice, along with their counts.

### Cross-Browser Testing
1. Run the script locally to verify functionality.
2. Execute the solution on BrowserStack with:
   - 5 parallel threads.
   - Various combinations of desktop and mobile browsers.

---

