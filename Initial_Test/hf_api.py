from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
llm=HuggingFaceEndpoint(repo_id='deepseek-ai/DeepSeek-Prover-V2-671B')
model=ChatHuggingFace(llm=llm)
result=model.invoke('how we can use deepseek to find the best answer for a question?')
print(result.content)