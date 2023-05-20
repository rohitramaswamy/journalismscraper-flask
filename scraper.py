import requests
from bs4 import BeautifulSoup



def FoxNews():
    #logic to parse text based on custom tags
    response = requests.get("http://www.foxnews.com")
    soup = BeautifulSoup(response.content, 'html.parser')
    str = ""
    for headline in soup.find_all(class_=  "info-header"):
        
        str = str + " " + headline.getText() +" "
    return str

def NYTimes():
    response = requests.get("http://www.nytimes.com")
    soup = BeautifulSoup(response.content, 'html.parser')
    str =""
    for headline in soup.find_all( "a"):
      str= str + " " + headline.getText() +" "
    return str



    



