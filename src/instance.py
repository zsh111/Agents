from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
from openai import api_key, base_url
from tavily import TavilyClient
from env import OPENAI_API_KEY, OPENAI_URL, TAVILY_API_KEY


def get_api_key() -> str:
    if OPENAI_API_KEY is None:
        raise ValueError("OPENAI_API_KEY is not set")
    return OPENAI_API_KEY


def Instance():
    llm = ChatOpenAI(
        model="deepseek-chat",
        temperature=0.7,
        api_key=get_api_key,
        base_url=OPENAI_URL,
    )
    return llm


def Singleton():
    return init_chat_model(
        model="deepseek-chat",
        model_provider="openai",
        api_key=get_api_key,
        base_url=OPENAI_URL,
    )


def Tavily_Instance():
    return TavilyClient(api_key=TAVILY_API_KEY)
