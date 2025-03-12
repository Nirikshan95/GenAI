# import libraries
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.title(' Personalized Story Generator')
story_type=st.text_input(label='Enter you Story type')
llm=HuggingFaceEndpoint(repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0')

template=PromptTemplate(template='write a {story_type} story it should be engaging and grab the interest',input_variables=['story_type'])
model=ChatHuggingFace(llm=llm)
if st.button(label='Generate story'):
    prompt=template.invoke({'story_type':story_type})
    result=model.invoke(prompt)
    st.write(result.content)