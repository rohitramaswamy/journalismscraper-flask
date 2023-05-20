from flask import Flask, request, render_template
import scraper
import sentiment
app = Flask(__name__)





@app.route("/", methods=["POST", "GET"])


def index():
    nytimes_selected = ""
    foxnews_selected = ""
    yes_checked = ""
    no_checked = ""
    
  
    if request.method == "POST":
        #if the submit button was pressed
        website_chosen = request.form["website"]
        show_scraped = request.form["scrapedata"]
        #gets the chosen website
        
        if website_chosen == "nytimes":
            website_frequency = sentiment.freqDist(scraper.NYTimes())
            website_sentiment = sentiment.sentimentAnalyzer(scraper.NYTimes())
            
            
            nytimes_selected = "selected"  
        else:
            website_sentiment =sentiment.sentimentAnalyzer(scraper.FoxNews())
            website_frequency = sentiment.freqDist(scraper.FoxNews())
            
            foxnews_selected = "selected"
        #adds a selected flag to the form 
        if show_scraped == "true":
            yes_checked = "checked"
            if website_chosen == "nytimes":
                website_scrape = sentiment.filterString(scraper.NYTimes())
            else:
                website_scrape = sentiment.filterString(scraper.FoxNews())
        else:
            no_checked = "checked"
            website_scrape = ""
        #adds a checked flag to the form 
  
        

        try:
            return render_template("gui.html", message = website_frequency,
                                           foxnews_selected = foxnews_selected,
                                           nytimes_selected = nytimes_selected, 
                                           Positive = website_sentiment['pos'] ,
                                           Negative = website_sentiment['neg'],
                                           Neutral = website_sentiment['neu'], 
                                           Compound = website_sentiment['compound'],
                                            no_checked = no_checked,
                                            yes_checked = yes_checked,
                                           Scraped = website_scrape)
        except:
            return "There was an issue adding your task"
    else:
        
            
            

        return render_template("gui.html", yes_checked = "checked" )


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")