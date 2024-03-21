import io, sys, asyncio
from sydney import SydneyClient
from utils import *


async def _ask_copilot(prompt) -> str:
    """Ask ChatGPT and get a response.

    Args:
        prompt (str): The input prompt.

    Returns:
        str: The response from ChatGPT.
    """
    res = []
    # suppress printing message in terminal
    sys.stdout = io.StringIO()
    async with SydneyClient() as sydney:
        response = await sydney.ask(prompt)
        res.append(response)
    # restore printing
    sys.stdout = sys.__stdout__
    return ''.join(res)


def ask_copilot(prompt):
    response = asyncio.run(_ask_copilot(prompt))
    return response
        

if __name__ == '__main__':
    # path for the markdown file
    path = '/Users/yifan/Documents/GitHub/qa-data/biased-examples/biased_examples_copilot.md'
    # input prompt
    prompt = "How are you today?"
    print("\nGenerating from Copilot ...")
    # response from Copilot
    response = ask_copilot(prompt)
    print_qa(prompt, response)
    save_markdown(path, prompt, response)