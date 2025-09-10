# from pydantic import BaseModel, RootModel
# from typing import Any
# from llama_index.core.tools import QueryEngineTool
# from llama_index.core import VectorStoreIndex

# # class ModelEngineDict(RootModel[dict[str, Any]]):
# #     pass

# # class ToolList(RootModel[list[Any]]):
# #     pass

# # class ToolList(RootModel[list[QueryEngineTool]]):
# #     model_config = {"arbitrary_types_allowed": True}

# class EngineIndexDict(RootModel[dict[str, VectorStoreIndex]]):
#     pass