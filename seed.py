from superheroes_api import create_app, db
from superheroes_api.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():

    print("Dropping all tables ...")
    db.drop_all()
    print("Tables dropped")

    db.create_all()
    print("Tables created")

    # add some powers
    p1 = Power(name="super strength", description="gives the wielder super-human strengths")
    p2 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    p3 = Power(name="super human senses", description="allows the wielder to use her senses at a super-human level")
    p4 = Power(name="elasticity", description="can stretch the human body to extreme lengths")

    db.session.add_all([p1, p2, p3, p4])

    # add some heroes
    h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    h2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    h3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")
    h4 = Hero(name="Janet Van Dyne", super_name="The Wasp")
    h5 = Hero(name="Wanda Maximoff", super_name="Scarlet Witch")
    h6 = Hero(name="Carol Danvers", super_name="Captain Marvel")
    h7 = Hero(name="Jean Grey", super_name="Dark Phoenix")
    h8 = Hero(name="Ororo Munroe", super_name="Storm")
    h9 = Hero(name="Kitty Pryde", super_name="Shadowcat")
    h10 = Hero(name="Elektra Natchios", super_name="Elektra")

    db.session.add_all([h1, h2, h3, h4, h5, h6, h7, h8, h9, h10])

    # link powers with heroes
    hp1 = HeroPower(strength="Strong", hero=h1, power=p2)
    hp2 = HeroPower(strength="Average", hero=h3, power=p1)
    hp3 = HeroPower(strength="Weak", hero=h2, power=p4)

    db.session.add_all([hp1, hp2, hp3])

    db.session.commit()
    print("Database seeded with super people and powers")
