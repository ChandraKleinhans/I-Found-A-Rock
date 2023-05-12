from flask import Flask
import re

app=Flask(__name__)
app.secret_key = "this_is_secret"
DATABASE = "rock_db"
