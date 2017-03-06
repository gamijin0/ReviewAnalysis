import sqlalchemy as SA
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engin  = SA.create_engine("mysql+mysqlconnector://root:xlsd1996@chaos.ac.cn/iTunes",encoding='utf-8',echo=False)
Session = sessionmaker(autoflush=True)
Base = declarative_base()

Session.configure(bind=engin)

session = Session()


# comment_url = "https://itunes.apple.com/rss/customerreviews/page=1/id=1195035357/sortby=mostrecent/json?l=en&&cc=cn"
# appInfo_url = "https://itunes.apple.com/lookup?id=1195035357&&country=cn"
#
COMMENT_URL = "https://itunes.apple.com/rss/customerreviews/page=%d/id=%s/sortby=mostrecent/json?l=en&&cc=cn"
APPINFO_URL = "https://itunes.apple.com/lookup?id=%s&&country=cn"


from .modules.app import App
from .modules.comment import Comment