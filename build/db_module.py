from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    action = Column(String, nullable=False)
    amount = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

# Setup database connection
def db_connect():
    engine = create_engine('postgresql://{user}:{password}@{host}/{db}'.format(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        host=os.getenv('DB_HOST'),
        db=os.getenv('DB_NAME')
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
