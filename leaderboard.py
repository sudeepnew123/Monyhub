
# Leaderboard Command
def leaderboard(message):
    # You can get top users here based on their balance or XP
    top_players = ["User1: ₹2000", "User2: ₹1500", "User3: ₹1000"]
    bot.send_message(message.chat.id, "
".join(top_players))
    