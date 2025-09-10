from llama_index.core.agent.worklflow import ReActAgent
from llama_index.core.workflow import Context

def call_agent(query_engine_tools, question):
    q = list(query_engine_tools.values())
    agent = ReActAgent(
        tools = query_engine_tools,
        llm = OpenAI(model="gpt-4o-mini")
    )