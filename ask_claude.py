from sys import exit as sys_exit
from claude2_api.client import (
    ClaudeAPIClient,
    SendMessageResponse,
)
from claude2_api.session import SessionData, get_session_data
from claude2_api.errors import ClaudeAPIError, MessageRateLimitError, OverloadError

import io, sys
from utils import *

def ask_claude(prompt):
    sys.stdout = io.StringIO()
    # automatically retrieve a SessionData instance using selenium, 
    # gather cookie session, user agent and organization ID
    session: SessionData = get_session_data()
    # initialize a client instance using a session
    client = ClaudeAPIClient(session, timeout=240)
    # Create a new chat and cache the chat_id
    chat_id = client.create_chat()
    if not chat_id:
        print("\nMessage limit hit, cannot create chat...")
        return
    try:
        # send message with/without attachments
        res: SendMessageResponse = client.send_message(
            chat_id, prompt, attachment_paths=None
        )
        if res.answer:
            sys.stdout = sys.__stdout__
            return res.answer
        else:
            print(f"\nError code {res.status_code}, raw_answer: {res.raw_answer}")
    except ClaudeAPIError as e:
        if isinstance(e, MessageRateLimitError):
            print(f"\nMessage limit hit, resets at {e.reset_date}")
            print(f"\n{e.sleep_sec} seconds left until -> {e.reset_timestamp}")
        elif isinstance(e, OverloadError):
            print(f"\nOverloaded error: {e}")
        else:
            print(f"\nGot unknown Claude error: {e}")
    finally:
        client.delete_chat(chat_id)
    # delete all chats
    client.delete_all_chats()
    sys.stdout = sys.__stdout__

if __name__ == '__main__':
    # path for the markdown file
    path = '/Users/yifan/Documents/GitHub/qa-data/biased-examples/biased_examples_claude_3_sonnet.md'
    # input prompt
    prompt = "How are you today?"
    print("\nGenerating from Claude ...")
    # response from Copilot
    response = ask_claude(prompt)
    print_qa(prompt, response)
    save_markdown(path, prompt, response)