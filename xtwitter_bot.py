
import tweepy
import schedule
import random
import time
from datetime import datetime, timedelta
import pytz
import os
import sys
from dotenv import load_dotenv

#load in API keys
load_dotenv()

# Twitter API credentials from .env file
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

philosophers_quotes = [
    "The only true wisdom is in knowing you know nothing. – Socrates",
    "I think, therefore I am. – René Descartes",
    "Be kind, for everyone you meet is fighting a harder battle. – Plato",
    "It is the mark of an educated mind to be able to entertain a thought without accepting it. – Aristotle",
    "Happiness is not an ideal of reason but of imagination. – Immanuel Kant",
    "Man is born free, and everywhere he is in chains. – Jean-Jacques Rousseau",
    "The unexamined life is not worth living. – Socrates",
    "The mind is furnished with ideas by experience alone. – John Locke",
    "One cannot step twice in the same river. – Heraclitus",
    "Liberty consists in doing what one desires. – John Stuart Mill",
    "He who thinks great thoughts, often makes great errors. – Martin Heidegger",
    "God is dead! He remains dead! And we have killed him. – Friedrich Nietzsche",
    "The only thing I know is that I know nothing. – Socrates",
    "To be is to be perceived. – George Berkeley",
    "That which does not kill us makes us stronger. – Friedrich Nietzsche",
    "We live in the best of all possible worlds. – Gottfried Wilhelm Leibniz",
    "The life of man is solitary, poor, nasty, brutish, and short. – Thomas Hobbes",
    "An eye for an eye only ends up making the whole world blind. – Mahatma Gandhi",
    "Hell is other people. – Jean-Paul Sartre",
    "No man's knowledge here can go beyond his experience. – John Locke",
    "I can control my passions and emotions if I can understand their nature. – Baruch Spinoza",
    "The price good men pay for indifference to public affairs is to be ruled by evil men. – Plato",
    "The greatest happiness of the greatest number is the foundation of morals and legislation. – Jeremy Bentham",
    "I don’t know why we are here, but I’m pretty sure that it is not in order to enjoy ourselves. – Ludwig Wittgenstein",
    "There is but one truly serious philosophical problem, and that is suicide. – Albert Camus",
    "We are what we repeatedly do. Excellence, then, is not an act, but a habit. – Aristotle",
    "Knowledge is power. – Francis Bacon",
    "Without music, life would be a mistake. – Friedrich Nietzsche",
    "Happiness depends upon ourselves. – Aristotle",
    "If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things. – René Descartes",
    "Even while they teach, men learn. – Seneca",
    "To be is to do. – Immanuel Kant",
    "To do is to be. – Jean-Paul Sartre",
    "Do be do be do. – Frank Sinatra (often humorously included in philosophical quotes)",
    "Leisure is the mother of philosophy. – Thomas Hobbes",
    "There is nothing so absurd that some philosopher has not already said it. – Cicero",
    "Those who cannot remember the past are condemned to repeat it. – George Santayana",
    "Freedom is secured not by the fulfilling of one's desires, but by the removal of desire. – Epictetus",
    "The end justifies the means. – Niccolò Machiavelli",
    "Act only according to that maxim whereby you can at the same time will that it should become a universal law. – Immanuel Kant",
    "All is for the best, in the best of all possible worlds. – Voltaire",
    "He who has a why to live can bear almost any how. – Friedrich Nietzsche",
    "If God did not exist, it would be necessary to invent him. – Voltaire",
    "The function of prayer is not to influence God, but rather to change the nature of the one who prays. – Søren Kierkegaard",
    "Happiness is the highest good. – Aristotle",
    "Is man merely a mistake of God's? Or God merely a mistake of man's? – Friedrich Nietzsche",
    "You can discover more about a person in an hour of play than in a year of conversation. – Plato",
    "We are too weak to discover the truth by reason alone. – Saint Augustine",
    "The brave man is he who overcomes not only his enemies but his pleasures. – Democritus",
    "One is not born, but rather becomes, a woman. – Simone de Beauvoir",
    "The more I read, the more I acquire, the more certain I am that I know nothing. – Voltaire",
    "Time is the wisest of all things that are; for it brings everything to light. – Thales",
    "There is only one good, knowledge, and one evil, ignorance. – Socrates",
    "Man is the measure of all things. – Protagoras",
    "Life must be understood backward. But it must be lived forward. – Søren Kierkegaard",
    "Man is condemned to be free; because once thrown into the world, he is responsible for everything he does. – Jean-Paul Sartre",
    "It is one thing to show a man that he is in an error, and another to put him in possession of truth. – John Locke",
    "We must cultivate our garden. – Voltaire",
    "You cannot step into the same river twice. – Heraclitus",
    "To live is to suffer, to survive is to find some meaning in the suffering. – Friedrich Nietzsche",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson",
    "There is only one way to avoid criticism: do nothing, say nothing, and be nothing. – Aristotle",
    "He who opens a school door, closes a prison. – Victor Hugo",
    "All men by nature desire to know. – Aristotle",
    "You must be the change you wish to see in the world. – Mahatma Gandhi",
    "He who has a why to live can bear almost any how. – Friedrich Nietzsche",
    "I would never die for my beliefs because I might be wrong. – Bertrand Russell",
    "The state is that great fiction by which everyone tries to live at the expense of everyone else. – Frédéric Bastiat",
    "The greater the difficulty, the more glory in surmounting it. – Epicurus",
    "Do not pray for an easy life, pray for the strength to endure a difficult one. – Bruce Lee",
    "I know but one freedom, and that is the freedom of the mind. – Antoine de Saint-Exupéry",
    "The privilege of a lifetime is to become who you truly are. – Carl Jung",
    "It is not the length of life, but the depth of life. – Ralph Waldo Emerson",
    "The life of the dead is placed in the memory of the living. – Marcus Tullius Cicero",
    "The soul becomes dyed with the color of its thoughts. – Marcus Aurelius",
    "Without deviation from the norm, progress is not possible. – Frank Zappa",
    "To love is to act. – Victor Hugo",
    "The essence of the independent mind lies not in what it thinks, but in how it thinks. – Christopher Hitchens",
    "To know oneself, one should assert oneself. – Albert Camus",
    "Man is the only creature who refuses to be what he is. – Albert Camus",
    "An unexamined life is not worth living. – Socrates",
    "We are too much accustomed to attribute to a single cause that which is the product of several, and the majority of our controversies come from that. – Marcus Aurelius",
    "Waste no more time arguing about what a good man should be. Be one. – Marcus Aurelius",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "The more sand that has escaped from the hourglass of our life, the clearer we should see through it. – Jean-Paul Sartre",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. – Buddha",
    "The mind is everything. What you think you become. – Buddha",
    "Peace comes from within. Do not seek it without. – Buddha",
    "Holding on to anger is like grasping a hot coal with the intent of throwing it at someone else; you are the one who gets burned. – Buddha",
    "Three things cannot be long hidden: the sun, the moon, and the truth. – Buddha",
    "All that we are is the result of what we have thought. – Buddha",
    "Life can only be understood backwards; but it must be lived forwards. – Søren Kierkegaard",
    "He who is not a good servant will not be a good master. – Plato",
    "The worst form of inequality is to try to make unequal things equal. – Aristotle",
    "We are all born ignorant, but one must work hard to remain stupid. – Benjamin Franklin",
    "Time is a created thing. To say 'I don't have time' is to say 'I don't want to.' – Lao Tzu",
    "Do not impose on others what you yourself do not desire. – Confucius",
    "Real knowledge is to know the extent of one's ignorance. – Confucius",
    "When it is obvious that the goals cannot be reached, don't adjust the goals, adjust the action steps. – Confucius",
    "I hear and I forget. I see and I remember. I do and I understand. – Confucius",
    "Success depends upon previous preparation, and without such preparation there is sure to be failure. – Confucius",
    "Our greatest glory is not in never falling, but in rising every time we fall. – Confucius",
    "It is not what happens to you, but how you react to it that matters. – Epictetus",
    "If you want to improve, be content to be thought foolish and stupid. – Epictetus",
    "Man is disturbed not by things, but by the views he takes of them. – Epictetus",
    "Men are not worried by real problems so much as by their imagined anxieties about real problems. – Epictetus",
    "The best revenge is to be unlike him who performed the injury. – Marcus Aurelius",
    "Dwell on the beauty of life. Watch the stars, and see yourself running with them. – Marcus Aurelius",
    "It is not death that a man should fear, but he should fear never beginning to live. – Marcus Aurelius",
    "You have power over your mind - not outside events. Realize this, and you will find strength. – Marcus Aurelius",
    "Very little is needed to make a happy life; it is all within yourself, in your way of thinking. – Marcus Aurelius",
    "He who knows himself is enlightened. – Lao Tzu",
    "The greatest wealth is to live content with little. – Plato",
    "No one saves us but ourselves. No one can and no one may. We ourselves must walk the path. – Buddha",
    "You cannot teach a man anything; you can only help him find it within himself. – Galileo Galilei",
    "Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less. – Marie Curie",
    "It is the power of the mind to be unconquerable. – Seneca",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "A journey of a thousand miles begins with a single step. – Lao Tzu",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. – Martin Luther King Jr.",
    "We must not allow other people's limited perceptions to define us. – Virginia Satir",
    "The purpose of life is a life of purpose. – Robert Byrne",
    "He who fears he will suffer, already suffers because he fears. – Michel de Montaigne",
    "Those who know do not speak. Those who speak do not know. – Lao Tzu",
    "Knowing others is intelligence; knowing yourself is true wisdom. Mastering others is strength; mastering yourself is true power. – Lao Tzu",
    "People are disturbed not by things, but by the view they take of them. – Epictetus",
    "We are all in the gutter, but some of us are looking at the stars. – Oscar Wilde",
    "The man who moves a mountain begins by carrying away small stones. – Confucius",
    "The mind is not a vessel to be filled, but a fire to be kindled. – Plutarch",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
    "Out of clutter, find simplicity. From discord, find harmony. In the middle of difficulty lies opportunity. – Albert Einstein",
    "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
    "A smooth sea never made a skilled sailor. – Franklin D. Roosevelt",
    "The most difficult thing is the decision to act, the rest is merely tenacity. – Amelia Earhart",
    "The best way to predict the future is to create it. – Peter Drucker",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. – Buddha",
    "We do not see things as they are, we see them as we are. – Anaïs Nin",
    "In three words I can sum up everything I've learned about life: it goes on. – Robert Frost",
    "Believe you can and you're halfway there. – Theodore Roosevelt"
    
] 

