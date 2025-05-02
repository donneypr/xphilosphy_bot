import tweepy
import schedule
import random
import time
from datetime import datetime
import pytz
import os
import sys
from dotenv import load_dotenv

# Load in API keys from the .env file
load_dotenv()

# Twitter API credentials from .env file
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Initialize Twitter client using Tweepy
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)


philosophers_quotes = [
    "To be, or not to be, that is the question.",
    "I think, therefore I am.",
    "The only thing we have to fear is fear itself.",
    "That's one small step for man, one giant leap for mankind.",
    "In the beginning God created the heavens and the earth.",
    "All the world's a stage, and all the men and women merely players.",
    "Float like a butterfly, sting like a bee.",
    "Speak softly and carry a big stick; you will go far.",
    "The unexamined life is not worth living.",
    "To infinity and beyond!",
    "Elementary, my dear Watson.",
    "I'll be back.",
    "Frankly, my dear, I don't give a damn.",
    "May the Force be with you.",
    "I'm gonna make him an offer he can't refuse.",
    "E = mc^2.",
    "Keep your friends close, but your enemies closer.",
    "You must be the change you wish to see in the world.",
    "Not all those who wander are lost.",
    "The only way to do great work is to love what you do.",
    "Life is what happens when you're busy making other plans.",
    "The truth will set you free.",
    "That which does not kill us makes us stronger.",
    "Imagination is more important than knowledge.",
    "Genius is one percent inspiration and ninety-nine percent perspiration.",
    "Ask not what your country can do for you – ask what you can do for your country.",
    "If you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "A journey of a thousand miles begins with a single step.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "To thine own self be true.",
    "The pen is mightier than the sword.",
    "You only live once, but if you do it right, once is enough.",
    "Keep calm and carry on.",
    "Houston, we have a problem.",
    "I came, I saw, I conquered.",
    "In three words I can sum up everything I've learned about life: it goes on.",
    "If music be the food of love, play on.",
    "There is no place like home.",
    "Carpe diem. Seize the day, boys. Make your lives extraordinary.",
    "The course of true love never did run smooth.",
    "The night is darkest just before the dawn.",
    "All animals are equal, but some animals are more equal than others.",
    "Not everything that is faced can be changed, but nothing can be changed until it is faced.",
    "It matters not what someone is born, but what they grow to be.",
    "Do or do not. There is no try.",
    "All we have to decide is what to do with the time that is given us.",
    "Hope is a good thing, maybe the best of things, and no good thing ever dies.",
    "I have a dream.",
    "The only real mistake is the one from which we learn nothing.",
    "No one can make you feel inferior without your consent.",
    "A person who never made a mistake never tried anything new.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "You miss 100% of the shots you don't take.",
    "Two roads diverged in a wood, and I—I took the one less traveled by, and that has made all the difference.",
    "It is better to be feared than loved, if you cannot be both.",
    "Truth is stranger than fiction.",
    "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "Don't cry because it's over, smile because it happened.",
    "Life is either a daring adventure or nothing at all.",
    "We accept the love we think we deserve.",
    "The way to get started is to quit talking and begin doing.",
    "The best way to predict the future is to invent it.",
    "If you want to live a happy life, tie it to a goal, not to people or things.",
    "In the end, we will remember not the words of our enemies, but the silence of our friends.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "I have no special talent. I am only passionately curious.",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "Be yourself; everyone else is already taken.",
    "To live is the rarest thing in the world. Most people exist, that is all.",
    "It does not do to dwell on dreams and forget to live.",
    "We are what we repeatedly do. Excellence, then, is not an act, but a habit.",
    "Do what you can, with what you have, where you are.",
    "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away.",
    "The only thing necessary for the triumph of evil is for good men to do nothing.",
    "The greatest wealth is to live content with little.",
    "It always seems impossible until it's done.",
    "Turn your wounds into wisdom.",
    "Everything you can imagine is real.",
    "The purpose of our lives is to be happy.",
    "Life is really simple, but we insist on making it complicated.",
    "May you live all the days of your life.",
    "The best revenge is massive success.",
    "If you tell the truth, you don't have to remember anything.",
    "A friend is someone who knows all about you and still loves you.",
    "Wise men speak because they have something to say; fools because they have to say something.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Great minds discuss ideas; average minds discuss events; small minds discuss people.",
    "I would rather die on my feet than live on my knees.",
    "To err is human; to forgive, divine.",
    "Whatever you are, be a good one.",
    "You can't help everyone, but everyone can help someone.",
    "The best thing to hold onto in life is each other.",
    "Do not go where the path may lead, go instead where there is no path and leave a trail.",
    "Some are born great, some achieve greatness, and some have greatness thrust upon them.",
    "The truth is rarely pure and never simple.",
    "Love all, trust a few, do wrong to none.",
    "Action is the foundational key to all success.",
    "Education is the most powerful weapon which you can use to change the world.",
    "In the middle of difficulty lies opportunity.",
    "It is never too late to be what you might have been.",
    "Whether you think you can or you think you can't, you're right.",
    "Not how long, but how well you have lived is the main thing.",
    "Life isn't about finding yourself. Life is about creating yourself.",
    "He who has a why to live can bear almost any how.",
    "The harder I work, the luckier I get.",
    "Doubt kills more dreams than failure ever will.",
    "If opportunity doesn't knock, build a door.",
    "Live as if you were to die tomorrow. Learn as if you were to live forever.",
    "The greatest pleasure in life is doing what people say you cannot do.",
    "The secret of getting ahead is getting started.",
    "Everything has beauty, but not everyone sees it.",
    "Life is a journey, not a destination.",
    "Change your thoughts and you change your world.",
    "Don't count the days, make the days count.",
    "If you want to lift yourself up, lift up someone else.",
    "Strive not to be a success, but rather to be of value.",
    "Be kind, for everyone you meet is fighting a hard battle.",
    "Courage is grace under pressure.",
    "A mind that is stretched by new experiences can never go back to its old dimensions.",
    "Dream big and dare to fail.",
    "Don't watch the clock; do what it does. Keep going.",
    "It is during our darkest moments that we must focus to see the light.",
    "Happiness is not something ready-made. It comes from your own actions.",
    "Mistakes are proof that you are trying.",
    "Do one thing every day that scares you.",
    "The best way out is always through.",
    "Always do what you are afraid to do.",
    "A negative mind will never give you a positive life.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Don't let yesterday take up too much of today.",
    "If you can dream it, you can do it.",
    "Be the master of your fate, not the slave of your circumstances.",
    "If you want to go fast, go alone. If you want to go far, go together.",
    "No man is an island.",
    "You are never too old to set another goal or to dream a new dream.",
    "The only journey is the one within.",
    "What we think, we become.",
    "Do what you love, and the money will follow.",
    "In matters of style, swim with the current; in matters of principle, stand like a rock."
]

