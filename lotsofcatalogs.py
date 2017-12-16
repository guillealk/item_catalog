from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Catalog, Base, CatalogItem, User
 
engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()


catalog1 = Catalog(user_id=1,
                   name="Soccer") 
session.add(catalog1)
session.commit()

catalogItem1 = CatalogItem(user_id=1,
                           tittle="Soccer Cleats",
                           description="The shoes",
                           catalog=catalog1)

catalogItem2 = CatalogItem(user_id=1,
                           tittle="Jersey",
                           description="The shirt",
                           catalog=catalog1)

session.add(catalogItem1)
session.add(catalogItem2)
session.commit()

catalog2 = Catalog(user_id=1,
                   name="Basketball") 
session.add(catalog2)
session.commit()


catalog3 = Catalog(user_id=1,
                   name="Baseball") 
session.add(catalog3)
session.commit()

catalogItem3 = CatalogItem(user_id=1,
                           tittle="Bat",
                           description="The bat",
                           catalog=catalog3)

session.add(catalogItem3)
session.commit()

catalog4 = Catalog(user_id=1,
                   name="Frisbee") 
session.add(catalog4)
session.commit()


catalog5 = Catalog(user_id=1,
                   name="Snowboarding") 
session.add(catalog5)
session.commit()

catalogItem4 = CatalogItem(user_id=1,
                           tittle="Snowboard",
                           description="Best for any terrain and conditions.",
                           catalog=catalog5)

session.add(catalogItem4)
session.commit()

print "added menu items!"