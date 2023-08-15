
import os
import json
import requests
from dotenv import load_dotenv

# import streamlit as st
from langchain.schema import SystemMessage


load_dotenv()
brwoserless_api_key = os.getenv("BROWSERLESS_API_KEY")
serper_api_key = os.getenv("SERP_API_KEY")

# Tool for search
def search(query):
    url = "https://google.serper.dev/search"

    payload  = json.dumps({
        "q":query
    })

    headers = {
        "X-API-KEY": serper_api_key,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    return response.text

search("What are NEXTJs 13 new features?")