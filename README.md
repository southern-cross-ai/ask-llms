# Ask LLMs

## TL;DR

Input your prompt, get a response and save your Q&As into local Markdown files. Free to use, without API.

Current supported LLMs are:

- Claude2
- Copilot

## Requirements

- Python 3.10+
- Firefox browser installed for Claude
- [geckodriver](https://github.com/mozilla/geckodriver) installed for Claude
- Microsoft account for Copilot cookies (Optional)

## Install API Packages

- For Claude2:
  ``` pip install unofficial-claude2-api ```

  More details on [st1vms/unofficial-claude2-api](https://github.com/st1vms/unofficial-claude2-api?tab=readme-ov-file),

- For Copilot:
  ``` pip install sydney-py ```

  More details on  [vsakkas/sydney.py](https://github.com/vsakkas/sydney.py).

## How to use it?

1. In `main.py`, customise your Markdown file paths for saving Q&As:

``` python
path_claude = '/example_path/examples_claude.md'
path_copilot = '/example_path/examples_copilot.md'
```

2. Input your prompt:

``` Python
prompt = "How are you today?"
```

3. The responses from LLMs will be printed in the terminal and saved as your local files. 

   For example: ![example](./example.png)

4. Run `main.py`.
