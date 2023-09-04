import flask_testing as ft
import flask as fl

app = fl.Flask(__name__)  #creates a Flask app object
db = ""
class Person:
    pass

class TestBase(ft.TestCase): #Setup up mock app for testing

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///testdata.sqlite', #uses test db
            DEBUG=True,
            WTF_CSFR_ENABLED=False) #turns off secret key and 
        
        return app
    
    def setup(self):
        db.create_all()

        #Test data
        test_person = Person('Athena',True)
        db.session.add(test_person)
        db.session.commit()

    def teardown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self): 
        response = self.client.get(fl.url_for('index'))
        self.assertEqual(response.status_code,200) #tests get req to index route, status code = 200 if running properly
        self.assertIn('checks if this is in the page',response.data.decode()) #checks to see if the text is in the page

class TestCrud(TestBase):

    def test_person_form_post(self):
        response = self.client.post(fl.url_for('person_form_method'), data = dict(first_name='Athena',alive=True))
        
        obj1 = Person.query.filter_by(name='Athena').first()
        self.assertEqual(obj1.name, 'Athena') #see's if object has been created with the name
