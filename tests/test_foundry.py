from openai import OpenAI
from azure.identity import AzureCliCredential, get_bearer_token_provider

endpoint = "https://azurearchitecturecopilo-resource.services.ai.azure.com/openai/v1"
deployment_name = "gpt-4o"

credential = AzureCliCredential()

token_provider = get_bearer_token_provider(
    credential,
    "https://ai.azure.com/.default"
)

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

response = client.responses.create(
    model=deployment_name,
    input="What is Azure AI Foundry?"
)

print(response.output_text)