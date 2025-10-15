import customtkinter as ctk
import json
import os
import sys
import threading
from datetime import datetime
from llama_cpp import Llama

# Import config modules
from config.settings import ModelConfig, GenerationConfig, AppConfig
from config.prompts import get_system_prompt, get_chat_prompt, PRESET_CONFIGS

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Custom Purple Magical Theme
class MagicalTheme:
    DARK_BG = "#0A0A0A"
    CARD_BG = "#1A1A1A" 
    ACCENT_PURPLE = "#8B5FBF"
    LIGHT_PURPLE = "#9D71E8"
    TEXT_PRIMARY = "#E2E2E2"
    TEXT_SECONDARY = "#B0B0B0"
    HOVER_PURPLE = "#7A4BA8"

class Phi3ChatApp:
    def __init__(self):
        # Load configurations
        self.model_config = ModelConfig()
        self.gen_config = GenerationConfig()
        self.app_config = AppConfig()
        
        # Setup custom theme
        self.setup_custom_theme()
        
        # Setup window
        self.window = ctk.CTk()
        self.window.title(self.app_config.window_title)
        self.window.geometry(self.app_config.window_size)
        self.window.configure(fg_color=MagicalTheme.DARK_BG)
        
        # Set window icon
        try:
            icon_path = resource_path("assets/logo.ico")
            self.window.iconbitmap(icon_path)
        except Exception as e:
            print(f"⚠️ Could not load icon: {e}")
        
        # Application state
        self.llm = None
        self.chat_history = []
        self.is_loading = False
        self.is_generating = False
        self.current_system_prompt = get_system_prompt(
            self.app_config.language, 
            self.app_config.mode
        )
        
        self.load_history()
        self.setup_ui()
        self.load_model_async()
    
    def setup_custom_theme(self):
        """Setup custom magical purple theme"""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
    
    def load_model_async(self):
        """Load model di thread terpisah"""
        def load():
            self.is_loading = True
            self.update_status("🔮 Loading magical model...")
            
            try:
                self.llm = Llama(
                    model_path=self.model_config.model_path,
                    n_ctx=self.model_config.n_ctx,
                    n_threads=self.model_config.n_threads,
                    n_batch=self.model_config.n_batch,
                    n_gpu_layers=self.model_config.n_gpu_layers,
                    verbose=False
                )
                self.update_status("✨ Model ready! Let's chat...")
                print("🎉 Model loaded successfully!")
                
            except Exception as e:
                self.update_status(f"❌ Error: {str(e)}")
                print(f"❌ Error loading model: {e}")
            
            self.is_loading = False
        
        thread = threading.Thread(target=load)
        thread.daemon = True
        thread.start()
    
    def update_status(self, message):
        """Update status di UI"""
        def update():
            if hasattr(self, 'status_label'):
                self.status_label.configure(text=message)
        self.window.after(0, update)
    
    def load_history(self):
        """Load chat history"""
        try:
            history_file = resource_path("chat_history.json")
            if os.path.exists(history_file):
                with open(history_file, "r", encoding="utf-8") as f:
                    self.chat_history = json.load(f)
        except Exception as e:
            print(f"Error loading history: {e}")
            self.chat_history = []
    
    def save_history(self):
        """Save chat history"""
        try:
            history_file = resource_path("chat_history.json")
            with open(history_file, "w", encoding="utf-8") as f:
                json.dump(self.chat_history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving history: {e}")
    
    def setup_ui(self):
        """Setup user interface dengan theme magical"""
        # Main container
        self.main_frame = ctk.CTkFrame(self.window, fg_color=MagicalTheme.DARK_BG)
        self.main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Sidebar dengan glassmorphism effect
        self.sidebar = ctk.CTkFrame(self.main_frame, width=280, 
                                  fg_color=MagicalTheme.CARD_BG,
                                  corner_radius=15)
        self.sidebar.pack(side="left", fill="y", padx=(0, 15))
        
        # App Title dengan style magical
        title_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        title_frame.pack(pady=15, padx=15, fill="x")
        
        app_title = ctk.CTkLabel(title_frame, text="ARCANA AI", 
                               font=ctk.CTkFont(size=20, weight="bold"),
                               text_color=MagicalTheme.LIGHT_PURPLE)
        app_title.pack()
        
        app_subtitle = ctk.CTkLabel(title_frame, text="ARCANA AI", 
                                  font=ctk.CTkFont(size=12),
                                  text_color=MagicalTheme.TEXT_SECONDARY)
        app_subtitle.pack()
        
        # Status dengan icon magical
        self.status_label = ctk.CTkLabel(self.sidebar, text="Initializing...",
                                       text_color=MagicalTheme.LIGHT_PURPLE,
                                       font=ctk.CTkFont(size=11))
        self.status_label.pack(pady=10)
        
        # Prompt Settings Section
        settings_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        settings_frame.pack(pady=10, padx=15, fill="x")
        
        settings_title = ctk.CTkLabel(settings_frame, text="🔮 SPELL SETTINGS",
                                    font=ctk.CTkFont(size=14, weight="bold"),
                                    text_color=MagicalTheme.TEXT_PRIMARY)
        settings_title.pack(anchor="w", pady=(0, 10))
        
        # Language selection
        lang_label = ctk.CTkLabel(settings_frame, text="Language:",
                                text_color=MagicalTheme.TEXT_SECONDARY)
        lang_label.pack(anchor="w", pady=(5, 0))
        
        self.lang_var = ctk.StringVar(value=self.app_config.language)
        lang_combo = ctk.CTkComboBox(settings_frame, 
                                   values=["indonesia", "english"],
                                   variable=self.lang_var,
                                   command=self.update_prompt_settings,
                                   fg_color=MagicalTheme.CARD_BG,
                                   button_color=MagicalTheme.ACCENT_PURPLE,
                                   border_color=MagicalTheme.ACCENT_PURPLE)
        lang_combo.pack(fill="x", pady=2)
        
        # Mode selection
        mode_label = ctk.CTkLabel(settings_frame, text="Mode:",
                                text_color=MagicalTheme.TEXT_SECONDARY)
        mode_label.pack(anchor="w", pady=(10, 0))
        
        self.mode_var = ctk.StringVar(value=self.app_config.mode)
        mode_combo = ctk.CTkComboBox(settings_frame,
                                   values=["coding", "general"],
                                   variable=self.mode_var,
                                   command=self.update_prompt_settings,
                                   fg_color=MagicalTheme.CARD_BG,
                                   button_color=MagicalTheme.ACCENT_PURPLE,
                                   border_color=MagicalTheme.ACCENT_PURPLE)
        mode_combo.pack(fill="x", pady=2)
        
        # Quick Presets dengan style card
        presets_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        presets_frame.pack(pady=15, padx=15, fill="x")
        
        presets_title = ctk.CTkLabel(presets_frame, text="⚡ QUICK PRESETS",
                                   font=ctk.CTkFont(weight="bold"),
                                   text_color=MagicalTheme.TEXT_PRIMARY)
        presets_title.pack(anchor="w", pady=(0, 8))
        
        # Preset buttons dengan style magical
        for preset_id, preset_config in PRESET_CONFIGS.items():
            btn = ctk.CTkButton(
                presets_frame,
                text=preset_config["description"],
                command=lambda pid=preset_id: self.apply_preset(pid),
                height=35,
                fg_color=MagicalTheme.ACCENT_PURPLE,
                hover_color=MagicalTheme.HOVER_PURPLE,
                text_color=MagicalTheme.TEXT_PRIMARY,
                corner_radius=8
            )
            btn.pack(fill="x", pady=3)
        
        # Current settings info
        self.settings_info = ctk.CTkLabel(self.sidebar, 
                                        text=f"✨ {self.app_config.mode.title()} Mode\n🔤 {self.app_config.language.title()}",
                                        font=ctk.CTkFont(size=11),
                                        text_color=MagicalTheme.TEXT_SECONDARY)
        self.settings_info.pack(pady=15, padx=15)
        
        # History section
        history_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        history_frame.pack(pady=10, padx=15, fill="both", expand=True)
        
        history_title = ctk.CTkLabel(history_frame, text="📜 CHAT HISTORY",
                                   font=ctk.CTkFont(size=14, weight="bold"),
                                   text_color=MagicalTheme.TEXT_PRIMARY)
        history_title.pack(anchor="w", pady=(0, 8))
        
        self.history_frame = ctk.CTkScrollableFrame(history_frame, 
                                                  fg_color=MagicalTheme.CARD_BG)
        self.history_frame.pack(fill="both", expand=True)
        
        # Action buttons
        action_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        action_frame.pack(pady=15, padx=15, fill="x")
        
        clear_btn = ctk.CTkButton(action_frame, text="🧹 Clear History", 
                                command=self.clear_history,
                                fg_color=MagicalTheme.ACCENT_PURPLE,
                                hover_color=MagicalTheme.HOVER_PURPLE)
        clear_btn.pack(fill="x", pady=3)
        
        about_btn = ctk.CTkButton(action_frame, text="ℹ️ About", 
                                command=self.show_about,
                                fg_color=MagicalTheme.ACCENT_PURPLE,
                                hover_color=MagicalTheme.HOVER_PURPLE)
        about_btn.pack(fill="x", pady=3)
        
        # Main chat area dengan glass effect
        self.chat_frame = ctk.CTkFrame(self.main_frame, 
                                     fg_color=MagicalTheme.CARD_BG,
                                     corner_radius=15)
        self.chat_frame.pack(side="right", fill="both", expand=True)
        
        # Chat display area dengan style modern
        self.chat_display = ctk.CTkTextbox(self.chat_frame, wrap="word", 
                                         font=ctk.CTkFont(family="Segoe UI", size=13),
                                         fg_color="#0F0F0F",
                                         text_color="#E8E8E8",
                                         border_width=0,
                                         corner_radius=10)
        self.chat_display.pack(fill="both", expand=True, padx=15, pady=15)
        self.chat_display.configure(state="disabled")
        
        # Input area dengan style magical
        self.input_frame = ctk.CTkFrame(self.chat_frame, 
                                      fg_color="transparent")
        self.input_frame.pack(fill="x", padx=15, pady=15)
        
        self.user_input = ctk.CTkEntry(self.input_frame, 
                                     placeholder_text="🔮 Cast your message here...",
                                     fg_color=MagicalTheme.CARD_BG,
                                     border_color=MagicalTheme.ACCENT_PURPLE,
                                     text_color=MagicalTheme.TEXT_PRIMARY,
                                     height=40,
                                     corner_radius=10)
        self.user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", lambda e: self.send_message())
        
        self.send_btn = ctk.CTkButton(self.input_frame, text="✨ Send", 
                                    command=self.send_message,
                                    fg_color=MagicalTheme.ACCENT_PURPLE,
                                    hover_color=MagicalTheme.HOVER_PURPLE,
                                    height=40,
                                    width=80,
                                    corner_radius=10)
        self.send_btn.pack(side="right")
        
        self.update_history_display()
    
    def update_prompt_settings(self, *args):
        """Update prompt settings"""
        self.app_config.language = self.lang_var.get()
        self.app_config.mode = self.mode_var.get()
        
        self.current_system_prompt = get_system_prompt(
            self.app_config.language,
            self.app_config.mode
        )
        
        self.settings_info.configure(
            text=f"✨ {self.app_config.mode.title()} Mode\n🔤 {self.app_config.language.title()}"
        )
    
    def apply_preset(self, preset_id):
        """Apply preset configuration"""
        if preset_id in PRESET_CONFIGS:
            preset = PRESET_CONFIGS[preset_id]
            self.lang_var.set(preset["language"])
            self.mode_var.set(preset["mode"])
            self.update_prompt_settings()
    
    def show_about(self):
        """Show about information"""
        about_text = """
ARCANA AI was developed by Al Musawiru.

Version: 1.0
Model: Phi-3-mini-4k-instruct-q4
Context: 4K tokens
Quantization: Q4_0

Features:
• Non-streaming responses (Stable)
• Dark purple magical theme
• Multiple language support (ID/EN)
• Coding & general modes
• Chat history management

Built with:
• Python + CustomTkinter
• llama-cpp-python
• Phi-3 model by Microsoft

Thank you for using
"""
        
        dialog = ctk.CTkToplevel(self.window)
        dialog.title("About ARCANA AI")
        dialog.geometry("400x450")
        dialog.transient(self.window)
        dialog.grab_set()
        
        textbox = ctk.CTkTextbox(dialog, wrap="word")
        textbox.pack(fill="both", expand=True, padx=20, pady=20)
        textbox.insert("1.0", about_text)
        textbox.configure(state="disabled")
        
        close_btn = ctk.CTkButton(dialog, text="Close", command=dialog.destroy)
        close_btn.pack(pady=10)
    
    def update_history_display(self):
        """Update history sidebar dengan style magical"""
        for widget in self.history_frame.winfo_children():
            widget.destroy()
        
        for i, chat in enumerate(self.chat_history):
            preview = chat.get('user_message', '')[:25] + "..." if len(chat.get('user_message', '')) > 25 else chat.get('user_message', '')
            timestamp = chat.get('timestamp', '')[:16]
            
            history_btn = ctk.CTkButton(
                self.history_frame, 
                text=f"📄 {timestamp}\n{preview}",
                command=lambda idx=i: self.load_chat(idx),
                height=50,
                anchor="w",
                fg_color=MagicalTheme.CARD_BG,
                hover_color=MagicalTheme.HOVER_PURPLE,
                text_color=MagicalTheme.TEXT_SECONDARY,
                corner_radius=8
            )
            history_btn.pack(fill="x", pady=2, padx=5)
    
    def send_message(self):
        """Send message dengan non-streaming response"""
        if self.is_loading or not self.llm:
            self.show_temp_message("🔮 Model is still loading magic...")
            return
            
        user_text = self.user_input.get().strip()
        if not user_text:
            return
        
        if self.is_generating:
            self.show_temp_message("⏳ Still generating previous message...")
            return
        
        # Disable input selama processing
        self.user_input.configure(state="disabled")
        self.send_btn.configure(state="disabled")
        
        # Add user message
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"👤 You: {user_text}\n\n")
        self.chat_display.see("end")
        
        # Show thinking indicator
        self.chat_display.insert("end", "🤖 Arcana: Thinking...")
        self.chat_display.see("end")
        self.window.update()
        
        # Format prompt
        formatted_prompt = get_chat_prompt(
            self.current_system_prompt, 
            user_text, 
            self.chat_history
        )
        
        def generate_response():
            try:
                # NON-STREAMING response
                response = self.llm(
                    formatted_prompt,
                    max_tokens=self.gen_config.max_tokens,
                    temperature=self.gen_config.temperature,
                    top_p=self.gen_config.top_p,
                    stop=self.gen_config.stop_tokens,
                    stream=False
                )
                
                ai_response = response['choices'][0]['text'].strip()
                self.window.after(0, lambda: self.finalize_response(user_text, ai_response, None))
                
            except Exception as e:
                error_msg = str(e)
                self.window.after(0, lambda: self.finalize_response(user_text, None, error_msg))
        
        thread = threading.Thread(target=generate_response)
        thread.daemon = True
        thread.start()
    
    def finalize_response(self, user_text, ai_response, error):
        """Finalize non-streaming response"""
        self.is_generating = False
        
        self.chat_display.configure(state="normal")
        
        # Hapus "Thinking..." text
        self.chat_display.delete("end-1l", "end")
        
        if error:
            self.chat_display.insert("end", f"🤖 Arcana: ❌ Error: {error}\n\n")
        else:
            self.chat_display.insert("end", f"🤖 Arcana: {ai_response}\n\n")
            
            # Save ke history
            chat_entry = {
                'timestamp': datetime.now().isoformat(),
                'user_message': user_text,
                'ai_response': ai_response,
                'settings': {
                    'language': self.app_config.language,
                    'mode': self.app_config.mode
                }
            }
            self.chat_history.append(chat_entry)
            self.save_history()
            self.update_history_display()
        
        self.chat_display.see("end")
        self.chat_display.configure(state="disabled")
        
        # Re-enable input
        self.user_input.configure(state="normal")
        self.send_btn.configure(state="normal")
        self.user_input.focus()
        self.user_input.delete(0, "end")
    
    def show_temp_message(self, message):
        """Tampilkan temporary message"""
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", f"💡 {message}\n\n")
        self.chat_display.see("end")
        self.chat_display.configure(state="disabled")
    
    def load_chat(self, index):
        """Load chat dari history"""
        if 0 <= index < len(self.chat_history):
            chat = self.chat_history[index]
            
            self.chat_display.configure(state="normal")
            self.chat_display.delete("1.0", "end")
            
            self.chat_display.insert("end", f"👤 You: {chat['user_message']}\n\n")
            self.chat_display.insert("end", f"🤖 Arcana: {chat['ai_response']}\n\n")
            
            self.chat_display.configure(state="disabled")
            self.chat_display.see("end")
    
    def clear_history(self):
        """Clear chat history"""
        self.chat_history = []
        self.save_history()
        self.update_history_display()
        
        self.chat_display.configure(state="normal")
        self.chat_display.delete("1.0", "end")
        self.chat_display.configure(state="disabled")
    
    def run(self):
        """Run aplikasi"""
        self.window.mainloop()

if __name__ == "__main__":
    app = Phi3ChatApp()
    app.run()