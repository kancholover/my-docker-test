#DB_URL에 정의한 MYSQL의 Docker 컨테이너에 접속할 세션을 생성

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

db_engine = create_engine(DB_URL, echo=True)
db_Session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

def get_db():
    with db_session() as session:
        yield session
#라우터에서는 get_db() 함수로 이 세션을 가져와 DB에 접근할 수 있도록 한다. 
