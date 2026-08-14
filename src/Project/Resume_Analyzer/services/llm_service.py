
from groq import Groq

from ..config.settings import groq_api_key

client = Groq(api_key=groq_api_key)