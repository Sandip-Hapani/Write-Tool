from unicodedata import name
from pydantic import BaseModel
from typing import List, Optional

'''
This is refer as a model and each variable are in payload."
'''

class UserInput(BaseModel):
    description: str

class ProductDescription(BaseModel):
    name: str
    characteristics: str
