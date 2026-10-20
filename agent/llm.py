"""LLM setup for the Terraform Security Review Agent.

Every chain imports `llm` from this module, so the model, endpoint and
temperature are configured in one place.
"""

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model=os.environ["ZAI_MODEL"],
    openai_api_key=os.environ["ZAI_API_KEY"],
    openai_api_base=os.environ["ZAI_API_BASE"],
    temperature=0.1,  # low: the same finding should get a consistent explanation
)


if __name__ == "__main__":
    response = llm.invoke("Reply with one short sentence confirming you are working.")
    print(response.content)