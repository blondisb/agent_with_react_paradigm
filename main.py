import os
import dotenv
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from document_storing import getdoc, loading_storage

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
    getdoc()
    loading_storage()
