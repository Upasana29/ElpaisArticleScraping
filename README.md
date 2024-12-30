# ElpaisArticleScraping

# Selenium Web Scraper for El País Opinion Section

This project is a Python-based web scraper that uses Selenium to fetch articles, cover images, and content from the **Opinion** section of [El País](https://elpais.com/). It also translates article headlines from Spanish to English and identifies repeated words in the headlines.

## Features

- Automatically accepts cookies and navigates to the Opinion section.
- Fetches the first 5 articles, their headlines, content, and cover images.
- Saves cover images locally in the `article_images/` directory.
- Translates headlines from Spanish to English using Google Translate.
- Analyzes translated headlines to identify repeated words.

## Project Structure

```plaintext
selenium-web-scraper/
├── article_images/        # Directory for storing downloaded images
├── elpaisArticleScraping.py     # Main Python script
├── README.md              # Documentation for the project
└── requirements.txt       # Dependencies for the project
