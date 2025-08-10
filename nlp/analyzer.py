from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import json

llm = Ollama(model="mistral")
template = """
Analyze the following news article and:
1. Extract 3 to 5 important keywords.
2. Classify the article into one category.

Article:
"{text}"

Respond only with JSON:
{{
  "keywords": [...],
  "category": "..."
}}
"""
prompt = PromptTemplate(template=template, input_variables=["text"])
chain = LLMChain(llm=llm, prompt=prompt)

def analyze_news(text):
    result = chain.run({"text": text})
    try:
        parsed = json.loads(result)
        return parsed.get("keywords", []), parsed.get("category", "Unknown")
    except json.JSONDecodeError:
        return [], "Unknown"
