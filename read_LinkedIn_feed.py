from plugin import plugin
from LinkedIn_Feed_Bot import LinkedInBot

@plugin("read linkedin")
def read_feed(jarvis, s):
    user = 'Sir'
    jarvis.say('Yes, ' + user)

    # Currently, it is only supports Google Chrome browser.
    jarvis.say('Opening browser.')
    bot = LinkedInBot.bot(browser='chrome')

    jarvis.say('Signing in.')
    username = jarvis.input('Please insert username: ')
    password = jarvis.input('Please insert password: ')
    bot.sign_in(username, password)

    jarvis.say('Exctracting data, ' + user)
    for i in range(10):
        bot.scroll_down()
    
    df = bot.df_author_post()

    jarvis.say('Beginning your reading.')
    for index, row in df.iterrows():
        jarvis.say(row.author_name)
        jarvis.say(row.author_title)
        jarvis.say(row.post)

        jarvis.say('Next post.')
