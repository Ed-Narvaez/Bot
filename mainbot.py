from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from models import User
POSTGRES = {
'user': 'root',
'pw': 'root',
'db': 'usuarios',
'host': '127.0.0.1',
'port': '5432',
}
app = Flask(__name__)
 
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.spanish")

app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager(app)
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    
    userText = request.args.get('msg')
    user = User(mensaje=userText)
    user.save()
    respuesta = User.get_by_mensaje(userText)
    return str(spanish_bot.get_response(userText))
 
 
if __name__ == "__main__":
    app.run()
