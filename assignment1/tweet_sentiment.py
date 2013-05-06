import json
import sys

def hw():
    print 'Hello, world!'


def lines(fp):
    print str(len(fp.readlines()))


def main():
    """(noneTYpe) -> NoneType

    Run the program
    """

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    sentiments = process_sentiments(sent_file)

    i = 0
    for line in tweet_file:
        if i < 20:
            i += 1
        else:
            break

        score = process_tweet(line, sentiments)

        print score


def process_sentiments(scores):
    """(File) -> dict(str, float)

    Take string, score pairs from scores and return a dictionary of
    strings and floats.
    """

    dictionary = {}

    for line in scores:
        string, score = line.strip().split('\t')
        dictionary[string] = float(score)

    return dictionary


def process_tweet(tweet, scores):
    """(File, dict(str, float)) -> float

    Return the overall score of each tweet.
    """

    sentiment = 0

    tweet = json.loads(tweet)


    if "delete" in tweet:
        sentiment = 0
    else:
        tweet_text = tweet["text"]
        for word in tweet_text.split():
            if word in scores:
                sentiment += scores[word]

    return sentiment

if __name__ == '__main__':
    main()