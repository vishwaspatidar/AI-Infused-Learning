from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from scrapper import fetch_website_contents   # reuse Class 1's scraper
load_dotenv()

prompt = ChatPromptTemplate.from_template(            # ①
    "Give a short, friendly summary of this website in hindi:\n\n{website}")

model  = ChatGroq(model="openai/gpt-oss-120b", temperature=0.3)   # ②

parser = StrOutputParser()                             # ③

chain = prompt | model | parser                        # ④

def summarize(url):
    return chain.invoke({"website": fetch_website_contents(url)})   # ⑤

user = input("Enter the website URL you want to summarize :  ")
print(summarize(user))