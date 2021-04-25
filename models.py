"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *


def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()


### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
db.define_table(
    'contact',
    Field('user_email', default=get_user_email),
    Field('first_name'),
    Field('last_name'),
)

db.define_table(
    'phone',
    Field('contact_id', 'reference contact'),
    Field('phone_number'),
    Field('phone_name'),
)

db.commit()
