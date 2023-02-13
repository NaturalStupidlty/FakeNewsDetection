import time
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.safari.options import Options
from django.core.validators import URLValidator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        link = request.form.get("text_input")

        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Safari(options=options, )

        val = URLValidator()
        try:
            val(f'{link}')
        except:
            driver.quit()
            return render_template("index.html", output="")

        driver.execute_script(f"window.location.href = '{link}'")

        time.sleep(7)

        page = driver.page_source
        soup = BeautifulSoup(''.join(page), 'html.parser')

        articles = soup.find_all('p')
        news_list = []

        for article in articles:
            news_list.append(article.text)

        driver.quit()

        for article in news_list:
            print(article)
    else:
        news_list = ""

    return render_template("index.html", output=news_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
