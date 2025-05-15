from dotenv import find_dotenv, load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from settings import OPENAI_MODEL
from template import TEMPLATE

_ = load_dotenv(find_dotenv('.env'))

openai = ChatOpenAI(model=OPENAI_MODEL)

prompt_template = PromptTemplate.from_template(TEMPLATE)
