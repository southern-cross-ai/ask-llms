import io, sys, asyncio, importlib.util
from gemini_webapi import GeminiClient


async def _ask_gemini(prompt):
    # suppress messages from APIs
    sys.stdout = io.StringIO()
    if importlib.util.find_spec('broswer-cookie3'):
        # if browser-cookie3 is installed, simply use client = GeminiClient()
        # it will auto-load cookies from your broswer
        client = GeminiClient()
    else:
        # if you prefer to use your own cookies:
        # 1. open Gemini ((https://gemini.google.com/app)) in your browser
        # 2. log in your Google account
        # 3. use f-12 to open your developer tool and find network tab
        # 4. click any request and find cookies named "__Secure_1PSID" and "_Secure_1PSIDTS" (optional)
        # 5. chop off "__Secure_1PSID=" or "__Secure_1PSIDTS=" at the beginning and ";" at the end
        # 6. copy and paste into the following two variables
        Secure_1PSID = ''
        Secure_1PSIDTS = ''  # optional
        client = GeminiClient(Secure_1PSID, Secure_1PSIDTS, proxies=None)
    await client.init(timeout=30, auto_close=True, auto_refresh=False, verbose=False)
    response = await client.generate_content(prompt)
    # restore suppressed messages
    sys.stdout = sys.__stdout__
    return response.text


def ask_gemini(prompt):
    response = asyncio.run(_ask_gemini(prompt))
    return response


if __name__ == '__main__':
    import utils
    path = './tests/gemini_tests.md'
    prompt = "When is the next holiday in Canberra 2024?"
    print("\nGenerating from Gemini ...")
    response = ask_gemini(prompt)
    utils.print_qa(prompt, response)
    utils.save_markdown(path, prompt, response)