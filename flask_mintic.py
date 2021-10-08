from files import utils, comments

from flask import Flask
from flask import render_template, url_for,redirect,request,flash, redirect
import random


import os

app = Flask(__name__)

app.secret_key = os.urandom(24)




@app.route('/')
def hello():
    return redirect(url_for('home'))

# HOME

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/inicio',methods=['GET','POST'])
def inicio():
    return render_template('Principal.html')

# REGISTRO

@app.route('/registro',methods=['GET','POST'])
def registro():

    #Get data from register form
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

    #validate username, password and email
    #pip install validate_email
        if (not utils.isUsernameValid(username)):
            error = 'User must be alphanumeric'
            flash(error)
            return render_template('registro.html')

        elif(username=='' or username==None):
            error = 'Please enter username'
            flash(error)
            return render_template('registro.html')

        

        if not utils.isPasswordValid(password):
            error = "Invalid Password"
            flash(error)
            return render_template('registro.html')

        if not utils.isEmailValid(email):
            error = "Invalid Email"
            flash(error)
            return render_template('registro.html')
        if (utils.isUsernameValid(username) and utils.isPasswordValid(password) and 
            utils.isEmailValid(email)):

            flash('Check your email to activate your account')  
            return redirect('login')

    if(request.method == 'GET'):
        return render_template('registro.html')



# MENU

@app.route('/menu',methods=['GET'])
def menu():
    return render_template('menu.html')

@app.route('/menu/busqueda',methods=['GET','POST'])
def busqueda():
    return render_template('busqueda.html')

@app.route('/menu/lista_deseos',methods=['GET','POST','PUT'])
def lista_deseos():
    return 'lista_deseos'

@app.route('/menu/platos',methods=['GET','POST'])
def platos():
    return render_template('productos/Page-2.html')


#COMENTARIOS

@app.route('/comentarios',methods=['GET','POST'])
def comentarios():
    
    comentarios = comments.comentarios # folder: files, file: comments, list: 'comentarios'

    return render_template('comentarios/comments.html', comments= comentarios)

@app.route('/comentarios/insert', methods=['GET','POST'])
def insert_comment():
    comentarios = comments.comentarios

    if request.method == 'GET':
        return render_template('comentarios/insert_comment.html')

    if request.method == 'POST':
        id_comentario = str(random.randint(10,100))
        id_autor = str(random.randint(10,100))
        id_plato = str(random.randint(10,100))
        comentario = request.form['comentario']

        day = str(random.randint(1,31))
        month = str(random.randint(1,12))
        year = str(random.randint(2019,2021))
        fecha = day + '/' + month + '/' + year

        new_comment = comments.Comment(id_comentario,id_autor,id_plato, comentario, fecha)
        comentarios.append(new_comment)
        flash('Comment Added')
        return render_template('comentarios/comments.html', comments = comentarios)


@app.route('/comentarios/update',methods=['GET','POST'] )
def update_comment():
    
    
        flash('Comment Updated')
        return redirect(url_for('comentarios'))

@app.route('/comentarios/delete',methods=['GET','POST'] )
def delete_comment():
    

        flash('Comment Deleted')
        return redirect(url_for('comentarios'))



@app.route('/menu/pedidos',methods=['GET','POST','PUT'])
def pedidos():
    return 'pedidos'

#implementar busqueda por categoria, ej: tortas, pasteles, galletas
@app.route('/menu/busqueda/<string:categoria>',methods=['GET'])
def resultados(categoria):
    dict = {
        'galletas': ['galleta de coco', 'galleta de avena', 'galleta de chocolate'],
        'pan':['rollo','frances','mogollas'],
        'tortas':['mousse de chocolate','tarta de fresas','pie de manzana']
    }
    return f'Resultado de la busqueda por Categoria: {dict[categoria]}'

#implementar busqueda por id del plato
@app.route('/menu/busqueda/platos/<string:id_plato>',methods=['GET'])
def get_platos(id_plato):
    dict2 = {'plato1':'tortas', 'plato2':'hojaldres','plato3':'chessecake'}

    return f'Resultado de la busqueda por Id Producto: {dict2[id_plato]}'

# LOGIN

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'Prueba' and password == 'Prueba123':
            return redirect('usuarios')
        elif (username == '' or password == ''):
            flash('User and password could not be empty')
        else:
            flash('Incorrect data')
            
            return render_template('login2.html')

    return render_template('login2.html')




#PERFIL DE USUARIOS
@app.route('/usuarios', methods=['GET','POST'])
def usuarios():
    return 'Pagina de usuarios'

@app.route('/usuarios/<string:id_usuario>', methods=['GET'])
def get_user_by_id(id_usuario):
    usuarios = ['Fabian','Carolina','Leonardo', 'Raul', 'Arturo','Daniel']
    if id_usuario in usuarios:
        return f'Bienvenido {id_usuario}'
    else:
        return 'Usuario no encontrado'




# NOSOTROS

@app.route('/nosotros',methods=['GET'])
def nosotros():
    return 'Nosotros'




if __name__ == '__main__':
    app.run(debug=True)