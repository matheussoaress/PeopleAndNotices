import tweepy;

class TweetFinder:
    def __init__(self):
        self.__consumerKey = "gsfsSH7JbH3PDEN29Zh7iKJYW";
        self.__consumerSecret = "kvBDQNgj43vFQ7tj6cMopXHbpXQTrbpmFqcEyA8ZyQAO0HbFS8";
        self.__owner = "matheushsoaress";
        self.__ownerID = "1537497085";
        self.__accessToken = "1537497085-rrccQS7lIkkfwQHjZEXEis2nbMyHV8pcarfu3hp";
        self.__accessTokenSecret = "o4rIZEUP9xyJ05UotT9xWCmu6Pp6zuKcbxDcjciasnPms";

    def doLoggon(self):
        auth = tweepy.OAuthHandler( self.__consumerKey, self.__consumerSecret);
        auth.set_access_token(self.__accessToken, self.__accessTokenSecret);

        self.__api = tweepy.API(auth);

    def search(self, q):
        a_s = self.__api.search(q);
        for a in a_s:
            print(a.text);