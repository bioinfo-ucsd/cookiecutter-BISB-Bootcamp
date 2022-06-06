import re
import sys
from datetime import datetime
from cookiecutter.main import cookiecutter

def check_context():

    NAMES_REGEX = r'^[a-zA-Z,\s-]+$'
    GITHUB_REGEX = r'^[a-z]+$'
    EMAIL_REGEX = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
    YEARS_REGEX = r'^[0-9][a-z][a-z]$'
    
    instructors = [{
            "name": '{{ cookiecutter.instructor1_name }}', 
            "email": '{{ cookiecutter.instructor1_email }}',
            "github": '{{ cookiecutter.instructor1_github }}',
            "year": '{{ cookiecutter.instructor1_year }}',
            "advisor": '{{ cookiecutter.instructor1_advisor }}'
        }, 
        {
            "name": '{{ cookiecutter.instructor2_name }}', 
            "email": '{{ cookiecutter.instructor2_email }}',
            "github": '{{ cookiecutter.instructor2_github }}',
            "year": '{{ cookiecutter.instructor2_year }}',
            "advisor": '{{ cookiecutter.instructor2_advisor }}'
        }, 
        {
            "name": '{{ cookiecutter.instructor3_name }}',
            "email": '{{ cookiecutter.instructor3_email }}',
            "github": '{{ cookiecutter.instructor3_github }}',
            "year": '{{ cookiecutter.instructor3_year }}',
            "advisor": '{{ cookiecutter.instructor3_advisor }}'
        }, 
        {
            "name": '{{ cookiecutter.instructor4_name }}',
            "email": '{{ cookiecutter.instructor4_email }}',
            "github": '{{ cookiecutter.instructor4_github }}',
            "year": '{{ cookiecutter.instructor4_year }}',
            "advisor": '{{ cookiecutter.instructor4_advisor }}'
        }
    ]
    
    for ins in instructors:
        
        name, email, github, year, advisor = ins['name'], ins['email'], ins['github'], ins['year'], ins['advisor']
    
        if not re.match(NAMES_REGEX, name):
            print('ERROR: %s is not a valid name!' % name)
            sys.exit(1)
    
        if not re.match(EMAIL_REGEX, email):
            print('ERROR: %s is not a valid email!' % email)
            sys.exit(1)
        
        if not re.match(GITHUB_REGEX, github):
            print('ERROR: %s is not a valid github username!' % github)
            sys.exit(1)
        
        if not re.match(YEARS_REGEX, year):
            print('ERROR: %s is not a valid year!' % year)
            sys.exit(1)
    
        if not re.match(NAMES_REGEX, advisor):
            print('ERROR: %s is not a valid name!' % advisor)
            sys.exit(1)

check_context()
