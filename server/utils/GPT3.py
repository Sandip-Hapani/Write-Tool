from server.utils import config
import openai

openai.api_key = config.openai_api_key

class GPT3:
    
    def completion(self, prompts, tmp=0.96, p_top=1, m_tokens=256):
        
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompts,
            temperature=tmp,
            max_tokens=m_tokens,
            top_p=p_top,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"]
        )   
    
        return response
    
    def extract_keyword(self, user_para):
        with open("server/prompts/keywords.prompt") as f:
            prompt = f.read()

        prompt = prompt + "\n###\nTopic: " + user_para + "\n***\nKeywords:"
        response = self.completion(prompt)
        keywords = response['choices'][0]['text']

        return keywords


    def keyword_to_para(self, keywords):
        with open("server/prompts/key_para.prompt") as f:
            prompt = f.read()
        
        prompt = prompt + "\n###\nKeywords: " + keywords + "\n***\nParagraph:"
        response = self.completion(prompts=prompt, tmp=0.88, m_tokens=350, p_top=0.96)
        first_para = response['choices'][0]['text']

        return first_para
    
    def content_rephrase(self, user_content):
        
        prompt = "Paraphrase the below-given Content" + "\n###\nContent: " + user_content + "\n***\nOutput:"
        response = self.completion(prompt)        
        result = response['choices'][0]['text']

        return result
    
    def content_summeriser(self, user_content):
        
        prompt = "Summarise the below-given Content in one to two lines" + "\n###\nContent: " + user_content + "\n***\nSummary:"
        response = self.completion(prompt)        
        result = response['choices'][0]['text']

        return result
    
    def content_email_writer(self, user_content):
        
        prompt = "Write an email on the below-given user content with subjects, salutations and closing" + "\n###\nContent: " + user_content + "\n***\Email:"
        response = self.completion(prompt)        
        result = response['choices'][0]['text']

        return result
    
    def content_tagline_generator(self, user_content):
        
        prompt = "Generate a catchy tagline from the below-given description." + "\n###\nDescription: " + user_content + "\n***\Tagline:"
        response = self.completion(prompt)        
        result = response['choices'][0]['text']

        return result
    
    def content_blog_post_outline(self, topic):
        
        prompt = "Generate 5 outlines of the below-given Topic." + "\n###\Topic: " + topic + "\n***\nOutlines:"
        response = self.completion(prompt)        
        result = response['choices'][0]['text'] + "\n6. Conclusion"

        return result
    
    def content_jobdesc_hashtag(self, job_desc):
        
        prompt = "Generate a relevant hashtags from the below-given job description." + "\n###\nJob Description: " + job_desc + "\n***\Hashtags:"
        response = self.completion(prompt)        
        result = response['choices'][0]['text']

        return result
    
    def content_headline_generator(self, content):
        
        prompt = "Generate a headline from the below-given content." + "\n###\nContent: " + content + "\n***\Headline:"
        response = self.completion(prompt)        
        result = response['choices'][0]['text']

        return result
    
    def content_product_description(self, prod_name, prod_char):
        
        prompt = "Generate a catchy product description from the below-given product name and product characteristics." + "\n###\nProduct Name: " + prod_name + "\nProduct Characteristics: " + prod_char + "\n***\Product Description:"
        response = self.completion(prompt)        
        result = response['choices'][0]['text']

        return result