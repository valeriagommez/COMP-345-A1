def clean_a_tweet(tokenized_tweet):
    clean_tokenized_tweet = []
    singlePunctuation = ['.', '!', '?', ';', ':', '...', ',', '%']

    for token in tokenized_tweet : 
        if not (token in singlePunctuation) : # only append if it's not a punctuation character
            
            if (len(token) > 0) : 
                if (token[0] == "@") : # if the token is a username
                    token = "@USER"
            
            if "https" in token : # if the token is a URL
                token = "URL"

            else :  # for other normal tokens
                token = token.lower()

            clean_tokenized_tweet.append(token)

    # print(clean_tokenized_tweet)
    return(clean_tokenized_tweet)


def main():
    tokenizedText = ['@NBCSAthletics', 'Ya', 'just', 'knew', 'the', 'season', 'wouldn’t', 'go', 'by', 'without', 'some', 'bench', 'clearing', 'brawls', '...', 'Covid', 'or', 'not', '.', 'Behaviors', 'can’t', 'be', 'changed', 'because', 'of', 'rules', ',', 'sadly']
    clean_a_tweet(tokenizedText)

if __name__=="__main__":
    main()
