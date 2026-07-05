from requests import head
from server.utils.GPT3 import GPT3


total_keywords = []

def length_gen(keys):

    for i in keys:
        if i in total_keywords:
            keys.remove(i)
        else:
            total_keywords.append(i.lstrip())

    return keys

def next_para_gen(total_paras):

    gpt_obj = GPT3()
    para_keys = gpt_obj.extract_keyword(total_paras)
    para_keys = length_gen(para_keys.split(", "))
    para_keys = ", ".join(para_keys)
    paragraph = gpt_obj.keyword_to_para(keywords=para_keys)

    return paragraph


def gen_article(user_para):

    gpt3_keyword = GPT3()
    keywords = gpt3_keyword.extract_keyword(user_para)
    keys = length_gen(keywords.split(", "))
    
    half = len(keys)//2
    para1_keys = ", ".join(keys[:half])
    para2_keys = ", ".join(keys[half:])

    paragraph1 = gpt3_keyword.keyword_to_para(keywords=para1_keys)
    paragraph2 = gpt3_keyword.keyword_to_para(keywords=para2_keys)
    total_paras = paragraph1 + paragraph2

    paragraph3 = next_para_gen(total_paras)
    paragraph4 = next_para_gen(total_paras + paragraph3)

    return paragraph1+paragraph2+paragraph3+paragraph4

def rephraser(user_content):
    
    reph = GPT3()
    rephrased_content = reph.content_rephrase(user_content).strip()
    
    return rephrased_content

def summary_gen(user_content):
    
    reph = GPT3()
    summary = reph.content_summeriser(user_content).strip()
    
    return summary

def write_email(user_content):
     
    email = GPT3()
    written_email = email.content_email_writer(user_content).strip()
    
    return written_email

def tagline_generator(user_content):
     
    tagline = GPT3()
    tagline = tagline.content_tagline_generator(user_content).strip()
    
    return tagline

def blog_post_outline(user_content):
     
    blog = GPT3()
    outline = blog.content_blog_post_outline(user_content).strip()
    
    return outline

def jobdesc_hashtag(user_content):
     
    job_desc = GPT3()
    hashtags = job_desc.content_jobdesc_hashtag(user_content).strip()
    
    return hashtags

def desc_to_headline(user_content):
    
    headline = GPT3()
    gen_headline = headline.content_headline_generator(user_content).strip()
    
    return gen_headline
    
def product_description(prod_name, prod_char):
     
    prd = GPT3()
    prod_desc = prd.content_product_description(prod_name=prod_name, prod_char=prod_char).strip()
    
    return prod_desc

