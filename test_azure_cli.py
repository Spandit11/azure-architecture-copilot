from azure.identity import AzureCliCredential

try:
    credential = AzureCliCredential()

    token = credential.get_token(
        "https://ai.azure.com/.default"
    )

    print("SUCCESS")
    print(token.token[:50] + "...")

except Exception as ex:
    print("FAILED")
    print(ex)