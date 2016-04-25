#! /usr/bin/env python
from app import app
from app import db
from app.models import Member, Wish

db.create_all();
app.run(debug=True,host="0.0.0.0",port=8080)
