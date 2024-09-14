from flask import Blueprint
from ..extensions import db
from ..models.user import User

#from bs4 import BeautifulSoup
#import requests
 

user = Blueprint('user', __name__)

@user.route('/user/<name>')
def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()

    #response = requests.get('https://ruz.spbstu.ru/faculty/125/groups/40439?date=2024-9-9')
    #raw_data = BeautifulSoup(response.text, 'lxml')

    #test = raw_data.find_all('div', class_='schedule__date')
    #result = ''
    #for element in test:
        #result += str(element)
    #return result

    return 'Success!'