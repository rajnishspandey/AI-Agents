# AI-Agents
In this repository I have added some example of creating AI Agents.

## Prerequisites
-  must have groq api key if you don't have login to https://groq.com/ from Dev console, generate the key
-  have some basic knowledge of python

# AI Agent creation
After you pull the code make sure to create .env file and save the groq api key into it as GROQ_API_KEY = "yourkey"

1 -  create virtual environment
```shell
python -m venv .venv
```

or 

```shell
conda create -p venv python=3.12
```

2 - activate virtual environment
```shell
conda activate ./.venv/
```
or
```shell
source .venv/bin/activate
```

3 - with given file requirements.txt install all the dependecies 
```shell
pip install -r requirements.txt
```

4 - run the python file
```shell
python financial_agent.py
```

and see the magic

incase if it fails,
just run to check if you see phi and phidata both
```shell
conda list phi
```

if yes then
```shell
pip uninstall phi
```

now you should be good to go. run the python file again and have fun.

Happy learning.

***Note : -*** Groq id in the code can change over the time but no worries you can find it on groq portal anytime inside devconsole>models and use accordingly.

references
https://www.phidata.com/

>  SOME EXTRA INFO

***Helping hands for AI journey***
>  models - ollama.com, huggingface.co

>  AI Agents - phidata.com, microsoft.github.io/autogen/0.2/, langflow.org, 

>  Data Engineering - kaggle.com

>  to deploy the models - groq.com
