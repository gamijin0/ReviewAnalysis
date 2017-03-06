from .. import Base
from sqlalchemy import Column,Integer,String,Numeric,ForeignKey,Sequence
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = "comments"

    app_id = Column(Integer,ForeignKey("apps.id"))
    app = relationship("App",back_populates="comment")

    comment_id = Column(Integer,Sequence("comment_id_seq"),primary_key=True)
    author_name = Column(String(length=50))
    title = Column(String(length=50))
    rate_level = Column(Integer)
    content = Column(String(length=500))
