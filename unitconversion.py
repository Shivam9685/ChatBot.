from chatterbot import ChatBot

bot= ChatBot("Unit Conversion",logic_adapters=['chatterbot.logic.UnitConversion']) 

while True:
    user_text = input("Ask a question (Unit Convesion): ")
    print(str(bot.get_response(user_text)))