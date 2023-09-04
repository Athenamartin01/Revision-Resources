import flask_wtf as fwtf
import wtforms as wt
import wtforms.validators as wtv



class PersonForm(fwtf.FlaskForm): #Creates a form
    name = wt.StringField("Name: ") #creates a string input field
    age = wt.IntegerField("Age: ",validators=[wtv.DataRequired(),wtv.Length(min=2,max=10)]) #validators are used to check the field follows rules
    hair_col = wt.SelectField("Breed: ",choices=[('Brown','Brown'),('Blonde','Blonde')]) #sleectfield stores the first word chosen, and displays the second to the user as the choice
    username = wt.StringField("username")
    submit = wt.SubmitField("Submit")

#Validation Methods
    def validate_usernamer(self,username): 
        if username.data.lower() == 'admin':
            raise wtv.ValidationError("Can't use admin as username")
        
class checkAdmin:
    def __init__(self, message=None):
        if not message:
            message = 'please choose another username'
        self.message = message

    def __call__(self, form, field):
        if field.data.lower() =='admin':
            raise wtv.ValidationError(self.message)
