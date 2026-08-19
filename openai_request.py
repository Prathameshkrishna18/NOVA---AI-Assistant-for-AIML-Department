from openai import OpenAI
import os

client = OpenAI(api_key="sk-proj-C3MIA")

#def send_request(query):


#    completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#             "role": "user",
#            "content": query
#           }
#   
# 
#  ]
# )

#return completion.choices[0].message.content

def send_request(query):


    completion = client.chat.completions.create(
         model="gpt-4o-mini",
         messages=query
    )

    return completion.choices[0].message.content
