from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from server.models.users import UserInput, ProductDescription
from server.utils.GPT3 import GPT3
from server.utils import http_status
from server.utils.article import *


app = FastAPI()

@app.get("/")
def writer_tools_home():
    return {"Welcome to": "Rejoice Writer Tool"} 

@app.post("/v1/blog-gen")
def get_article(user_input: UserInput):

    total_keywords = []
    payload = jsonable_encoder(user_input)
    user_para = payload.get('description')
    paragraphs = gen_article(user_para)

    response = {
            "success": True,
            "status_code": http_status.OK,
            "message": "Keywords generated successfully",
            "data": paragraphs
    }

    return response

@app.post("/v1/rephraser")
def paraphraser(user_input: UserInput):

    total_keywords = []
    payload = jsonable_encoder(user_input)
    user_content = payload.get('description')
    paragraphs = rephraser(user_content)

    response = {
            "success": True,
            "status_code": http_status.OK,
            "message": "Content Rephrased Successfully",
            "data": paragraphs
    }

    return response

@app.post("/v1/summerizer")
def summarise(user_input: UserInput):

    total_keywords = []
    payload = jsonable_encoder(user_input)
    user_content = payload.get('description')
    paragraphs = summary_gen(user_content)

    response = {
            "success": True,
            "status_code": http_status.OK,
            "message": "Content Summary Generated Successfully",
            "data": paragraphs
    }

    return response

@app.post("/v1/email")
def email_writer(user_input: UserInput):

    total_keywords = []
    payload = jsonable_encoder(user_input)
    user_content = payload.get('description')
    email = write_email(user_content)

    response = {
            "success": True,
            "status_code": http_status.OK,
            "message": "Email Generated Successfully",
            "data": email
    }

    return response

@app.post("/v1/tagline")
def gen_tagline(user_input: UserInput):

    total_keywords = []
    payload = jsonable_encoder(user_input)
    user_content = payload.get('description')
    email = tagline_generator(user_content)

    response = {
            "success": True,
            "status_code": http_status.OK,
            "message": "Tagline Generated Successfully",
            "data": email
    }

    return response

@app.post("/v1/blog_outline")
def gen_blog_outline(user_input: UserInput):

    total_keywords = []
    payload = jsonable_encoder(user_input)
    user_content = payload.get('description')
    outline = blog_post_outline(user_content)

    response = {
            "success": True,
            "status_code": http_status.OK,
            "message": "Outlines Generated Successfully",
            "data": outline
    }

    return response

@app.post("/v1/job_desc")
def gen_jobdesc_hashtags(user_input: UserInput):

    total_keywords = []
    payload = jsonable_encoder(user_input)
    user_content = payload.get('description')
    hashtags = jobdesc_hashtag(user_content)

    response = {
            "success": True,
            "status_code": http_status.OK,
            "message": "Hashtags Generated Successfully",
            "data": hashtags
    }

    return response

@app.post("/v1/headline")
def gen_headline(user_input: UserInput):

    total_keywords = []
    payload = jsonable_encoder(user_input)
    user_content = payload.get('description')
    headline = desc_to_headline(user_content)

    response = {
            "success": True,
            "status_code": http_status.OK,
            "message": "Headline Generated Successfully",
            "data": headline
    }

    return response

@app.post("/v1/product_description")
def gen_prod_description(user_input: ProductDescription):

    total_keywords = []
    payload = jsonable_encoder(user_input)
    prod_name = payload.get('name')
    prod_char = payload.get('characteristics')
    prod_description = product_description(prod_name, prod_char)

    response = {
            "success": True,
            "status_code": http_status.OK,
            "message": "Product Description Generated Successfully",
            "data": prod_description
    }

    return response