from app import app
from app.models.product import *

def home():
    p = Product.query.all()
    return p