from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Analista de Dados',
    'localidade': 'SC, Brail',
    'salario': 'R$ 5.000'
}, {
    'id': 2,
    'titulo': 'Desenvolvedor Frontend',
    'localidade': 'PR, Brail',
    'salario': 'R$ 3.000'
}, {
    'id': 3,
    'titulo': 'Cientista de dados',
    'localidade': 'SP, Brail',
    'salario': 'R$ 4.000'
}, {
    'id': 4,
    'titulo': 'Desenvolvedor Backend',
    'localidade': 'SP, Brail',
    'salario': 'R$ 5.000'
}, {
    'id': 5,
    'titulo': 'Estatístico',
    'localidade': 'RJ, Brail',
    'salario': 'R$ 3.400'
}]


@app.route("/")
def hello():
  return render_template("home.html", vagas=VAGAS)
  
@app.route("/vagas")
def lista_vagas():
  return jsonify(VAGAS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
