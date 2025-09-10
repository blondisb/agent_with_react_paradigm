import dotenv, os
from llama_index.core.agent.workflow import ReActAgent, ToolCallResult, AgentStream
from llama_index.core.workflow import Context
from llama_index.llms.openai import OpenAI
from utils.all_prints import print_error, log_message

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class AgentResponse():
    
    def define_agent_n_context(self, input_tools):
        try:  
            agent = ReActAgent(
                tools = input_tools,
                llm = OpenAI(model="gpt-4o-mini")
            )
            ctx = Context(agent)
            return agent, ctx
        # .
        except Exception as e:
            print_error(e, "Error defining the agent")


    async def call_agent(self, agent: ReActAgent, ctx: Context, question: str):
        try:
            handler = agent.run(
                user_msg=question,
                ctx = ctx
            )
            async for event in handler.stream_events():
                log_message(1001)
                
                if isinstance(event, AgentStream):
                    # print(f"\n----{event}", end="", flush=True)
                    print(f"{event.delta}", end="", flush=True)
                    
                log_message(1002)
            return (await handler)
        except Exception as e:
            print_error(e, "Error calling the agent")