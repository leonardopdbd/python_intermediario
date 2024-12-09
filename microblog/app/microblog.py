from flask import Flask, render_template

# Função para criar a aplicação
def create_app():
    app = Flask(__name__)

    # Rota principal
    @app.route('/')
    def index():
        return render_template('index.html')

    return app

# Cria o app e inicia o servidor
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
