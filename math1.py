from chatterbot import ChatBot


bot = ChatBot("Math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("------Math ChatBot--------")

while True:
    user_text = input("Type te math equatiion that you want to solve: ")
    print("ChatBot: " + str(bot.get_response(user_text)))
