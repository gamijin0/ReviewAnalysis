from .. import Base
from sqlalchemy import Column,Integer,String,Numeric
from sqlalchemy.orm import relationship
from .comment import Comment

class App(Base):
    __tablename__ = "apps"

    id = Column(Integer,primary_key=True)
    name = Column(String(length=30))
    fileSizeBytes = Column(Integer)
    version = Column(String(length=10))
    description = Column(String(length=1000))
    releaseDate = Column(String(length=30))
    formattedPrice = Column(String(length=20))
    minimumOsVersion = Column(String(length=10))
    averageUserRating = Column(Numeric)
    userRatingCount = Column(Integer)

    comment = relationship(Comment)

