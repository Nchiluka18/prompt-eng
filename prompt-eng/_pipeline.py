##
## Prompt Engineering Lab
## Platform for Education and Experimentation with Prompt NEngineering in Generative Intelligent Systems
## _pipeline.py :: Simulated GenAI Pipeline 
## 
#  
# Copyright (c) 2025 Dr. Fernando Koch, The Generative Intelligence Lab @ FAU
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# Documentation and Getting Started:
#    https://github.com/GenILab-FAU/prompt-eng
#
# Disclaimer: 
# Generative AI has been used extensively while developing this package.
# 


import requests
import json
import os
import time

def load_config():
    """
    Load config file looking into multiple locations
    """
    config_locations = [
        "./_config",
        "prompt-eng/_config",
        "../_config"
    ]
    
    # Find CONFIG
    config_path = None
    for location in config_locations:
        if os.path.exists(location):
            config_path = location
            break
    
    if not config_path:
        raise FileNotFoundError("Configuration file not found in any of the expected locations.")
    
    # Load CONFIG
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()


def create_payload(model, prompt, target="ollama", **kwargs):
    """
    @NOTE: Need to adjust here to support multiple target formats
    """
    payload = None
    if target == "ollama":
        payload = {
            "model": model,
            "prompt": prompt, 
            "stream": False,
        }
        if kwargs:
            payload["options"] = {key: value for key, value in kwargs.items()}
    elif target == "open-webui":
        payload = {
            "model": model,
            "messages": [ {"role" : "user", "content": prompt } ]
        }

        ## @NOTE: Need to load parameters for Open-WebUI payload
        ###
        
        #if kwargs:
        #    payload["options"] = {key: value for key, value in kwargs.items()}
    
    else:
        print(f'!!ERROR!! Unknown target type {target}')
    return payload


def model_req(payload=None):
    """
    COMPLETE
    """
        
    # CUT-SHORT Condition
    try:
        load_config()
    except:
        return -1, f"!!ERROR!! Problem loading prompt-eng/_config"

    url = os.getenv('URL_GENERATE', None)
    api_key = os.getenv('API_KEY', None)
    delta = response = None

    headers = dict()
    headers["Content-Type"] = "application/json"
    if api_key: headers["Authorization"] = f"Bearer {api_key}"

    #print(url, headers)
    #print(payload)

    # Send out request to Model Provider
    try:
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload) if payload else None, headers=headers)
        delta = time.time() - start_time
    except:
        return -1, f"!!ERROR!! Request failed! You need to adjust prompt-eng/config with URL({url})"

    # Checking the response and extracting the 'response' field
    if response is None:
        return -1, f"!!ERROR!! There was no response (?)"
    elif response.status_code == 200:

        ## @NOTE: Need to adjust here to support multiple response formats
        result = ""
        delta = round(delta, 3)

        response_json = response.json()
        if 'response' in response_json: ## ollama
            result = response_json['response']
        elif 'choices' in response_json: ## open-webui
            result = response_json['choices'][0]['message']['content']
        else:
            result = response_json 
        
        return delta, result
    elif response.status_code == 401:
        return -1, f"!!ERROR!! Authentication issue. You need to adjust prompt-eng/config with API_KEY ({url})"
    else:
        return -1, f"!!ERROR!! HTTP Response={response.status_code}, {response.text}"
    return


###
### DEBUG
###

if __name__ == "__main__":
    from _pipeline import create_payload, model_req
    MESSAGE = """
    You are an intelligent personal finance assistant. A user has provided their financial data. Your task is to analyze their income, expenses, and investments, and offer tailored advice for improving their financial situation.

    Example 1:
    User’s financial data:
    - Monthly income: $6,000
    - Monthly expenses: $4,000
    - Savings goal: Save $12,000 in the next 6 months
    - Investments: $10,000 in real estate

    AI’s response:
    - You have $2,000 in disposable income per month. Consider cutting down on unnecessary expenses (e.g., dining out) to save an additional $500 each month.
    - You’re on track to meet your savings goal, but you can invest in a more diversified portfolio to potentially increase returns.

    Example 2:
    User’s financial data:
    - Monthly income: $5,000
    - Monthly expenses: $2,800
    - Savings goal: Save $8,000 in the next 10 months
    - Investments: $7,000 in stocks

    AI’s response:
    - You have a $1,200 surplus each month. You are in a good position to reach your savings goal early. Consider investing in bonds or diversifying your portfolio for better returns.

    Now, analyze the following user's financial data and provide similar advice:
    User’s financial data:
    - Monthly income: $5,000
    - Monthly expenses: $3,200 (including rent, utilities, food, etc.)
    - Savings goal: Save $10,000 in the next 12 months
    - Investments: $5,000 in stocks (portfolio includes 60% tech, 30% healthcare, 10% bonds)
    """
    PROMPT = MESSAGE
    payload = create_payload(
                         target="open-webui",   
                         model="qwen2", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

    time, response = model_req(payload=payload)
    print(response)
    if time: print(f'Time taken: {time}s')
