from azure.identity import DefaultAzureCredential

try:
    credential = DefaultAzureCredential()

    token = credential.get_token(
        "https://ai.azure.com/.default"
    )

    print("SUCCESS")
    print("Token acquired")
    print(token.token[:50] + "...")

except Exception as ex:
    print("FAILED")
    print(ex)