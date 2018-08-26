from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 513)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(printhere)
        self.pushButton.setGeometry(QtCore.QRect(170, 180, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 85, 131, 21))
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(6, 130, 151, 31))
        self.label2.setObjectName("label_2")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 290, 271, 192))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(translate("MainWindow", "MainWindow"))
        self.pushButton.setText(translate("MainWindow", "ANALYZE"))
        self.label.setText(translate("MainWindow", "Enter Hashtag to Search : "))
        self.label2.setText(translate("MainWindow", "Number of Tweets to Analyze :"))
    def numberofSearchTerms(self):
        self.numberofSearchTerms = QtWidgets.QTextEdit(self.centralwidget)
        self.numberofSearchTerms.setGeometry(QtCore.QRect(170, 130, 104, 31))
        self.numberofSearchTerms.setObjectName("numberofSearchTerms")
    def searchTerm(self):
        self.searchTerm = QtWidgets.QTextEdit(self.centralwidget)
        self.searchTerm.setGeometry(QtCore.QRect(170, 80, 104, 31))
        self.searchTerm.setObjectName("searchTerm")
    
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

                
   
   
        consumerKey="Kx05pI2ZHtRkQs6LHsLYOkeRK"
        consumerSecret="grY1yujbtYBRwfspIS8swiFoXUlTrBgr5I4IwcQhBbWmyFgYPM"
        accessToken="2530152451-OO6vRCLjNXQIaHyelo1TdFhSlI8YpBzpUX91RAa"
        accessTokenSecret="jscWVipPNASXspdVbwNxiRY1ZpiAw3syUi6agB4kcmr1m"


        auth=tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
        auth.set_access_token(accessToken,accessTokenSecret)
        api=tweepy.API(auth)


        tweets=tweepy.Cursor(api.search, q=searchTerm, lang="English")
        tweepy.items(numberofSearchTerms)


        positive=0.00
        negative=0.00
        mixed=0.00
        polarity=0.00

        def percentage(part,whole):
            return 100*float(part)/float(whole)


        def printhere():
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

        labels=["Positive["+str(positive)+"%]","Mixed Views["+str(mixed)+"%]","Negative["+
        str(negative)+"%]"]
        sizes=[positive,mixed,negative]
        colors=["pink","lightgreen","lightblue"]
        patches,texts=plt.pie(sizes,colors=colors,startangle=90)
        plt.legend(patches,labels,loc="best")
        plt.title("People are reacting on"+searchTerm)
        plt.axis("equal")
        plt.tight_layout()
        plt.show()
