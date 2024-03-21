# Ask LLMs

## TL;DR

Input your prompt, generate a response and save your Q&As into local Markdown files. Free to use.

Current supported LLMs are:

- Claude 2
- Copilot

## Requirements

- Python 3.10+
- Firefox browser installed for Claude
- [geckodriver](https://github.com/mozilla/geckodriver) installed for Claude
- Microsoft account for Copilot cookies (Optional)

## Install API Packages

- For Claude 2:
  ``` pip install unofficial-claude2-api ```

  More details on [st1vms/unofficial-claude2-api](https://github.com/st1vms/unofficial-claude2-api?tab=readme-ov-file).

- For Copilot:
  ``` pip install sydney-py ```

  More details on  [vsakkas/sydney.py](https://github.com/vsakkas/sydney.py).

## How to use it?

1. In `main.py`, customise your Markdown file paths for saving Q&As to local:

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

## Seek help

- Anything related to API packages:
Seek help from [st1vms/unofficial-claude2-api](https://github.com/st1vms/unofficial-claude2-api?tab=readme-ov-file) and [vsakkas/sydney.py](https://github.com/vsakkas/sydney.py).

- Anything related to this repo:
Create issues/discussions/PRs and let's figure it out together :)
