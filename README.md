# Ice Breaker

Getting this error 'bash: __vsc_prompt_cmd_original: command not found'

Can fix this by:
```
unset PROMPT_COMMAND
```

pipenv items to install:

```
pipenv shell
pipenv install langchain
pipenv install langchain-openai
pipenv install langchain-community
pipenv install langchainhub
pipenv install black
pipenv install python-dotenv
```