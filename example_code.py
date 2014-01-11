import azure_translate_api

azure_client = azure_translate_api.AzureTranslateAPI('client_id',  # make sure to replace client_id with your client id
                                                     'client_secret') # replace the client secret with the client secret for you app.
print azure_client.TranslateText('Good morning my love', 'en', 'fr')