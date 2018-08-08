
#Import Statements#

from textblob import TextBlob  	 #ForAnalyzingGrammarInData 
import sys, tweepy            	 #ForAuthentication
import matplotlib.pyplot as plt 	 #ForPlottingPieChart



def percentage(part,whole):
    return 100*float(part)/float(whole) 

#ToShowDataInPercentage



consumerKey="Kx05pI2ZHtRkQs6LHsLYOkeRK"
consumerSecret="safrrew"
accessToken="ss-agsdga"
accessTokenSecret="slfjas;ojsjf" 
 #PasscodesForAuthentication


searchTerm=input("Enter hashtag to search:")
numberofSeachTerms=int(input("How many tweets to analyze?")) 

#FirstInput

tweets=tweepy.Cursor(api.search, q=searchTerm, lang="English").items(numberofSeachTerms)

#GetData

positive=0.00
negative=0.00
mixed=0.00
polarity=0.00

#DefineSegregation

for tweet in tweets:
    print(tweet.text) 		#PrintingRecievedData
    analysis=TextBlob(tweet.text)	#DeclareLoopConditions
    polarity+=analysis.sentiment.polarity
    if(analysis.sentiment.polarity==0.00):
        mixed+=1
    elif(analysis.sentiment.polarity<0.00):
        negative+=1
    elif(analysis.sentiment.polarity>0.00):
        positive+=1

#LoopEnds

positive=percentage(positive,numberofSeachTerms)
negative=percentage(negative,numberofSeachTerms)
mixed=percentage(mixed,numberofSeachTerms)
polarity=percentage(polarity,numberofSeachTerms)

#CallingPercentageFunction


positive=format(positive,'.2f')
negative=format(negative,'.2f')
mixed=format(mixed,'.2f')

#ConvertingToFloatVals


print('How people are reacting on'+searchTerm)

if(polarity==0):
    print("Mixed Views")
elif(polarity<0.00):
    print("Negatively")
elif(polarity>0.00):
    print("Positively")

#LoopInTextBlob


