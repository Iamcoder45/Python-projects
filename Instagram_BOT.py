from instabot import Bot

bot = Bot()

bot.login(username="samriti_903", password="Qwertyuiop@67678")

#bot.follow("ris__habh__01")

#bot.follow("ris__habh__01")



# for i in range(2,10):
#     bot.send_message("hello from this side",["ris__habh__01"])

#bot.logout()

followers=bot.get_user_followers("samriti_903")

for i in followers:
    print(bot.get_user_info(i))


#https://instagrambot.github.io/docs/en/For_developers.html                for further insta bot functions


