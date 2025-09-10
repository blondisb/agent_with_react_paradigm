
def print_error(e: Exception, context: str = ""):
    print(f"\n-------------------\nERROR:\n in {context}: {e}")
    print("------------\n")
    raise e

def log_message(message):
    print(f"\n=============\nLOG:\n {message}\n")