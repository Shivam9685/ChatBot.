from chatterbot import ChatBot
import spacy

# Load the small English model for spaCy
nlp = spacy.load("en_core_web_sm")

# Initialize ChatterBot with the loaded spaCy model
bot = ChatBot(
    "Math",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.MathematicalEvaluation"
        }
    ],
    tagger_language=nlp
)

print("------Math ChatBot--------")

while True:
    try:
        user_text = input("Type the math equation that you want to solve: ")
        bot_response = bot.get_response(user_text)
        print("ChatBot: " + str(bot_response))
    except (KeyboardInterrupt, EOFError):
        break
    except Exception as e:
        print(f"An error occurred: {str(e)}")
