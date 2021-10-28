from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    on_offer = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Item name = {self.name}, price = {self.price}>"

class Item2(Base):
    __tablename__ = 'items2'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    on_offer = Column(Boolean, default=False) #nullable = False means NOT NULL

    def __repr__(self):
        return f"<Item name = {self.name}, price = {self.price}>"

class Test(Base):
    __tablename__ = "test"
    applier_id = Column(Integer, primary_key=True)
    accepter_id = Column(Integer)


