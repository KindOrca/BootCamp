import tweepy

def connect_api():
    """
    connect_api 함수는 tweepy 로 API 를 연결한 'api' 객체를 리턴합니다.

    Hint: api 객체는 tweepy.API 로 만들 수 있습니다.
    """

    api_key = '8Vq20QQ0TLBR5QjtZ2PdOvAYl'
    api_key_secret = '9eGaxGXF67Z6vzoPqDG8U9DrCLvAWmfSGv4WheydpL3W4nENXr'
    access_token = '1557379749307359232-7xpTsZMzpgatEqFuZeIi5Gx64fQkj8'
    access_token_secret = 'Qz6ya2Y9TmYISvNvBYUbrDdQW4eVrxbTPKFjOS1aIMFm7'

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api


def get_tweets(api, username):
    """
    'username' 이 주어지면 해당 유저의 트윗들을 가지고 올 수 있어야 합니다.
    각 트윗은 140 자 이상이어도 모든 내용을 가지고 올 수 있어야 합니다.

    Hint: 'tweet_mode' 에 대해서 알아보세요!
    """

    tweets = api.user_timeline(username, tweet_mode='extended')

    return tweets
