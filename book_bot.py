import os
import telebot
global msg
msg = ""
global pub_year
pub_year = ""
global author
from libgen_api import LibgenSearch

API_KEY = "1925342805:AAG7j9hBzAd0olw74goOJhfH7dNlMrTm0_w"

s = LibgenSearch()


bot = telebot.TeleBot(API_KEY)

start_message = "This is a book finding bot. Simply select whether you want to find the book by the Title or by Author's name. Kindly make sure that you type correct names. We do not promote any kind of piracy and strictly recommend you to purchase books. \n \n How do you want to search book - \n 1. /title_name \n 2. /author_name"

@bot.message_handler(commands=['start'])
def greet(message):
    global msg
    msg = ""
    bot.send_message(message.chat.id,start_message)

@bot.message_handler(commands=['title_name'])
def title_name_search(message):

    bot.send_message(message.chat.id,"Enter the Correct name of book: ")
    while msg == "":
        @bot.message_handler(func=lambda message: True)
        def greet(message):
            global msg
            
            print("User typed: " + message.text)
            msg = message.text
            return msg
        if msg != "":
            break
        
    title = msg
    bot.send_message(message.chat.id,"You requested for " + "'" + msg + ". Here are some matches. Kindly match according to your author and publication year.")

    results = s.search_title(title)

    for result in results:
        msg1 = str(result)
        new_msg = " "
        symbols_remove = ["'","{","}"]
        for x in msg1:
            if x in symbols_remove:
                new_msg += ""
            elif x == ":":
                new_msg += "-"
            elif x == ",":
                new_msg += "\n"
            else:
                new_msg += x
                
        bot.send_message(message.chat.id,new_msg)
    
    bot.send_message(message.chat.id,"If you want to search for another book.\n Type /start")


@bot.message_handler(commands=['author_name'])
def title_name_search(message):

    bot.send_message(message.chat.id,"Enter the Correct name of author: ")
    while msg == "":
        @bot.message_handler(func=lambda message: True)
        def greet(message):
            global msg
            
            print("User typed: " + message.text)
            msg = message.text
            return msg
        if msg != "":
            break
        
    author = msg
    bot.send_message(message.chat.id,"You requested for " + "'" + msg + "' book. Here are some matches. Kindly match according to your book's title and publication year. This might take some time, please be patient.")

    results = s.search_author(author)

    for result in results:
        msg1 = str(result)
        new_msg = " "
        symbols_remove = ["'","{","}"]
        for x in msg1:
            if x in symbols_remove:
                new_msg += ""
            elif x == ":":
                new_msg += "-"
            elif x == ",":
                new_msg += "\n"
            else:
                new_msg += x
                
        bot.send_message(message.chat.id,new_msg)
    
    bot.send_message(message.chat.id,"In case you did not find your book, kindly check your book's name carefully, even slight change of a letter can change the result. If you want to search for another book.\n Type /start")

    
bot.polling()