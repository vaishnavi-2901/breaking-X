import tweepy
import ssl

# Set up your Twitter API credentials
consumer_key = "consumer key"
consumer_secret = "consumer secret"
access_token = "access token"
access_token_secret = "access token secret"
# bearer token AAAAAAAAAAAAAAAAAAAAAKkptAEAAAAAclZBKydyFUWosazXNZj4rvfmisU%3DytytFDQjDRY1gqA0PaarPzwpOr1P33D11EgqTb2Sp61OoWF17h
# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
context = ssl._create_unverified_context()
# Create an API object
api = tweepy.API(auth, wait_on_rate_limit=True)

def unfollow_non_followers():
    try:
        # Get your followers and friends (people you follow)
        followers = set(api.get_follower_ids())
        friends = set(api.get_friend_ids())

        # Find users you follow but who don't follow you back
        non_followers = friends - followers

        # Unfollow non-followers
        for user_id in non_followers:
            api.destroy_friendship(user_id)
            print(f"Unfollowed user with ID {user_id}")

        print("Unfollow process completed successfully!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import requests

    # response = requests.get("https://api.twitter.com/1.1/followers/ids.json", verify=False) to disabe the ssl

    unfollow_non_followers()
