from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey = '7vO6JMlzWovEtpYazYntroGVfHzZtr8-bicgEOVAk2Gb'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/17c2f935-8435-461c-bed7-08ef9c69ef64'

authenticator = IAMAuthenticator(apikey)
speech2text = SpeechToTextV1(authenticator=authenticator)
speech2text.set_service_url(url)

with open('Voice.mp3', 'rb') as f:
    res = speech2text.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

text = res['results'][0]['alternatives'][0]['transcript']

confidence = res['results'][0]['alternatives'][0]['confidence']

with open('output.txt', 'w') as out:
    out.writelines(text)
