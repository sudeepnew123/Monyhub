
import telebot
from telebot import types

API_TOKEN = '7342110972:AAE77URvP_IH6EPLBXmbpR040VoZVEApT2E'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to Monyhub Xtreme 5.0 Ultra Edition!\nType /commands to see all features.")

@bot.message_handler(commands=['commands'])
def commands(message):
    bot.send_message(message.chat.id, "/balance, /send, /pay, /spin, /mine, /quiz, /leaderboard, etc.")

bot.polling()
    