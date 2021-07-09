apikey = 'EtGPFm9rPIM8fdtWr12VOM7iXvVuCfy6WYFEUqvZ03r2'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/700ce724-fe09-4149-bf8d-deecdf9da1e4'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



authenticator = IAMAuthenticator(apikey)
text_2_speech = TextToSpeechV1(authenticator=authenticator)
text_2_speech.set_service_url(url)

with open('./output.mp3', 'wb') as audio_file:
    res = text_2_speech.synthesize('Hi There! Test One Two Three, Test One Two Three', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
    
