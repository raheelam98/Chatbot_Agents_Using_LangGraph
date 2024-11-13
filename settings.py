import os

# Get all environemnt variables
os.environ['GEMINI_API_KEY']  = os.getenv('GEMINI_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['TAVILY_API_KEY']  = os.getenv('TAVILY_API_KEY')