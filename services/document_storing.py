import os
import requests
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from utils.all_prints import print_error

url_docs = {
    "Apple": """https://s2.q4cdn.com/470004039/files/doc_earnings/2024/q4/filing/10-Q4-2024-As-Filed.pdf""",
    "Nvidia": """https://s201.q4cdn.com/141608511/files/doc_financials/2024/q4/1cbe8fe7-e08a-46e3-8dcc-b429fc06c1a4.pdf"""
}

class DocumentStoring():
    
    def getdoc(self):
        try:
            if not os.path.exists("pdfs"):
                os.makedirs("pdfs")

            for k, v in url_docs.items():
                r = requests.get(v)
                # Verify that we received PDF content
                if 'application/pdf' in r.headers.get('content-type', '').lower():
                    with open(f"pdfs/{k}_10k.pdf", "wb") as f:
                        f.write(r.content)
                else:
                    print(f"Warning: {k} URL did not return PDF content")
        except Exception as e:
            print_error(e, "Error downloading documents")


    def loading_storage(self):
        try:
            self.getdoc()
            pdir = "./storage"
            
            if not os.path.exists(pdir):
                os.makedirs(pdir)

            try:
                index_list = {}
                for key in url_docs.keys():
                    index_list[key] = load_index_from_storage(
                        StorageContext.from_defaults(persist_dir=f"{pdir}/{key}")
                    )
                index_loaded = True
            except Exception as e:
                print(f"Error loading indices: {e}")
                index_loaded = False

            if not index_loaded:
                engine_dict = {}
                for key in url_docs.keys():
                    doc = SimpleDirectoryReader(
                        input_files=[f"pdfs/{key}_10k.pdf"]
                    ).load_data()

                    index = VectorStoreIndex.from_documents(doc)
                    index.storage_context.persist(persist_dir=f"{pdir}/{key}")
                    engine_dict[key] = index.as_query_engine(similarity_top_k=3)

                return engine_dict
        except Exception as e:
            print_error(e, "Error in loading or creating storage")
            
            

                    
                    