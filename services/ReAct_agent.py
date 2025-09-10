import dotenv, os
from llama_index.core.agent.workflow import ReActAgent, ToolCallResult, AgentStream
from llama_index.core.workflow import Context
from llama_index.llms.openai import OpenAI
from utils.all_prints import print_error, log_message

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class AgentResponse():
    
    def define_agent(self, input_tools):
        try:
            return ReActAgent(
                tools = input_tools,
                llm = OpenAI(model="gpt-4o-mini")
            )
        except Exception as e:
            print_error(e, "Error defining the agent")


    async def call_agent(self, agent: ReActAgent, question: str):
        try:
            handler = agent.run(
                user_msg=question,
                ctx = Context(agent)
            )
            async for event in handler.stream_events():
                if isinstance(event, AgentStream):
                    # print(f"\n----{event}", end="", flush=True)
                    print(f"\n----{event.delta}", end="", flush=True)
            return (await handler)
        except Exception as e:
            print_error(e, "Error calling the agent")