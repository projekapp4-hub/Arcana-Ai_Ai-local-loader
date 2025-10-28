# Arcana-Ai_Ai-local-loader

[Indonesian version](README_id.md)

Welcome to **Arcana-Ai**! A simple AI Loader application that allows you to load and interact with AI models (GGUF) locally on your computer.

This application is built entirely in Python, using `customtkinter` for a modern user interface (GUI) and `llama-cpp-python` for fast and efficient AI inference on the CPU (or GPU if supported).

---

## ✨ Features

* **Modern Interface:** A clean and responsive GUI built with `customtkinter`.
* **Local & Private:** All AI processing runs 100% on your machine. No data is sent to external servers.
* **High Performance:** Powered by `llama-cpp-python`, optimized for LLM model inference.
* **Easy to Use:** Simply download the GGUF model, load it into the app, and start interacting.

---

## 🛠️ Installation

To run this app, you need Python 3.10+ and some C++ build tools.

### 1. Prerequisite: C++ Build Tools (Required)

`llama-cpp-python` needs to compile (build) some parts of the source code. On Windows, this requires C++ build tools from Visual Studio.

1.  Visit the [Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/) page.
2.  Download **Build Tools for Visual Studio**. (You can also use the “Visual Studio Community” installer, but Build Tools is lighter if you don't need the full IDE).
3. Run the installer.
4. In the “Workloads” tab, check **“Desktop development with C++”**.

5. Click “Install” and wait for the process to complete.

### 2. Project Installation

Once the prerequisites are met, follow these steps:

1.  **Clone this repository:**
```bash
    git clone [https://github.com/(USERNAME)/(REPO_NAME).git](https://github.com/(USERNAME)/(REPO_NAME).git)
    cd (REPO_NAME)
   ```

2.  **Create a Virtual Environment (Highly recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * On Windows (CMD/PowerShell):
        ```bash
        .\venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install all dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(This will automatically install `customtkinter` and `llama-cpp-python`. The installation process for `llama-cpp-python` may take several minutes as it requires compilation).*

---

## 🚀 Usage

1.  Ensure your virtual environment is active (see installation steps).
2.  Run the application:
    ```bash
    python main.py
    ```

3.  **Get the Model:**
    This application is designed to load models in **GGUF** format. You can download compatible GGUF models (e.g., Llama 3, Mistral, etc.) from [Hugging Face](https://huggingface.co/models?search=gguf).

4.  Within the application, use the “Load Model” button (or similar) to select the `.gguf` file you downloaded.

---

## 🤝 Contributions

We greatly appreciate your contributions! If you find a bug or want to add a new feature, please follow these steps:

1.  **Fork** this repository.
2. Create a new branch (`git checkout -b fitur/FiturKeren`).
3. Ensure you have followed the **Installation Steps** above correctly, especially the **C++ Build Tools Prerequisites** section, as this is crucial for development.
4. Make your changes and commit them (`git commit -m ‘Adding FiturKeren’`).
5.  Push to your branch (`git push origin feature/CoolFeature`).
6.  Open a **Pull Request**.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
