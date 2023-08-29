from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

pet = Pet(name="Muttley", 
          species="Mutt", 
          photo_url="https://i.etsystatic.com/20828471/r/il/916398/3418752947/il_fullxfull.3418752947_g2pm.jpg",
          notes="The dog from Wacky Races")

db.session.add(pet)
db.session.commit()