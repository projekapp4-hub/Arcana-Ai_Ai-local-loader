"""
System prompts untuk Phi-3 Chat App - Balanced for 3B Model
"""

def get_system_prompt(language="indonesia", mode="coding"):
    """
    Return system prompt yang balanced untuk model 3B
    """
    
    base_prompts = {
        "indonesia": {
            "coding": """<|system|>
Anda asisten AI bernama Arcana untuk pemrograman.
ATURAN dalam menjawab pertanyaan:
1. Jawab dengan PENJELASAN yang JELAS dan LENGKAP
2. Berikan contoh kode yang praktis dan bekerja
3. Jelaskan konsep dengan bahasa yang mudah dimengerti
4. Struktur jawaban dengan rapi
5. Gunakan bahasa Indonesia yang baik
6. Hindari jawaban terlalu pendek atau terlalu panjang

FORMAT JAWABAN:
- Penjelasan konsep singkat
- Contoh kode yang relevan
- Penjelasan cara penggunaan
- Tips atau best practice jika diperlukan
- jawab dalam bentuk narasi, bukan per point
<|end|>
""",
            "general": """<|system|>
Anda asisten AI bernama Arcana untuk membantu menjawab pertanyaan hal umum.
ATURAN dalam menjawab pertanyaan:
1. Berikan jawaban yang INFORMATIF dan LENGKAP
2. Jelaskan dengan bahasa Indonesia yang jelas
3. Gunakan contoh yang relevan jika diperlukan
4. Struktur jawaban dengan logika yang baik
5. Jawab dengan depth yang cukup untuk memahami topik

FORMAT JAWABAN:
- Jawaban inti yang jelas
- jawab dalam bentuk narasi, bukan per point
<|end|>
"""
        },
        "english": {
            "coding": """<|system|>
You are an AI assistant named Arcana for programming..
RULES for answering questions:
1. Provide CLEAR and COMPLETE explanations
2. Give practical working code examples
3. Explain concepts in easy-to-understand language
4. Structure answers neatly
5. Use proper English
6. Avoid answers that are too short or too long

ANSWER FORMAT:
- Brief concept explanation
- Relevant code example
- Usage explanation
- Tips or best practices if needed
- Write it as a narrative, not as bullet points.
<|end|>
""",
            "general": """<|system|>
You have an AI assistant named Arcana to help answer general questions.
RULES for answering questions:
1. Give INFORMATIVE and COMPLETE answers
2. Explain with clear English
3. Use relevant examples when needed
4. Structure answers with good logic
5. Provide sufficient depth for topic understanding
6. Don't talk about programming too often.

ANSWER FORMAT:
- Clear core answer
- Write it as a narrative, not as bullet points.
<|end|>
"""
        }
    }
    
    lang = language if language in base_prompts else "indonesia"
    mod = mode if mode in base_prompts[lang] else "general"
    
    return base_prompts[lang][mod]


def get_chat_prompt(system_prompt, user_message, chat_history=None):
    """
    Format prompt untuk chat dengan context management yang balanced
    """
    context = ""
    if chat_history and len(chat_history) > 0:
        # Balanced context - cukup untuk continuity tapi tidak overload
        recent_history = chat_history[-3:]  # 3 pesan terakhir untuk context yang baik
        for chat in recent_history:
            # Biarkan context lebih panjang untuk jawaban yang lengkap
            user_msg = chat['user_message'][:150]  # Max 150 chars
            ai_resp = chat['ai_response'][:200]    # Max 200 chars
            
            context += f"<|user|>\n{user_msg}<|end|>\n"
            context += f"<|assistant|>\n{ai_resp}<|end|>\n"
    
    return f"{system_prompt}{context}<|user|>\n{user_message}<|end|>\n<|assistant|>\n"


def get_debug_info():
    """Info untuk debugging prompt settings"""
    return {
        "model_size": "3B",
        "optimization": "balanced_length",
        "max_history": 3,
        "response_style": "clear_complete_explanations",
        "focus": "informative_structured_answers"
    }


# Preset configurations
PRESET_CONFIGS = {
    "indonesia_coding": {
        "language": "indonesia",
        "mode": "coding",
        "description": "ID + Coding",
        "note": "Penjelasan lengkap dengan contoh kode"
    },
    "indonesia_general": {
        "language": "indonesia", 
        "mode": "general",
        "description": "ID + General",
        "note": "Jawaban informatif dan mudah dipahami"
    },
    "english_coding": {
        "language": "english",
        "mode": "coding", 
        "description": "EN + Coding",
        "note": "Complete explanations with code examples"
    },
    "english_general": {
        "language": "english",
        "mode": "general",
        "description": "EN + General", 
        "note": "Informative and well-structured answers"
    }
}


# Quick preset functions untuk akses mudah
def get_preset_config(preset_id):
    """Get preset configuration by ID"""
    return PRESET_CONFIGS.get(preset_id, PRESET_CONFIGS["indonesia_coding"])

def get_available_presets():
    """Get list of available preset IDs"""
    return list(PRESET_CONFIGS.keys())

def get_preset_display_info():
    """Get preset info untuk display di UI"""
    display_info = {}
    for preset_id, config in PRESET_CONFIGS.items():
        display_info[preset_id] = {
            "name": config["description"],
            "note": config.get("note", ""),
            "language": config["language"],
            "mode": config["mode"]
        }
    return display_info


if __name__ == "__main__":
    # Test prompts
    print("=== Prompt Tester ===")
    for lang in ["indonesia", "english"]:
        for mode in ["coding", "general"]:
            prompt = get_system_prompt(lang, mode)
            print(f"\n--- {lang}_{mode} ---")
            print(prompt[:250] + "..." if len(prompt) > 250 else prompt)
    
    print(f"\n=== Debug Info ===")
    print(get_debug_info())