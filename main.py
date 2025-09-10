import os
import dotenv
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from services import document_storing, tools, ReAct_agent

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
    document_storing.getdoc()
    engine_dict = document_storing.loading_storage()

    tools_dict = tools.get_tools(engine_dict)
