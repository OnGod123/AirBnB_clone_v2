#!/usr/bin/python3
"""
Module db_storage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage class"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        HBNB_ENV = os.getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            result = self.__session.query(User).all() + \
                     self.__session.query(State).all() + \
                     self.__session.query(City).all() + \
                     self.__session.query(Amenity).all() + \
                     self.__session.query(Place).all() + \
                     self.__session.query(Review).all()
        else:
            result = self.__session.query(cls).all()

        return {'{}.{}'.format(type(obj).__name__, obj.id): obj for obj in result}

    def new(self, obj):
        """Adds new object to storage database"""
        self.__session.add(obj)

    def save(self):
        """Saves storage database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from storage database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads storage database"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()

