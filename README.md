## 🗣️ Advanced Voice Assistant


This project is an advanced, customizable voice assistant built primarily in Python, designed to demonstrate sophisticated integration of **Speech Recognition (STT)**, **Natural Language Understanding (NLU)**, and **Task Automation** via external APIs.

The assistant is capable of handling general knowledge queries, controlling local smart devices, and interacting with web services like email and weather providers.

### Key Features

  * **Speech Recognition:** Converts spoken commands into text using Google's Speech-to-Text service.
  * **Natural Language Processing (Simplified):** Uses Regular Expressions (`re`) for basic intent classification and entity extraction.
  * **Text-to-Speech (TTS):** Provides verbal feedback using the `pyttsx3` library.
  * **Task Automation:** Integrates with local files and simulated external APIs for email, weather, and smart home control.
  * **Modular Design:** Separates core logic (`Assistant.py`) from service integrations (`services/`).

-----

## 🛠️ Prerequisites

Before running the assistant, ensure you have the following installed:

1.  **Python 3.x**
2.  **PortAudio:** Required system-level dependency for `PyAudio` to access your microphone.
      * **Linux (Debian/Ubuntu):** `sudo apt-get install portaudio19-dev`
      * **macOS (Homebrew):** `brew install portaudio`

-----

## ⚙️ Setup and Installation

### 1\. Clone the Repository

```bash
git clone https://github.com/anmolingle/OIBSIP_Python_Task1.git
cd OIBSIP_Python_Task1
```

### 2\. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment.

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3\. Install Dependencies

Install all required libraries using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4\. Configuration (API Keys)

You must configure your API keys and credentials in the **`config.py`** file for the advanced services to work. **Do not commit sensitive keys to GitHub.**

| Variable | Service | Purpose |
| :--- | :--- | :--- |
| `WEATHER_API_KEY` | OpenWeatherMap | Fetching weather data. |
| `MY_EMAIL`, `MY_PASSWORD` | SMTP/Gmail | Credentials for sending emails (use an App Password\!). |
| `MQTT_BROKER`, `MQTT_PORT` | Smart Home (MQTT) | Address for your local smart home hub. |

-----

## 🚀 How to Run the Assistant

1.  Ensure your virtual environment is active (`(venv)` appears in your terminal prompt).

2.  Run the main script:

    ```bash
    python Assistant.py
    ```

3.  Wait for the assistant to say, "**System Ready. How may I help you?**" The terminal will then show "**Listening...**"

-----

## 🎤 Available Voice Commands

The assistant uses keyword matching and basic Regular Expressions to identify intents.

| Category | Example Command | Implementation |
| :--- | :--- | :--- |
| **General** | "What is the time?" | Python `datetime` |
| **Knowledge** | "Wikipedia search for **Apollo 11**" | `wikipedia` library |
| **Web** | "Open **YouTube**" | `webbrowser` |
| **Weather** | "Check the weather in **London**" | `services/weather_handler.py` (Requires API Key) |
| **Email** | "Send email to **John** subject **Report** body **Check the Q4 figures**" | `services/email_handler.py` (Requires SMTP config) |
| **Smart Home**| "Turn on the **living room lights**" | `services/smart_home.py` (Requires MQTT setup) |
| **Exit** | "Goodbye" or "Stop" | Exits the loop. |

-----

## 📂 Project Structure

```
OIBSIP_Python_Task1/
├── Assistant.py                # Main execution script (STT, TTS, Command Router)
├── config.py                   # Secure location for API keys and credentials (DO NOT COMMIT FILLED-OUT VERSION)
├── requirements.txt            # List of Python dependencies
└── services/
    ├── email_handler.py        # Handles SMTP communication and calendar reminder placeholders
    ├── weather_handler.py      # Handles HTTP requests to the Weather API
    └── smart_home.py           # Handles MQTT communication for device control
```

-----

## 🧠 Future Enhancements (Advanced NLU)

The current version uses simple string matching. For true natural language processing, consider integrating the following:

1.  **Rasa Framework:** Replace the RegEx-based intent matching with a full NLU model for better conversational flow.
      * **Required Libraries:** `rasa`
2.  **Official Google API:** Use the `google-api-python-client` and `google-auth-oauthlib` for secure, full OAuth access to user data for advanced calendar and email functionality.

-----

## 🤝 Contributing

Contributions are welcome\! Feel free to open issues or submit pull requests for improvements, especially to the NLU or service handlers.

-----

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
