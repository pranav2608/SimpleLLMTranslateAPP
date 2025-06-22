import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from langserve import add_routes
from pydantic import BaseModel


# Load API key
groq_api_key = os.getenv("GROQ_KEY")

# Define LangChain components
model = ChatGroq(model="gemma2-9b-it", groq_api_key=groq_api_key)  # model name fixed to a valid one

system_template = "Translate the following into {language}: "
prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{user_input}")
])
parser = StrOutputParser()

# Compose the chain
chain: Runnable = prompt | model | parser

# Define input schema
class TranslationInput(BaseModel):
    language: str
    user_input: str

# Define FastAPI app
app = FastAPI(
    title="This is demo langchain server",
    version="1.0",
    description="A Simple API server"
)

# Add the LangChain route with input schema
add_routes(
    app,
    chain,
    path="/chain",
    input_type=TranslationInput
)

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
