from langchain_openai import ChatOpenAI
from openai import api_key
from agents import __version__
from env import OPENAI_API_KEY, OPENAI_URL


def test_version():
    assert __version__ == "0.1.0"


def get_api_key() -> str:
    if OPENAI_API_KEY is None:
        raise ValueError("OPENAI_API_KEY is not set")
    return OPENAI_API_KEY


def chat():
    llm = ChatOpenAI(
        model="deepseek-chat",
        temperature=0.7,
        api_key=get_api_key,
        base_url=OPENAI_URL,
    )
    resp = llm.invoke("简单介绍你自己")
    print(resp.content)


if __name__ == "__main__":

    chat()
