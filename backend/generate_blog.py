from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def generate_blog(topic):
    """Generates a full blog post based on a given topic using GPT-4."""
    
    template = """Write a detailed blog post on the topic "{topic}".
    - Include an engaging introduction
    - Provide 3 key points with explanations
    - Use SEO-friendly keywords
    - End with a conclusion and call to action

    Return the blog in structured markdown format.
    """

    prompt = PromptTemplate(input_variables=['topic'], template=template)
    llm = ChatOpenAI(model_name = "gpt-4", openai_api_key = OPENAI_API_KEY)
    chain = LLMChain(llm = llm, prompt= prompt)

    return chain.run(topic= topic)
