import openai
from datetime import datetime
from anytree import Node, RenderTree
import numpy as np

openai.api_key = "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"

#parameters
retrieval_size = 10
reflection_trigger = 0.9


memory_stream = {
    "Time_of_creation": [],
    "Last_accessed": [],
    "Type": [],
    "Description": [],
    "Embedding_Vector": [],
    "Score": []
}

retrieved_memories = {
    "Time_of_creation": [],
    "Last_accessed": [],
    "Type": [],
    "Description": [],
    "Embedding_Vector": [],
    "Score": []
}

#create main loop to collect inputs here




def queryLLM(prompt: str, tokens: int):
    response = openai.Completion.create(engine = 'text-ada-001', 
                                    prompt = prompt, 
                                    max_tokens = tokens,
                                    n = 1,
                                    temperature = 0.5)
    print(response.choices[0].text)
    return response.choices[0]


def add_memory(input: str, type: str):
    #add input to memory stream
    #assign importance score
    #create embedding vector for the input
    memory_stream["Time_of_creation"].append(datetime.now())
    memory_stream["Last_accessed"].append(datetime.now())
    memory_stream["Type"].append(type)
    memory_stream["Description"].append(input)
    memory_stream["Recency"].append("")
    memory_stream["Relevence"].append("")
    importance_rating = importance(input)
    memory_stream["Importance"].append(importance_rating)
    memory_stream["Score"].append("")

    if importance_rating >= reflection_trigger:
        reflection(input, type)
    #memory_stream["Embedding_Vector"] "figure out how to create embedding vector"

def update_scores(input: str):

    for i in range(len(memory_stream)):
        memory_stream["Recency"][i] = recency(i)
        memory_stream["Relevence"][i] = relevence(input, i)
        memory_stream["Score"][i] = memory_stream["Recency"][i] + memory_stream["Relevence"][i] + memory_stream["Importance"][i]

    
def recency(index: int):
    #this creates recency factor with linearly decreasing rating based on length of memory
    
    rating = index / len(memory_stream["Type"])
    return rating


def importance(input: str):

    prompt = "On the scale of 1 to 10, where 1 is purely mundane \
            (e.g., brushing teeth, making bed) and 10 is \
            extremely poignant (e.g., a break up, college \
            acceptance), rate the likely poignancy of the \
            following piece of memory. \
            Memory: buying groceries at The Willows Market \
            and Pharmacy Rating: <fill in>"
    
    rating = queryLLM(prompt, 5)
    rating = rating/10
    return rating


def relevence(input: str, index: int):

    #access embedding vectors and compare using cosine similarity somehow

    #memory_stream["Embedding_Vector"][index]
    rating = 0.5
    return rating


def retrieval(input: str):

    update_scores(input)
    score_array = np.array(memory_stream["Score"])
    retrieval_bank = np.argsort(score_array)[-retrieval_size:]
    return retrieval_bank


def determine_response(inprompt: str, retreivallist):
    #build prompt based on retreivallist
    prompt = "hi"
    response = queryLLM(prompt, 50)
    return response


def reflection():
    memories = []
    if len(memory_stream["Description"]) < 100:
        a = len(memory_stream["Description"])
    elif len(memory_stream["Description"]) >= 100:
        a = 100

    for i in range(a):
        memories.append(memory_stream["Description"][len(memory_stream["Description"]) - i])

    for i in range(len(memories)):
        prompt = str(i) + ". " + memories[i] + ", "
    prompt = prompt + "Given only the information above what are the 3 most salient \
          high-level questions we can answer about the subjects in the statements?"
    
    response = queryLLM(prompt, 100)

    #use response to get retrieval of memories
    questions = response.split(?)
    
    for i in range(len(questions)):
        relevent_memories[i] = retrieval(questions[i])

    for i in range(len(relevent_memories)):
        prompt = str(i) + ". " + memories[i] + ", "

    prompt = prompt + "What high level insights can you infer from the above statement \
        (example format: insight (because of 1, 3, 8))"
    response = queryLLM(prompt, 100)

    add_memory(response, "Reflection")


def create_plan():

    

