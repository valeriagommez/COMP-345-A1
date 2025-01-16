from collections import Counter
from q1 import tokenize
from q2 import clean_a_tweet

f = open("/content/drive/My Drive/tweets/20000_tweets.txt", "r")

def count_unigrams (cleanTweets) :
    countDict = dict()  # create a dictionary for all the tokens in the tweets

    for tweet in cleanTweets :
        for token in tweet :    # go through each token in each tweet
            if (countDict.get(token) != None) : # if the current token is already in the dictionary
                countDict[token] = countDict.get(token) + 1 # increase counter
            else : 
                countDict[token] = 1

    return countDict

def main():
    cleanTweets = []
    uncleanTweets = []

    for tweet in f :
        uncleanTweets.append(tokenize(tweet))

    for tweet in uncleanTweets : 
        cleanTweets.append(clean_a_tweet(tweet))

    unigramCounts = count_unigrams(cleanTweets)

    # Sorting the dictionary in descending form, it's now an array of tuples
    unigramSorted = sorted(unigramCounts.items(), key=lambda unigram:unigram[1], reverse=True)

    print("Top 10 Unigrams")

    for i in range(0, 10) : 
        print(unigramSorted[i][0], "    ", unigramSorted[i][1])


if __name__=="__main__":
    main()