# Timezone setup for Toronto
toronto_timezone = pytz.timezone('America/Toronto')

def tweet_random_quote():
    quote = random.choice(philosophers_quotes)
    try:
        response = client.create_tweet(text=quote + " #philosophy #quote #thinking #motivation")
        print(f"Tweet posted successfully: {response.data}")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def active_clock():
    now = datetime.now(toronto_timezone)  
    next_run = schedule.next_run()  
    next_run = toronto_timezone.localize(next_run)
    time_until_next = next_run - now
    print(f"\rCurrent time: {now.strftime('%Y-%m-%d %H:%M:%S %Z')} | Next tweet: {next_run.strftime('%Y-%m-%d %H:%M:%S %Z')} | Time until next tweet: {str(time_until_next)}", end="", flush=True)

schedule.every().day.at("00:00").do(tweet_random_quote)
schedule.every().day.at("01:00").do(tweet_random_quote)
schedule.every().day.at("02:00").do(tweet_random_quote)
schedule.every().day.at("03:00").do(tweet_random_quote)
schedule.every().day.at("04:00").do(tweet_random_quote)
schedule.every().day.at("05:00").do(tweet_random_quote)
schedule.every().day.at("06:00").do(tweet_random_quote)
schedule.every().day.at("07:00").do(tweet_random_quote)
schedule.every().day.at("08:00").do(tweet_random_quote)
schedule.every().day.at("09:00").do(tweet_random_quote)
schedule.every().day.at("10:00").do(tweet_random_quote)
schedule.every().day.at("11:00").do(tweet_random_quote)
schedule.every().day.at("12:00").do(tweet_random_quote)
schedule.every().day.at("13:00").do(tweet_random_quote)
schedule.every().day.at("14:00").do(tweet_random_quote)
schedule.every().day.at("15:00").do(tweet_random_quote)
schedule.every().day.at("16:00").do(tweet_random_quote)
schedule.every().day.at("17:00").do(tweet_random_quote)
schedule.every().day.at("18:00").do(tweet_random_quote)
schedule.every().day.at("19:00").do(tweet_random_quote)
schedule.every().day.at("20:00").do(tweet_random_quote)
schedule.every().day.at("21:00").do(tweet_random_quote)
schedule.every().day.at("22:00").do(tweet_random_quote)
schedule.every().day.at("23:00").do(tweet_random_quote)

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












