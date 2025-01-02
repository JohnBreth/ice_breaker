# Ice Breaker

## Getting this error 'bash: __vsc_prompt_cmd_original: command not found'

Can fix this by:
```
unset PROMPT_COMMAND
```

## pipenv items to install:

```
pipenv shell
pipenv install langchain
pipenv install langchain-openai
pipenv install langchain-community
pipenv install langchainhub
pipenv install black
pipenv install python-dotenv
```

## How to add gp envar:

gp env -e VARIABLE_Name="value"

## JSON Validator

https://www.jsonlint.com

## ProxyCurl

People API
https://nubela.co/proxycurl/docs?python#company-api-employee-search-endpoint

Create python code to test pulling data from LinkedIn API, getting data in json, validating at jsonlint, and then creating a gist on GitHub
```
import requests

api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
api_key = $PROXYCURL_API_KEY
headers = {'Authorization': 'Bearer ' + api_key}
params = {
    "url": "https://www.linkedin.com/in/john-breth/",
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

#response.json()
#response._content

https://gist.github.com/JohnBreth/259a68e00f6499437049aa563d6f6df2
https://gist.githubusercontent.com/JohnBreth/259a68e00f6499437049aa563d6f6df2/raw/f37cf281874e2d11baf17d61786475c677f6f4db/john-breth.json

```
