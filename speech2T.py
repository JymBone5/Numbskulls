
#Libraries
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

#key
openai.api_key="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"
key="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"

#model
model_id='whisper-1'

media_file_path= 'C:/GitHub_repos/Numbskulls/Prompt_rec/PplonEarth.m4a'
media_file=open(media_file_path,'rb')

response=openai.Audio.transcribe(
    model=model_id,
    file=media_file,
    #response_format='srt' # text,json,srt,vtt

)
print(response['text'])

llm = OpenAI(model_name="text-ada-001",openai_api_key=key)
print(llm(response['text']))




