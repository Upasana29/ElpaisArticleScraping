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

bash
Copy code
git clone https://github.com/your-username/ElpaisArticleScraping.git
cd ElpaisArticleScraping
Install dependencies:
All dependencies are listed in requirements.txt. Install them using:
bash
Copy code
pip install -r requirements.txt
Place the chromedriver executable in your system's PATH or the project directory.



Usage
Run the script to scrape articles from El País:

bash
Copy code
python elpaisArticleScraping.py
Output
DataFrame: The script prints a DataFrame with the following columns:
headline: Article headline in Spanish.
content: Full content of the article.
image: Local path to the saved cover image.
Translated Titles: Translations of the Spanish headlines into English.
Repeated Words: Words that occur more than twice in the translated titles.

Cover Images
Cover images are saved in the article_images/ directory.

Example Output
plaintext
Copy code
DataFrame of Editorials:
headline
0  Felipe VI: la exigencia del bien común   
1                       El año de Sánchez   
2                       Siria y los peros   
3          El gobierno de los millonarios   
4                Nochevieja adelantada    

content
0  La dana ocupó un lugar de privilegio en el dis...   
1  En su ya clásica comparecencia de fin de año, ...   
2  Es sabido que todo lo que va antes de un “pero...   
3  Uno. Hace muchos años, a mediados del siglo XI...   
4  El final de año siempre ha tenido una carga si...   

image  
0  article_images/cover_1.jpg  
1  article_images/cover_2.jpg  
2  article_images/cover_3.jpg  
3  article_images/cover_4.jpg  
4  article_images/cover_5.jpg  

Translated Titles:
Felipe VI: The demand of the common good
Sánchez's year
Syria and Peros
The Government of the Millionaires
New Year's Eve advance

Repeated Words:
the: 4
of: 3

## Project Structure

```plaintext
selenium-web-scraper/
├── article_images/        # Directory for storing downloaded images
├── elpaisArticleScraping.py     # Main Python script
├── README.md              # Documentation for the project
└── requirements.txt       # Dependencies for the project
