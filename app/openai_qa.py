# from langchain.vectorstores import deeplake # check update
from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage

if __name__ == "__main__":
    print("Testing AzureChatOpenAI")
    model = AzureChatOpenAI(
        openai_api_version="2024-02-15-preview",
        azure_deployment="gpt-vision",
    )
    
    message = HumanMessage(
        content="What is the capital of France?",
    )
    print(model([message]))
    
    