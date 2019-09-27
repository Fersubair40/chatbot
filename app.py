from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

app = Flask(__name__)
bot = ChatBot('bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
              trainer='chatterbot.trainers.ListTrainer')

# for files in os.listdir('./english/'):
#     data = open('./english/' + files, 'r').readlines()
trainer = ListTrainer(bot)
trainer.train(['What is your name?', 'My name is Candice'])
trainer.train(['Who are you?', 'I am a bot'])
trainer.train(['who created you?', 'Tony Stark', 'Sahil Rajput', 'You?'])
    # trainer.train(data)
print("Training completed")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()

# app = Flask(__name__)

# english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(english_bot.get_response(userText))


# if __name__ == "__main__":
#     app.run()