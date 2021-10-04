from sqlalchemy import create_engine, Column, Integer, VARCHAR, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///moviecollection.db')
Base = declarative_base()

# Builds the table
class MovieCollection(Base):
    __tablename__= 'movies'

    id = Column(Integer, Sequence('user_id_seq'),  primary_key=True)
    Title = Column(VARCHAR(50))
    Format = Column(VARCHAR(9))
    Length = Column(Integer)
    Release_Year = Column(Integer)
    Rating = Column(Integer)

    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s" % (
            self.id, self.Title, self.Format, self.Length, self.Release_Year, self.Rating)


# Creates a connection to the database
def db_connection():
    try:
        x = sessionmaker(bind=engine)
        session = x()
        return session
    except Exception as exc:
        print(exc)


MovieCollection.__table__
Base.metadata.create_all(engine)
