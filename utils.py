def save_markdown(path, prompt, response):
    with open(path, 'a+') as file:
        file.write('\n')
        file.write("## {}\n".format(prompt))
        file.write(response)
    print("Saved at", path, '\n')


def print_qa(prompt, response):
    print("\nPrompt:\n", prompt)
    print("\nResponse:\n", response, '\n')