import asyncio
from ml_core import MLCore
from gpt_integration import GPTIntegration
from local_commands import LocalCommands
from telegram_communication import TelegramCommunication
from silero_tts import SileroTTS
from whisper_stt import WhisperSTT
from self_improvement import SelfImprovement
import config

async def main():
    ml_core = MLCore(".")
    gpt_integration = GPTIntegration()
    local_commands = LocalCommands()
    telegram_communication = TelegramCommunication(config.TELEGRAM_API_KEY)
    silero_tts = SileroTTS()
    whisper_stt = WhisperSTT()
    self_improvement = SelfImprovement()

    while True:
        message = await telegram_communication.receive_message()
        text_input = whisper_stt.speech_to_text(message.audio)

        if "gpt" in text_input:
            gpt_result = gpt_integration.gpt_request(text_input)
            response = gpt_integration.gpt_response_parser(gpt_result)
        else:
            response = ml_core.predict(text_input)

        if "local command" in response:
            local_commands.execute(response)

        if "self-improvement" in response:
            self_improvement.analyze_performance(response)
            self_improvement.update_model(ml_core)

        audio_output = silero_tts.text_to_speech(response)
        await telegram_communication.send_message(audio_output)

if __name__ == "__main__":
    asyncio.run(main())