from langchain.agents import create_agent

from instance import Instance, Tavily_Instance


#只推荐这种描述方式进行注释，不适用注解方式
def send_email(to: str, subject: str, body: str):
    """
    Agent function that processes the input state and returns the updated state.
    
    This function handles the main reasoning and decision-making logic
    for the agent workflow.
    
    Args:
        state: The current state dictionary containing conversation context
        
    Returns:
        dict: The updated state with agent response
    """
    email = {"to": to, "subject": subject, "body": body}
    return f"Email sent to {to} with subject '{subject}'"


def web_search(query: str):
    """
    Perform a web search for the given query and return the results.
    
    Args:
        query (str): The search query string.
        
    Returns:
        str: The search results.
    """

    ret = Tavily_Instance().search(query)
    return ret


'''
继承basetool定义
'''

agent = create_agent(Instance(),
                     tools=[
                         send_email,
                         web_search,
                     ],
                     system_prompt="你是一个有帮助的助手。你可以发送电子邮件。")
