from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from configs.settings import MODEL_REPO_ID, TEMPERATURE, MAX_TOKENS
import os

def load_deepseek_model():
    """
    The function `load_deepseek_model` loads a model from the Hugging Face model hub for chat
    generation.
    :return: An instance of the `ChatHuggingFace` class with the `llm` attribute set to the result of
    loading a model using the Hugging Face API.
    """
    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    llm = HuggingFaceEndpoint(
        repo_id=MODEL_REPO_ID, 
        huggingfacehub_api_token=token,
        temperature=TEMPERATURE,
        max_new_tokens=MAX_TOKENS
    )
    return ChatHuggingFace(llm=llm)
