import os
import telebot
import requests
import json
import csv

# TODO: 1.1 Get your environment variables 
yourkey = os.getenv('API_KEY')
bot_id = os.getenv('BOT_ID')

bot = telebot.TeleBot(bot_id, parse_mode=None)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    MOVIE_NAME = str(message.text.replace('/movie ', ''))
    api_url = f"http://www.omdbapi.com/?apikey=3c02b14d&t={MOVIE_NAME}"
    info=requests.get(api_url)
    info=info.json()
    bot.reply_to(message, 'Title : {} \nYear of Release : {} \nIMDB Ratings : {}'.format(info['Title'], info['Year'], info['imdbRating']))
    img= open('http://img.omdbapi.com/?apikey=3c02b14d&')
    bot.send_photo(message, img)
    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    MOVIE_NAME = str(message.text.replace('/movie ', ''))
    api_url = f"http://www.omdbapi.com/?apikey=3c02b14d&t={MOVIE_NAME}"
    info=requests.get(api_url)
    info=info.json()
    fields=['Title', 'Year of Release', 'IMDB Ratings']
    data=['interstellar', '2014', '8.4']
    with open('cinecsv', 'w') as cine_csv:
        writer=csv.writer(cine_csv)
        writer.writerow(fields)
        writer.writerows(data)
        bot.send_document(message, cine_csv)
     
    
    #TODO: 2.2 Send downlodable CSV file to telegram chat

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
