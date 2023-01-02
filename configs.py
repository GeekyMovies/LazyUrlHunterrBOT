# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
  API_ID = int(os.environ.get("API_ID", "23311160"))
    API_HASH = os.environ.get("API_HASH", "2a1366013eca4256bce853346dbcda49")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5854841142:AAFQPS3xMj8g4IMx_tLO21gcXF1jVje2gmE")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOKsBu5p6UaPbngygu0rTtFlWK6d19m234wXytjb-Dk2Czie3gF7Y_zTb9wqVczThDm2sFv7NlRFjJiGXmiroFjgYlS0lJ0do-rIEsic3iq-YywYi4kfP3UAeJxhZvnLExifGBL5wCNsrT0cTv3q9MzXOa5rlmqWqRYPQEwPIgnBlYsSuzpg_sedLShctENmBHjJs1uqhApk45cwA4WYG-hyrNXuQjEtl3enK37CBlEdsy5Hyqi_ff8Oo24chnD3pPp9ueBfRBVTdnm8U-CE4SRcjHpOhR3f9a7D9lMbsyqsMd4hJEyWqs-_Gvr3x67JpRaliyI-klJ19ncBzVo8a8GZiQSA=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME","usevrobot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER","5691018873"))
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Geekymovies:Geekymovies@cluster0.7llffit.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/LazyUrlHunterrBOT'>Lazy Url Hunterr</a> is an open source project.

    Devs: 
        <a href='https://t.me/mRiderDM'>❤️ LazyDeveloper ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Developer Channel: <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

💸<b>Donate us to Keep service Alive.💸</b>
»» A small amount of ₹5 - ₹20 - ₹50 - ₹100 will be great help !
🔺 Thank You 🔺 
"""

