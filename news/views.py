from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
# Create your views here.

def scrape(request):
    session = requests.Session()
   
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}


    url = "https://www.bbc.com/news"
    content = session.get(url).content
    #beautiful soup is a library that can extract data from HTML web pages.
    soup = BSoup(content, "html.parser")

    news = soup.find_all('div', {"class":"gs-c-promo-body gel-1/2@xs gel-1/1@m"})
    #for loop iterate over soup objects which are the html elements and texts.

    for article in news:
        link = article.find_all('a')[0]['href']
        title = article.find_all('a')[0].text.strip()
        image_src = article.find_all('img')[0]['src']
        
        # additional fields
        category = article.find('span', class_='gs-c-section-name').text.strip()
        author = article.find('span', class_='qa-contributor-name').text.strip()
        date_published = article.find('time')['datetime']
        content = session.get(link).content
        article_soup = BSoup(content, "html.parser")
        article_text = article_soup.find('div', class_='ssrcss-1vvhd4r-StyledParagraph').text.strip()
        source = 'BBC News'
        
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.source = source
        new_headline.category = category
        new_headline.author = author
        new_headline.date_published = date_published
        new_headline.content = article_text
        new_headline.save()
    
    return redirect("../")


def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "index.html", context)

