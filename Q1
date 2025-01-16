# a function to tokenize text into words
def tokenize(text):
    words = []
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # 1. separating the tokens using the SPACE character

    wordsNoSpace = text.split(" ") # splitting the tokens using SPACE characters

    # 2. separate the punctuation marks into different tokens
    singlePunctuation = ['.', '!', '?', ';', ':', '...', ',', '%']
    wordsSeparatePunct = []

    for token in wordsNoSpace :    # at this point, all tokens are separated by SPACES

        punctuationFound = False
        charToRemove = ""
        isLink = "https" in token
        isNumber = False

        if "\n" in token : 
            token = token.replace("\n","")

        for punctChar in singlePunctuation : 

            if (punctChar in token) and not (isLink): # if there's a punctuation mark and it's not a link
                punctuationFound = True
                charToRemove = punctChar
                
        if punctuationFound : 

            # Check if the current token is a number
            if token.find(charToRemove) > 0 : 
                charBefore = token[token.find(charToRemove) - 2]

            else : charBefore = ""

            charAfter = token[token.find(charToRemove) - 1]

            if (charBefore in numbers) or (charAfter in numbers): 
                isNumber = True

            if not (isNumber) or (charToRemove == '%') : # if it's not a number, then separate them
                token = token.replace(charToRemove, "")
                wordsSeparatePunct.append(token)
                wordsSeparatePunct.append(charToRemove)

            else : # do not separate numbers with decimal points
                wordsSeparatePunct.append(token)

        else : # do not separate if there are no punctuations
            wordsSeparatePunct.append(token)

    # 3. find contractions and count them as two

    contractions = ["'m", "'re", "n't", "'s", "'ll", "'ve"] # continue this

    for token in wordsSeparatePunct : 
        contractionFound = False

        for cur in contractions : 
            if cur in token :   # if the word contains a contraction 
                contractionFound = True
                contraction = cur
        
        if contractionFound : 
            token = token.replace(contraction, "")
            words.append(token)
            words.append(contraction)

        else : 
            words.append(token)

    return words

def main():
    text = "#Texas #USA #NorthAmerica Cases: 509,539 (+21) Death: 8,583 Recovered: 344,845 Critical: 1,754 New %: 0.3% Death %: 1.7% Population %: 1.8% #CoronaVirus #Covid19 #SarsCov2 #Forecast https://t.co/yHbd9gl1uz https://t.co/sRulRFOeUx"
    tokenizedText = tokenize(text)
    print(tokenizedText)

if __name__=="__main__":
    main()




