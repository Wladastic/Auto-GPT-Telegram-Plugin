import torch
import torchaudio
from typing import Tuple
from torchaudio.sox_effects import apply_effects_tensor


class SileroTTS:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model, self.symbols, self.sample_rate, self.example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                                       model='silero_tts',
                                                                                       language='en',
                                                                                       device=self.device)
        self.effects = [["reverb", 50, 50, 100]]

    def text_to_speech(self, text: str) -> Tuple[torch.Tensor, int]:
        input_text = torch.LongTensor([self.symbols.index(ch) for ch in text]).unsqueeze(0).to(self.device)
        with torch.no_grad():
            waveform, *_ = self.model(input_text)
        waveform, sample_rate = apply_effects_tensor(waveform.cpu(), self.sample_rate, self.effects)
        return waveform, sample_rate