import speech_recognition as sr

class WhisperSTT:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speech_to_text(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio_data = self.recognizer.record(source)
        try:
            text = self.recognizer.recognize_sphinx(audio_data)
            return text
        except sr.UnknownValueError:
            return "WhisperSTT could not understand the audio"
        except sr.RequestError as e:
            return f"WhisperSTT error: {e}"