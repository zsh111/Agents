from httpx import stream
from langchain_openai import ChatOpenAI
from openai import api_key
from agents import __version__
from env import OPENAI_API_KEY, OPENAI_URL
from instance import Instance


def test_version():
    assert __version__ == "0.1.0"

def stream_chat():
    for chunk in Instance().stream('用三句话介绍机器学习'):
        print(chunk)

    


if __name__ == "__main__":

    stream_chat()
