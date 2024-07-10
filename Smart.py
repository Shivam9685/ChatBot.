from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

bot = ChatBot("ChatBot", read_only=False, 
    logic_adapters=[
        {
            "import_path":"chatterbot.logic.BestMatch",
            "default_response":"Sorrt I don't have an answer",
            "maximum_similarity_threshold":0.9
        }
        ])

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

while True:
    user_response = input("User: ")
    print("Chatbot: "+ str(bot.get_response(user_response)))