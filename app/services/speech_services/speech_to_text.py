#from app.config import SPEECH_SERVICE_KEY, REGION
import azure.cognitiveservices.speech as speechsdk

from config import SPEECH_SERVICE_KEY, REGION

    
def recognize_from_microphone():
    try:
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_SERVICE_KEY, region=REGION)
        speech_config.speech_recognition_language = "en-US"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        return speech_recognition_result.text
    except Exception as e:
        raise RuntimeError("An error occurred during speech recognition: {}".format(e))
    

