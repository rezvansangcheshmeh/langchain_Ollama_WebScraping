from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from nlp.analyzer import llm

summary_prompt = PromptTemplate.from_template("""
Summarize the following news article in 3 concise lines.

Article:
"{text}"

Summary:
""")
summary_chain = LLMChain(llm=llm, prompt=summary_prompt)

def summarize_article(text):
    return summary_chain.run({"text": text}).strip()
