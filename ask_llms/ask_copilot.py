import io, sys, asyncio

# https://github.com/vsakkas/sydney.py
from sydney import SydneyClient

import utils


async def _ask_copilot(prompt):
    response = []
    # suppress messages from APIs
    sys.stdout = io.StringIO()
    async with SydneyClient() as sydney:
        # send a prompt to Copilot and return the response
        response.append(await sydney.ask(prompt))
    # restore suppressed messages
    sys.stdout = sys.__stdout__
    return ''.join(response)


def ask_copilot(prompt):
    response = asyncio.run(_ask_copilot(prompt))
    return response
        

if __name__ == '__main__':
    path = './tests/copilot_tests.md'
    prompt = "What's the weather today?"
    print("\nGenerating from Copilot ...")
    response = ask_copilot(prompt)
    utils.print_qa(prompt, response)
    utils.save_markdown(path, prompt, response)