
from flask import Flask
from flask import request
import pg8000.native
import logging

app = Flask(__name__)
log = logging.getLogger("werkzeug")
log.disabled = True


logging.basicConfig(level=logging.INFO, filename="app.log")
logger = logging.getLogger(__name__)


conn = pg8000.native.Connection("postgres", password="postgres")

def aluno_to_json(aluno) -> dict:
    return {
        "id": aluno[0],
        "nome": aluno[1],
        "idade": aluno[2],
        "nota": aluno[3]
    }

@app.route("/")
def hello_world():
    ip = request.remote_addr
    logger.info(f"IP: {ip} has made a GET to /")
    return "Hello, World!"


@app.route("/list/alunos")
def get_alunos(): 

    ip = request.remote_addr
    logger.info(f"IP: {ip} has made a GET to /list/alunos")
    return [aluno_to_json(aluno) for aluno in conn.run("SELECT * FROM alunos;")]



@app.route("/list/aluno/")
def get_aluno_id(): 
    id = request.args.get("id")

    ip = request.remote_addr
    logger.info(f"IP: {ip} has made a GET to /list/aluno?id={id}")
    return [aluno_to_json(a) for a in conn.run(f"SELECT * FROM alunos where id = {id}")]


