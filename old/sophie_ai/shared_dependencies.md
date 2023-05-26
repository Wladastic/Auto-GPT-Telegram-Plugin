the app is: Build an artificial general intelligence by building a ml core and giving it access to gpt if it needs to, as well as basic local commands like creating files, editing code or just specific lines of code, let it communicate with the user via telegram as well as silero tts and whisper stt. Make it able to improve itself.

the files we have decided to generate are: ml_core.py, gpt_integration.py, local_commands.py, telegram_communication.py, silero_tts.py, whisper_stt.py, self_improvement.py

Shared dependencies:

1. ml_core
   - MLCore class
   - train_model function
   - predict function

2. gpt_integration
   - GPTIntegration class
   - gpt_request function
   - gpt_response_parser function

3. local_commands
   - LocalCommands class
   - create_file function
   - edit_code function
   - edit_specific_line function

4. telegram_communication
   - TelegramCommunication class
   - send_message function
   - receive_message function

5. silero_tts
   - SileroTTS class
   - text_to_speech function

6. whisper_stt
   - WhisperSTT class
   - speech_to_text function

7. self_improvement
   - SelfImprovement class
   - analyze_performance function
   - update_model function