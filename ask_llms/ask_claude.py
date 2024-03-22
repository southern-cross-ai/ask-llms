import io, sys

#https://github.com/st1vms/unofficial-claude2-api?tab=readme-ov-file
from claude2_api.client import ClaudeAPIClient, SendMessageResponse
from claude2_api.session import SessionData, get_session_data
from claude2_api.errors import ClaudeAPIError, MessageRateLimitError, OverloadError

import utils


def ask_claude(prompt):
    # suppress messages from APIs
    sys.stdout = io.StringIO()
    # retrieve Claude 2 session data by using default Firefox Browser profile
    session: SessionData = get_session_data()
    # initialize a client instance using a session
    client = ClaudeAPIClient(session, timeout=240)
    # create a new chat and return its UUID
    chat_id = client.create_chat()
    if not chat_id:
        print("\nReach message limit!")
        return
    try:
        # send message without attachments
        res: SendMessageResponse = client.send_message(
            chat_id, prompt, attachment_paths=None
        )
        # if it successfully generates responses
        if res.answer:
            # restore suppressed messages
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
    # restore suppressed messages
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
    path = './tests/claude_2_tests.md'
    prompt = "What's the weather today?"
    print("\nGenerating from Claude 2 ...")
    response = ask_claude(prompt)
    utils.print_qa(prompt, response)
    utils.save_markdown(path, prompt, response)