import os
import requests
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex


url_docs = {
        "apple": """https://s2.q4cdn.com/470004039/files/doc_earnings/2024/q4/filing/10-Q4-2024-As-Filed.pdf""",
        "nvidia": """https://s201.q4cdn.com/141608511/files/doc_financials/2024/q4/1cbe8fe7-e08a-46e3-8dcc-b429fc06c1a4.pdf"""
    }


def getdoc():
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


def loading_storage():
    pdir = "./storage"
    if not os.path.exists(pdir):
        os.makedirs(pdir)

    try:
        storage_context = StorageContext.from_defaults(persist_dir=pdir)
        apple_index = load_index_from_storage(storage_context)

        storage_context = StorageContext.from_defaults(persist_dir=pdir)
        nvidia_index = load_index_from_storage(storage_context)
        
        index_loaded = True
    except Exception as e:
        print(f"Error loading indices: {e}")
        index_loaded = False


    if not index_loaded:
        apple_docs = SimpleDirectoryReader(
            input_files=["pdfs/apple_10k.pdf"]
        ).load_data()

        nvidia_docs = SimpleDirectoryReader(
            input_files=["pdfs/nvidia_10k.pdf"]
        ).load_data()

        apple_index = VectorStoreIndex.from_documents(apple_docs)
        nvidia_index = VectorStoreIndex.from_documents(nvidia_docs)

        apple_index.storage_context.persist(persist_dir=pdir)
        nvidia_index.storage_context.persist(persist_dir=pdir)