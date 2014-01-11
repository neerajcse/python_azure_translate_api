import azure_translate_api

client = azure_translate_api.MicrosoftTranslatorClient('client_id',  # make sure to replace client_id with your client id
                                                       'client_secret') # replace the client secret with the client secret for you app.
print client.TranslateText('Good morning my lovely french friends!', 'en', 'fr')