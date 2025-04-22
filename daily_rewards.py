
import datetime

# Daily Coins Command
def daily(message):
    # Here you can add a check if the user has claimed today's reward
    bot.send_message(message.chat.id, "You have received your daily reward: ₹50")

# Weekly Bonus Command
def weekly(message):
    # Weekly bonus logic
    bot.send_message(message.chat.id, "Congrats! You received a weekly bonus: ₹500")
    