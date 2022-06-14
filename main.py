import telebot
from telebot import types
from telegram import ReplyKeyboardMarkup 
from api_bot import BOT_KEY
from pycoingecko import CoinGeckoAPI
import requests
from bs4 import BeautifulSoup 


#this is for the get API from CoinGecko 
cg = CoinGeckoAPI()

#this is for connecting to the bot
bot = telebot.TeleBot(BOT_KEY , parse_mode=None )

#when this command is sent, the bot will close kyboard buttons
@bot.message_handler(commands=["close"])
def close(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(chat_id=message.chat.id ,
     text="prese /start or /help ." ,
     reply_markup=markup)

#when this command is sent, the bot will send the user my instagram page link
@bot.message_handler(commands=["instagram"])
def send_insta(message):
    name_of_user  = message.from_user.first_name
    bot.reply_to(message , f"https://www.instagram.com/hossein__soltani_/   \
         it is my instagram page {name_of_user} .please Follow me :) thanks ")

#when this command is sent, the bot will send the user my gmail
@bot.message_handler(commands=["gmail"])
def send_gmail(message):
    name_of_user = message.from_user.first_name
    bot.reply_to(message , f"hossei.soltani8484@gmail.com   it is my gmail {name_of_user} and you cat ask me any thing " )

#when this command is sent, the bot will send the user my twitter
@bot.message_handler(commands=["twitter"])
def send_twitter(message):
    bot.reply_to(message , " https://twitter.com/hossein_soli_   its my twitter page , Follow for interesting things")

#when this command is sent, the bot will send the user my github page
@bot.message_handler(commands=["github"])
def send_github(message):
    bot.reply_to(message , " https://github.com/For00hossein00in00sol   its my github page  ")

#when this command is sent, the bot will send the user my linkedin page
@bot.message_handler(commands=["linked_in"])
def send_linked(message):
    bot.reply_to(message , " https://www.linkedin.com/in/hossein-soltani-40a554233/      its my linkedin page  ")

#when this command is sent, bot get price of bitcoin from coingecko and send it to user
@bot.message_handler(commands=["bitcoin"])
def show_btcPrice(message):
    price = cg.get_price(ids='bitcoin' , vs_currencies='usd')["bitcoin"]["usd"]
    bot.reply_to(message ,
     f" the price of bitcoin is ${price} dollars  now . ")

#when this command is sent, bot get price of ethereum from coingecko and send it to user
@bot.message_handler(commands=["ethereum"])
def show_ethereumPrice(message):
    price = cg.get_price(ids="ethereum" ,
    vs_currencies="usd")["ethereum"]["usd"]
    bot.reply_to(message ,
    f"the prince of ethereum is ${price}  dollars now")

#when this command is sent, bot get price of tether from coingecko and send it to user
@bot.message_handler(commands=["tether"])
def show_tetherPrice(message):
    price =  cg.get_price(ids="tether" , vs_currencies="usd")["tether"]["usd"]
    bot.reply_to(message , f"the price of tether is ${price} dollars now") 

#when this command is sent, bot get price of usd from 'https://mihanblockchain.com/' and send it to user vs_currencies = tomman(iran money)\
#it use BeautifulSoup to get the price of usd from 'https://mihanblockchain.com/'
@bot.message_handler(commands=["usd"])
def show_usdPrice(message):
    url = "https://mihanblockchain.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text , "html.parser")
    price = soup.select_one("#tie-block_1315 > div > div > div > div > div.col-lg-3.col-sm-12.x-box-coin.p-0 > div > div:nth-child(4) > span:nth-child(2)").text
    bot.reply_to(message , f"the price of usd  in iran is ${price} tomans now")

#this is send some helps
@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message , "this is my help page , please choose one of the following commands : \n \
    /instagram \n \
    /gmail \n \
    /twitter \n \
    /github \n \
    /linked_in \n \
    /bitcoin \n \
    /ethereum \n \
    /tether \n \
    /usd \n \
    /close \n \
    ")

# it send the user my wallet address of ethereum
@bot.message_handler(commands=["support"])
def send_support(message):
    bot.reply_to(message , 
    "this is my support page  if you want to support me , there is my wallet : \n \
    0x7052Ea82fb7908Fc1D183c0c8C88b260C2f3DF5B  <= it is my ethereume wallet address \n \
    it makes me so happy :) \n  ")

#show kyboard buttons , get username of user
@bot.message_handler(commands=["about"])
def about_me(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("/github")
    btn2 = types.KeyboardButton("/gmail")
    btn3 = types.KeyboardButton("/instagram")
    btn4 = types.KeyboardButton("/twitter")
    btn5 = types.KeyboardButton("/linked_in")
    btn6 = types.KeyboardButton("/close")
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
    name_of_user = message.from_user.first_name
    bot.send_message(chat_id= message.chat.id ,
    text=f"hy {name_of_user} , to find and connection whit me tab on any of my pages you want , it make me very happy :)" ,
    reply_markup=markup)

#when this command is sent, bot will send some kyboard buttons to choose one of the following commands
@bot.message_handler(commands=["crypto"])
def show_crypto(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 =types.KeyboardButton("/bitcoin")
    btn2 = types.KeyboardButton("/ethereum")
    btn3 =types.KeyboardButton("/tether")
    btn4 = types.KeyboardButton("/close")
    markup.add(btn1,btn2,btn3 ,btn4)
    bot.send_message(chat_id=message.chat.id ,
    text="chose whan coin you want to see . " ,
    reply_markup=markup)

#it actolly not use full:)
@bot.message_handler(commands=["fiats_inIrane"])
def show_fiats(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("/usd")
    btn2 = types.KeyboardButton("/close")
    markup.add(btn1,btn2)
    bot.send_message(chat_id=message.chat.id ,
    text="chose whan fiat you want to see . " ,
    reply_markup=markup)

@bot.message_handler(commands=["markets"])
def show_markets(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 =types.KeyboardButton("/crypto")
    btn2 = types.KeyboardButton("/fiats_inIrane")
    btn3 = types.KeyboardButton("/close") 
    markup.add(btn1,btn2,btn3)
    name_of_user = message.from_user.first_name
    bot.send_message(chat_id=message.chat.id ,
     text=f"hy {name_of_user} , Here you cat raddar all markets ." ,
    reply_markup=markup)

#it is somthing like start menu , it send kyboard buttons to choose one of the following commands
@bot.message_handler(commands=["start"])
def start(message):
    markup =types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton("/markets")
    btn2 = types.KeyboardButton("/about")
    btn4 = types.KeyboardButton("/help")
    btn3 = types.KeyboardButton("/support")
    btn5 = types.KeyboardButton("/close")
    markup.add(btn1 ,btn2 ,btn3 ,btn4 , btn5)
    name_of_user = message.from_user.first_name
    bot.send_message(chat_id=message.chat.id ,
     text=f"welecoem to my bot {name_of_user} . what do you whant to do?" ,
     reply_markup=markup)


bot.infinity_polling()