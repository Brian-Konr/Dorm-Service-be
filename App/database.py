from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


<<<<<<< Updated upstream
engine = create_engine("postgresql://postgres:adgj123456@localhost/dorm_service", echo = True)
=======
engine = create_engine("postgresql+psycopg2://postgres:wujenny1218@localhost:5432/dorm_service", echo = True)

>>>>>>> Stashed changes


# 葉的
# import os
# from dotenv import load_dotenv
# load_dotenv()
# POSGRES_URI = os.getenv('POSGRES_URI')
# engine = create_engine(POSGRES_URI, echo = True)


Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)



#done setting up database
