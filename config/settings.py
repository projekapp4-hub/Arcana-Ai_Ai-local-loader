"""
Configuration settings untuk Phi-3 Chat App - Optimized untuk PyInstaller
"""

import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

class ModelConfig:
    """Configuration untuk model Phi-3 dengan GPU support"""
    def __init__(self):
        self.model_path = resource_path("model/Phi-3-mini-4k-instruct-q4.gguf")
        self.n_ctx = 4096  # Context penuh
        self.n_threads = max(1, os.cpu_count() - 1)
        self.n_batch = 512  # Optimal batch size
        self.n_gpu_layers = 20  # GPU layers untuk Intel UHD
        self.verbose = False
        self.use_mlock = False

class GenerationConfig:
    """Configuration untuk text generation yang optimal untuk Phi-3 3B"""
    def __init__(self):
        # Length settings
        self.max_tokens = 2048  # Balanced length untuk 3B model
        self.min_tokens = 10   # Minimum tokens
        
        # Creativity settings
        self.temperature = 0.7    # Balanced creativity
        self.top_p = 0.9          # Nucleus sampling
        self.top_k = 40           # Top-k sampling
        
        # Quality control
        self.repeat_penalty = 1.1      # Kurangi repetisi
        self.frequency_penalty = 0.0   
        self.presence_penalty = 0.0    
        
        # Stop conditions
        self.stop_tokens = ["<|end|>", "\n\nUser:", "\n\nHuman:", "###"]
        self.stop_sequences = []  
        
        # Generation mode
        self.stream = False       # Non-streaming untuk stability
        self.echo = False         
        
        # Performance
        self.seed = -1           
        
    def get_generation_kwargs(self):
        """Return kwargs untuk llama.cpp generation"""
        return {
            'max_tokens': self.max_tokens,
            'temperature': self.temperature,
            'top_p': self.top_p,
            'top_k': self.top_k,
            'repeat_penalty': self.repeat_penalty,
            'frequency_penalty': self.frequency_penalty,
            'presence_penalty': self.presence_penalty,
            'stop': self.stop_tokens,
            'stream': self.stream,
            'echo': self.echo,
            'seed': self.seed
        }
    
    def set_creative_mode(self):
        """Set parameters untuk mode kreatif"""
        self.temperature = 0.8
        self.top_p = 0.95
        self.top_k = 50
        self.max_tokens = 768
        
    def set_precise_mode(self):
        """Set parameters untuk mode presisi"""
        self.temperature = 0.3
        self.top_p = 0.8
        self.top_k = 20
        self.max_tokens = 384
        
    def set_balanced_mode(self):
        """Set parameters untuk mode balanced (default)"""
        self.temperature = 0.7
        self.top_p = 0.9
        self.top_k = 40
        self.max_tokens = 512
        
    def validate_settings(self):
        """Validate generation settings"""
        assert 0.1 <= self.temperature <= 2.0, "Temperature harus antara 0.1 dan 2.0"
        assert 0.1 <= self.top_p <= 1.0, "Top_p harus antara 0.1 dan 1.0"
        assert self.max_tokens > 0, "Max tokens harus positif"
        assert self.repeat_penalty >= 1.0, "Repeat penalty harus >= 1.0"
        
    def __str__(self):
        """String representation untuk debugging"""
        return f"""GenerationConfig:
  Max Tokens: {self.max_tokens}
  Temperature: {self.temperature}
  Top-p: {self.top_p}
  Top-k: {self.top_k}
  Repeat Penalty: {self.repeat_penalty}
  Stream: {self.stream}
  Stop Tokens: {self.stop_tokens}
"""

class AppConfig:
    """Configuration untuk aplikasi"""
    def __init__(self):
        self.window_title = "Arcana AI"
        self.window_size = "1000x700"
        self.theme = "dark"
        self.language = "indonesia"
        self.mode = "coding"