# Timezone setup for Toronto
toronto_timezone = pytz.timezone('America/Toronto')

def tweet_random_quote():
    """
    Selects a random quote from `philosophers_quotes` and posts it to Twitter.

    If the tweet fails, it logs an error message.
    """
    quote = random.choice(philosophers_quotes)
    try:
        response = client.create_tweet(text=quote)
        print(f"Tweet posted successfully: {response.data}")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def active_clock():
    """
    Displays the current time in Toronto timezone, the next scheduled tweet time,
    and the time remaining until the next tweet.
    """
    now = datetime.now(toronto_timezone)
    next_run = schedule.next_run()
    next_run = toronto_timezone.localize(next_run)
    time_until_next = next_run - now
    print(f"\rCurrent time: {now.strftime('%Y-%m-%d %H:%M:%S %Z')} | Next tweet: {next_run.strftime('%Y-%m-%d %H:%M:%S %Z')} | Time until next tweet: {str(time_until_next)}", end="", flush=True)


schedule.every().day.at(f"{11:02d}:00").do(tweet_random_quote)

try:
    while True:
        schedule.run_pending()
        active_clock()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nProcess interrupted. Exiting cleanly...")
    sys.exit(0)
except Exception as e:
    print(f"An unexpected error occurred in the main loop: {e}")
    sys.exit(1)










