from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

# engine = create_engine('sqlite:///chatroom.db', echo=True)
engine = create_engine('sqlite:///db/chatroom.db', echo=True)


Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False, autocommit=True)

AutoBase = automap_base()
AutoBase.prepare(engine, reflect=True)

user = AutoBase.classes.user


