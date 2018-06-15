'use strict'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalogs, Base, CatalogItems, User

engine = create_engine('postgresql://catalog:password@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

session.query(Catalogs).delete()
session.query(CatalogItems).delete()
session.query(User).delete()
session.commit()

User1 = User(name="Ketan Godse", email="godse.ketan@gmail.com",
             picture='')
session.add(User1)
session.commit()



catalogs1 = Catalogs(user_id=1, name="Soccer")

session.add(catalogs1)
session.commit()

catalogItems1 = CatalogItems(user_id=1, name="Jersey",
                     description="",
                     catalog=catalogs1)

session.add(catalogItems1)
session.commit()

catalogItems2 = CatalogItems(user_id=1, name="Soccer Cleats", 
                    description="",
                     catalog=catalogs1)

session.add(catalogItems2)
session.commit()

catalogItems3 = CatalogItems(user_id=1, name="Shinguards", 
                    description="",
                     catalog=catalogs1)

session.add(catalogItems3)
session.commit()

CatalogItems4 = CatalogItems(user_id=1, name="Two Shinguards", 
                    description="",
                     catalog=catalogs1)

session.add(CatalogItems4)
session.commit()

Catalogs2 = Catalogs(user_id=1, name="Basketball")

session.add(Catalogs2)
session.commit()

CatalogItems5 = CatalogItems(user_id=1, name="Ball", 
                     description="",
                     catalog=Catalogs2)

session.add(CatalogItems5)
session.commit()

Catalogs3 = Catalogs(user_id=1, name="Baseball")

session.add(Catalogs3)
session.commit()

CatalogItems6 = CatalogItems(user_id=1, name="Bat", 
                     description="",
                     catalog=Catalogs3)

session.add(CatalogItems6)
session.commit()

Catalogs4 = Catalogs(user_id=1, name="Frisbee")

session.add(Catalogs4)
session.commit()

CatalogItems7 = CatalogItems(user_id=1, name="Bat", 
                     description="",
                     catalog=Catalogs4)

Catalogs5 = Catalogs(user_id=1, name="Snowboarding")

session.add(Catalogs5)
session.commit()

CatalogItems8 = CatalogItems(user_id=1, name="Snowboard", 
                     description="",
                     catalog=Catalogs5)

session.add(CatalogItems8)
session.commit()

CatalogItems9 = CatalogItems(user_id=1, name="Goggles", 
                     description="",
                     catalog=Catalogs5)

session.add(CatalogItems9)
session.commit()

Catalogs6 = Catalogs(user_id=1, name="Rock Climbing")

session.add(Catalogs6)
session.commit()

CatalogItems4 = CatalogItems(user_id=1, name="Bat", 
                     description="",
                     catalog=Catalogs3)


Catalogs7 = Catalogs(user_id=1, name="Foosball")

session.add(Catalogs7)
session.commit()

CatalogItems4 = CatalogItems(user_id=1, name="Bat", 
                     description="",
                     catalog=Catalogs7)

Catalogs8 = Catalogs(user_id=1, name="Skating")

session.add(Catalogs8)
session.commit()

CatalogItems4 = CatalogItems(user_id=1, name="Bat", 
                     description="",
                     catalog=Catalogs3)





Catalogs9 = Catalogs(user_id=1, name="Hockey")

session.add(Catalogs9)
session.commit()

CatalogItems4 = CatalogItems(user_id=1, name="Stick", 
                     description="",
                     catalog=Catalogs9)

session.add(CatalogItems4)
session.commit()