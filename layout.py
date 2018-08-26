from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt


def percentage(part,whole):
    return 100*float(part)/float(whole)

consumerKey="Kx05pI2ZHtRkQs6LHsLYOkeRK"
consumerSecret="grY1yujbtYBRwfspIS8swiFoXUlTrBgr5I4IwcQhBbWmyFgYPM"
accessToken="2530152451-OO6vRCLjNXQIaHyelo1TdFhSlI8YpBzpUX91RAa"
accessTokenSecret="jscWVipPNASXspdVbwNxiRY1ZpiAw3syUi6agB4kcmr1m"


auth=tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api=tweepy.API(auth)

searchTerm=input("Enter hashtag to search:")
numberofSeachTerms=int(input("How many tweets to analyze?"))

tweets=tweepy.Cursor(api.search, q=searchTerm, lang="English").items(numberofSeachTerms)


positive=0.00
negative=0.00
mixed=0.00
polarity=0.00

for tweet in tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    polarity+=analysis.sentiment.polarity
    if(analysis.sentiment.polarity==0.00):
        mixed+=1
    elif(analysis.sentiment.polarity<0.00):
        negative+=1
    elif(analysis.sentiment.polarity>0.00):
        positive+=1

positive=percentage(positive,numberofSeachTerms)
negative=percentage(negative,numberofSeachTerms)
mixed=percentage(mixed,numberofSeachTerms)
polarity=percentage(polarity,numberofSeachTerms)

positive=format(positive,'.2f')
negative=format(negative,'.2f')
mixed=format(mixed,'.2f')

print('How people are reacting on'+searchTerm)

if(polarity==0):
    print("Mixed Views")
elif(polarity<0.00):
    print("Negatively")
elif(polarity>0.00):
    print("Positively")

labels=["Positive["+str(positive)+"%]","Mixed Views["+str(mixed)+"%]","Negative["+str(negative)+"%]"]
sizes=[positive,mixed,negative]
colors=["pink","lightgreen","lightblue"]
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title("People are reacting on"+searchTerm)
plt.axis("equal")
plt.tight_layout()
plt.show()
