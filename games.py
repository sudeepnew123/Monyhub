
import random

# Spin Command (Lucky Wheel)
def spin(message):
    rewards = ['₹100', '₹50', 'Emojis', 'Nothing']
    reward = random.choice(rewards)
    bot.send_message(message.chat.id, f"You won: {reward}")

# Mine Command
def mine(message):
    outcomes = ['Diamond', 'Bomb']
    result = random.choice(outcomes)
    if result == 'Diamond':
        bot.send_message(message.chat.id, "You found a Diamond!")
    else:
        bot.send_message(message.chat.id, "You hit a bomb! Try again.")

# Quiz Command
def quiz(message):
    questions = [
        ("What is 2 + 2?", "4"),
        ("What is the capital of France?", "Paris")
    ]
    question, answer = random.choice(questions)
    bot.send_message(message.chat.id, question)
    bot.register_next_step_handler(message, check_answer, answer)

def check_answer(message, answer):
    if message.text == answer:
        bot.send_message(message.chat.id, "Correct! 🎉")
    else:
        bot.send_message(message.chat.id, "Wrong answer! Try again.")
    