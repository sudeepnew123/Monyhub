
# Truth or Dare Command
def truth_or_dare(message):
    truths = ['What is your biggest fear?', 'What is your biggest secret?']
    dares = ['Dance for 10 seconds', 'Send a funny photo']
    choice = random.choice(['Truth', 'Dare'])
    if choice == 'Truth':
        bot.send_message(message.chat.id, random.choice(truths))
    else:
        bot.send_message(message.chat.id, random.choice(dares))
    