from openai import OpenAI
from azure.identity import AzureCliCredential, get_bearer_token_provider

endpoint = "https://azurearchitecturecopilo-resource.services.ai.azure.com/openai/v1"

credential = AzureCliCredential()

token_provider = get_bearer_token_provider(
    credential,
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)