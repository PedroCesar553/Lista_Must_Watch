from flask import Flask, redirect, render_template, request, url_for
from models.database import init_db
from models.lista import Atividade

app = Flask(__name__)

# Inicializa o banco de dados ao iniciar o app
init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Bem-vindo')

@app.route('/lista', methods=['GET','POST'])
def atividade():
    if request.method == 'POST':
        # Captura os dados do formulário
        titulo_atividade = request.form['titulo-atividade']
        tipo_de_atividade = request.form['tipo_de_atividade']
        indicado_por = request.form.get('indicado_por', '') # .get evita erro se campo estiver vazio
    
        # Cria o objeto e salva
        atividade_obj = Atividade(titulo_atividade, tipo_de_atividade, indicado_por)
        atividade_obj.salvar_atividade()
        
        # Redireciona para limpar o formulário após postar
        return redirect(url_for('atividade'))

    # Busca a lista atualizada
    atividades = Atividade.obter_atividades()
    return render_template('lista.html', titulo='Sua Lista de Desejos', atividades=atividades)

@app.route('/delete/<int:idAtividade>')
def delete(idAtividade):
    atividade_obj = Atividade.id(idAtividade)
    atividade_obj.excluir_atividade()
    return redirect(url_for('atividade'))

@app.route('/update/<int:idAtividade>', methods=['GET', 'POST']) 
def update(idAtividade):
    if request.method == 'POST':
        # Captura os novos dados na edição
        titulo = request.form['titulo-atividade']
        tipo = request.form['tipo_de_atividade']
        indicado = request.form.get('indicado_por', '')
        
        # Cria objeto com o ID existente para atualizar
        atividade_obj = Atividade(titulo, tipo, indicado, idAtividade)
        atividade_obj.atualizar_atividade()
        
        return redirect(url_for('atividade'))

    # Para exibir a lista e o item selecionado ao mesmo tempo
    atividades = Atividade.obter_atividades()
    atividade_selecionada = Atividade.id(idAtividade)
    
    return render_template('lista.html', 
                           titulo='Editando Item', 
                           atividade_selecionada=atividade_selecionada, 
                           atividades=atividades)

if __name__ == "__main__":
    app.run(debug=True)