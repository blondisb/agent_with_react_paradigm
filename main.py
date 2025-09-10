import os
import dotenv
import shutil
import asyncio
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from services import tools
from services.document_storing import DocumentStoring 
from services.ReAct_agent import AgentResponse
from utils.all_prints import log_message

dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

Settings.llm = OpenAI(
    model="gpt-4o-mini"
    # ,api_key=os.getenv("OPENAI_API_KEY"),
)

Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small"
    # ,api_key=os.getenv("OPENAI_API_KEY")
)



if __name__ == "__main__":

    async def main():
        # delete storage folder if exists
        if os.path.exists("storage"): shutil.rmtree("storage")
        
        docs_serv = DocumentStoring()
        agents_serv = AgentResponse()
        
        engine_dict = docs_serv.loading_storage()
        log_message(engine_dict)
        
        tool_list = tools.get_tools(engine_dict)
        log_message(tool_list)
        
        agent = None
        if not agent: agent, context = agents_serv.define_agent_n_context(tool_list)
        log_message(agent)
            
        qa1 = "What was the revenue of Nvidia in 2024? Comapre this value to 2023 revnue?"
        qa2 = "What was the revenue of Apple in 2024? Comapre it to Nvidia's revenue?"
        
        response = await agents_serv.call_agent(agent, context, qa1+qa2)
        log_message(response)
        

    asyncio.run(main())