
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask,render_template

app = Flask(__name__)

bot=ChatBot("Smart", read_only=False, logic_adapters=["chatterbt.logic.BestMatch"])

list_to_train = ["hi","Hello","What's ap","Nothing","How are you","Good"]
list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)

@app.route("/")
def main():
    return render_template("index.html")

#user_response=input("User: ")
#print(bot.get_response(user_response))

if __name__== "__main__":
    app.run(debug=True)