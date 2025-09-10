from llama_index.core.tools import QueryEngineTool

def get_tools(engine_dict):
    query_engine_tools = {}
    
    for k, v in engine_dict.items():
        query_engine_tools[k] = QueryEngineTool.from_defaults(
            query_engine=v,
            name=f"{k}_10k",
            description= (
                f"Delivers insights and information about {k}'s 2024 financial data.",
                "You'll provided with a detailed, plain text question to obtain the most relevant and precise responses"
            )
        )

    return query_engine_tools

