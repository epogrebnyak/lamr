from pydantic.dataclasses import dataclass 
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine, Session, select


import base64
import hashlib

# from https://github.com/vancanhuit/url-shortener/blob/master/src/app/service.py
def create_short_link(original_url: str, timestamp: float):
    to_encode = f"{original_url}{timestamp}"

    b64_encoded_str = base64.urlsafe_b64encode(
        hashlib.sha256(to_encode.encode()).digest()
    ).decode()
    return b64_encoded_str[:7]

def shorten(url: str) -> str:
    return create_short_link(url, 0)

class Pair(SQLModel, table=True):
    long: str 
    short: str
    id: Optional[int] = Field(default=None, primary_key=True)

def make_pair(url: str) -> Pair:
    return Pair(long=url, short=shorten(url))

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    p1 = make_pair("https://github.com/vancanhuit/url-shortener/blob/master/src/app/service.py")
    p2 = make_pair("https://sqlmodel.tiangolo.com/tutorial/select/")
    print(p1, p2)
    session.add(p1)
    session.add(p2)
    session.commit()

def select_pairs(engine):
    with Session(engine) as session:
        statement = select(Pair)
        results = session.exec(statement)
        for p in results:
            print(p)

select_pairs(engine)      

