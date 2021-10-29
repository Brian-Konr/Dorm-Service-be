from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# engine = create_engine("postgresql+psycopg2://postgres:1515225Ya@localhost:5432/dorm_service", echo = True)
engine = create_engine("postgresql://postgres:adgj123456@localhost/dorm_service", echo = True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)



#done setting up database
