# SimpleLLMTranslateAPP
This is a simple LLM App built using Langchain and Langserve, the application is created using FASTAPI

To run this app locally
1. http://127.0.0.1:8000/chain/invoke, hit this endpoint via POSTMAN with POST Endpoint
2. Pass the following as JSON body

{
  "input": {
    "language": "your choice",
    "user_input": "your sample text"
  }
}
