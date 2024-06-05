# from app.config import SPEECH_SERVICE_KEY, REGION
import azure.cognitiveservices.speech as speechsdk

from config import SPEECH_SERVICE_KEY, REGION

    
def synthesize_speech(text):
    try:
        speech_config = speechsdk.SpeechConfig(subscription=SPEECH_SERVICE_KEY, region=REGION)
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        speech_config.speech_synthesis_voice_name = 'en-US-AvaMultilingualNeural'
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        speech_synthesizer.speak_text_async(text).get()
        return f"Speech synthesized for text: {text}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"