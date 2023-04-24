#keys
openai_api_key = "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"

#libraries

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

#chat = ChatOpenAI(temperature=0.7, openai_api_key = openai_api_key)

llm = OpenAI(model_name="text-ada-001", openai_api_key=openai_api_key)
print(llm("what day comes after tuesday?"))
