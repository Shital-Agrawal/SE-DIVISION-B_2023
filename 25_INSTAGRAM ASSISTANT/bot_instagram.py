from instabot import Bot

my_bot = Bot()
#login
my_bot.login(username="achiever1922", password="Blast@")

#follow a user
my_bot.follow()("vin_3103")

#follow multiple users
my_bot.follow_users(["pra_nav2205","siiddhihatesyou"])

#unfollow the non followers
my_bot.unfollow_non_followers()

#upload an image
my_bot.upload("pytube.jpg", caption="pytube | create your own youtube video downloader using python")

#send message to user
my_bot.send_message("Hello sir! do you want to collabrate?","achiever1922")

#like a post
my_bot.like_user("achiever1922", amount=2)

#comment
user_id = my_bot.get_user_id_from_username("achiever1922")
media_id = my_bot.get_last_user_medias(user_id)
my_bot.comment(media_id, "This isvery nice")

#get list of followers of anyone
followers_list = my_bot.get_user_followers("achiever1922")

following_list = my_bot.get_user_following("achiever1922")

for count, each_follower in enumerate(followers_list):
    if count > 4:
        continue

    print(my_bot.get_username_from_user_id(each_follower))

for count1, each_follow in enumerate(following_list):
    if count1 > 4:
        continue

    print(my_bot.get_username_from_user_id(each_follow))
    
