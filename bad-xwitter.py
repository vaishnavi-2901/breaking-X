import tweepy

# Set up your Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# these above details you will get from developer account of twitter space

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def unfollow_non_followers():
    try:
        # Get your followers and friends (people you follow)
        followers = set(api.followers_ids())
        friends = set(api.friends_ids())

        # Find users you follow but who don't follow you back
        non_followers = friends - followers

        # Unfollow non-followers
        for user_id in non_followers:
            api.destroy_friendship(user_id)
            print(f"Unfollowed user with ID {user_id}")

        print("Unfollow process completed successfully!")
    except tweepy.TweepError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    unfollow_non_followers()
