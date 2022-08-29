from fastapi import APIRouter

img = APIRouter()

@img.get('/')
def home():
    return 'This route from analize the docs with IA'