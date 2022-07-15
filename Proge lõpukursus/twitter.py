"""Twitter."""


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    biggest = Tweet(0,0,1,0)
    for i in tweets:
        if (i.retweets/i.time) > (biggest.retweets/biggest.time):
            biggest = i
    return biggest
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old or broken and has 64 retweets.
    >Tweet2 is 3.12 hours old or broken and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    pass


def sort_by_popularity(tweets: list) -> list:
    return sorted(tweets, key = lambda tweets: tweets.retweets, reverse = True)
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    pass


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    filtered_list = []
    for i in tweets:
        if hashtag in i.content:
            filtered_list += [i]
    return filtered_list
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    pass


def sort_hashtags_by_popularity(tweets: list) -> list:
    filters = []
    list_of_filters_sum = []
    the_bug = []
    for i in tweets:
        if '#' in i.content:
            for x in range(1,len(i.content.split("#"))):
                if f'#{i.content.split("#")[x].strip()}' not in filters:
                     filters += [f'#{i.content.split("#")[x].strip()}']
    for i in filters:
        list_of_filters_sum += [[sum(x.retweets for x in filter_by_hashtag(tweets,i)), i]]
        print(list_of_filters_sum)
    ooga_booga = sorted(sorted(list_of_filters_sum, key = lambda i:i[1]), key = lambda i:i[0], reverse = True)
    for i in ooga_booga:
        the_bug += [i[1]]
    return the_bug
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    pass

tweet2 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart #heart", 1249, 1)
tweet1 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 284199)
tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
tweets = [tweet1, tweet2, tweet3]
'''
print(find_fastest_growing(tweets))  # -> "@elonmusk"
print(sort_by_popularity(tweets))
'''
#print(filter_by_hashtag(tweets, "#bigsmart")[1].user)
print(sort_hashtags_by_popularity(tweets))
