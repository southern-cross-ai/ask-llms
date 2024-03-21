from ask_claude import *
from ask_copilot import *
import asyncio
from utils import *


def main(LLMs):
    for name, (path, llm) in LLMs.items():
        print("Generating from", name)
        response = llm(prompt)
        print_qa(prompt, response)
        save_markdown(path, prompt, response)
    
    
if __name__=='__main__':
    # markdown files to save the prompts and responses
    path_claude = '/Users/yifan/Documents/GitHub/qa-data/biased-examples/biased_examples_copilot.md'
    path_copilot = '/Users/yifan/Documents/GitHub/qa-data/biased-examples/biased_examples_claude_3_sonnet.md'
    # input prompt
    prompt = "How are you today?"
    
    LLMs = {"Claude": (path_claude, ask_claude), 
            "Copilot": (path_copilot, ask_copilot)}
    
    main(LLMs)
    
    
    