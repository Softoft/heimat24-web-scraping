import re

import nltk
from bs4 import BeautifulSoup

# Download stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords


def count_chars(text):
    return len(text)


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def process_html(file_path):
    text = read_html_file(file_path)
    soup = BeautifulSoup(text, 'html.parser')

    text = soup.get_text()
    text = text.lower()
    lines = text.split('\n')
    unique_lines = list(set(lines))

    stop_words = set(stopwords.words('english') + stopwords.words('german'))
    filtered_lines = []
    for line in unique_lines:
        words = line.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        if filtered_words:
            filtered_lines.append(' '.join(filtered_words))

    text = '\n'.join(filtered_lines)
    return text


if __name__ == '__main__':
    print("{:,.2f}".format(count_chars(read_html_file("data/website_content.html"))))
    processed_text = process_html("data/website_content.html")
    print("{:,.2f}".format(count_chars(processed_text)))

    processed_text = processed_text[:10 ** 7]
    with open("data/processed_website_content.html", 'w', encoding='utf-8') as file:
        file.write(processed_text)

