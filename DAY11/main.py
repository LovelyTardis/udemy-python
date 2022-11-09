"""
    This day's project is a web scrapping program that requests data form a website.
    This data is processed to just take what it is needed. In this case it is books website,
    so scrapes the book title for books that has four or five rating stars and appends each one
    in a list. It finally prints all titles.
    Uses "requests", "lxml" and "beautifulsoup4" packages.
"""
import bs4
import requests

URL = "https://books.toscrape.com/catalogue/page-{}.html"
TOTAL_SEARCH_PAGES = 10


def main():
    titles = []
    print("Fetching data from books.toscrape.com...")
    for page in range(1, TOTAL_SEARCH_PAGES + 1):
        response = requests.get(URL.format(f"{page}"))
        soup = bs4.BeautifulSoup(response.text, "lxml")
        articles = soup.select("article")
        for article in articles:
            rating = article.select(".star-rating")[0]["class"][1]
            if rating == "Four" or rating == "Five":
                title = article.select("h3>a")[0]["title"]
                titles.append(title)
    for t in titles:
        print(t)


if __name__ == '__main__':
    main()
