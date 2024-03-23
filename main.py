from ask_llms import ask_copilot, ask_claude, ask_gemini
from ask_llms import utils


def main(LLMs):
    for name, (path, llm) in LLMs.items():
        print("Generating from", name, "...")
        response = llm(prompt)
        utils.print_qa(prompt, response)
        utils.save_markdown(path, prompt, response)
    
    
if __name__=='__main__':
    # file paths for saving your Q&As
    path_claude_2 = './tests/claude_2_tests.md'
    path_copilot = './tests/copilot_tests.md'
    path_gemini = './tests/gemini_tests.md'
    
    # input your prompt
    prompt = "Hey LLM, introduce yourself!"
    
    # LLMs that are used for generating responses
    # keep the same structure: {LLM_name: (path_to_markdown, ask_LLM_function)}
    LLMs = {"Claude 2": (path_claude_2, ask_claude), 
            "Copilot": (path_copilot, ask_copilot),
            "Gemini": (path_gemini, ask_gemini)}
    
    main(LLMs)