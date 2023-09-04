import flask_sqlalchemy as fl_sql
import flask as fl

app = fl.Flask(__name__)  #creates a Flask app object



db = fl_sql.SQLAlchemy(app) #creates a database object

class Family(db.Model): #functions as a table in a database
    id = db.Column(db.Integer, primary_key=True)
    fam_name = db.Column(db.String(30), nullable=False)
    people = db.relationship('Person',backref='familybr') #used to define relationships between tables
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), default="Athena")
    alive = db.Column(db.Boolean, nullable=False)
    fam_id = db.Column(db.Integer,db.ForeignKey('family.id'), nullable=False) #sets up a foreign key with the family db
    
new_fam = Family(fam_name='Martin') #create new family object 
db.session.add(new_fam) #add new record to db
db.session.commit() #commit changes

new_person = Person(first_name='Athena',alive=True, familybr=new_fam)
db.session.add(new_person)
db.session.commit()

all_people = Person.query.all() #return a list of all people as objects of type Person
first_person = Person.query.first() #return the first entry in the table
johns = Person.query.filter_by(first_name="John").all() #filters all result with first name John
person_with_id_1 = Person.query.get(1) #returns person with id 1
person_in_order = Person.query.order_by(Person.name.desc()).all() #order by Person name in descending order
first_2_people = Person.query.limit(2).all() #returns first 2 people
number_of_people = Person.query.count() #returns number of people in db

#Updating records
first_person = Person.query.first()
first_person.first_name = "New name"
db.session.commit()

#Deleting records
person_to_delete = Person.query.first()
db.session.delete(person_to_delete)
db.session.commit()
