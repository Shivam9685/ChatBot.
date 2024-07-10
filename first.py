import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Initialize ChatBot with the correct logic adapter
bot = ChatBot(
    "Smart", 
    read_only=False, 
    logic_adapters=["chatterbot.logic.BestMatch"],
    storage_adapter="chatterbot.storage.SQLStorageAdapter"
)

# List to train
list_to_train = ["hi", "Hello", "What's up", "Nothing", "How are you", "Good"]

# Train the chatbot
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

# Get user response and print chatbot response
user_response = input("User: ")
print(bot.get_response(user_response))
