from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from database import db
from forms import EmpresasForm
from models import Empresas

app = Flask(__name__)


# configuracion de la base de datos
USER_DB     = 'postgres'
PASS_DB     = 'admin'
URL_DB      = 'localhost'
NAME_DB     = 'Sae_Flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'  

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['AQLALCHEMY_TRACK_MODIFICATION'] = False
# iniciamos la aplicacion con init
db.init_app(app)
# configurar flask migrate
migrate = Migrate()
migrate.init_app(app, db)

# configuracion de flask-wtf
app.config['SECRET_KEY']='llave_secreta'


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    # listado de personas
    # personas = Persona.query.all()
    empresas = Empresas.query.order_by('id')
    total_empresas = Empresas.query.count()
    app.logger.debug(f'Listado Empresas: {empresas}')
    app.logger.debug(f'Total Empresas: {empresas}')
    return render_template('index.html', empresas= empresas, total_empresas = total_empresas)


@app.route('/ver/<int:id>')
def ver_detalle(id):
    # recuperamos la persona segun el id proporcionado
    # persona = Persona.query.get(id)
    empresas = Empresas.query.get_or_404(id)
    app.logger.debug(f'Ver Empresas: {empresas}')
    return render_template('detalle.html', empresas=empresas)


@app.route('/agregar', methods=['GET','POST'])
def agregar():
    empresas = Empresas()
    empresasForm = EmpresasForm(obj=empresas)
    if request.method == 'POST':
        if empresasForm.validate_on_submit():
            empresasForm.populate_obj(empresas)
            app.logger.debug(f'Persona a insertar: {empresas}')
            # INSERTAMOS EL NUEVO REGISTRO
            db.session.add(empresas)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html', forma = empresasForm)


@app.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    empresas = Empresas.query.get_or_404(id)
    empresasForm = EmpresasForm(obj=empresas)
    if request.method == 'POST':
        if empresasForm.validate_on_submit():
            empresasForm.populate_obj(empresas)
            app.logger.debug(f'Persona a actualizar {empresas}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html', forma = empresasForm)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    empresas = Empresas.query.get_or_404(id)
    app.logger.debug(f'Persona a Eliminar: {empresas}')
    db.session.delete(empresas)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/buscar', methods=['POST'])
def buscar():
    termino_busqueda = request.form['termino_busqueda']
    # Lógica para buscar empresas con el término de búsqueda  
    empresas = Empresas.query.filter(Empresas.nombre.like(f'%{termino_busqueda}%')).all()
    # empresas = Empresas.query.filter(Empresas.email.like(f'%{termino_busqueda}%')).all()
    # empresas = Empresas.query.filter(Empresas.categoria.like(f'%{termino_busqueda}%')).all()
    # empresas = Empresas.query.filter(Empresas.producto_o_servicio.like(f'%{termino_busqueda}%')).all()
    total_empresas = len(empresas)
    app.logger.debug(f'Empresas encontradas: {empresas}')
    return render_template('resultados_busqueda.html', empresas=empresas, total_empresas=total_empresas)

# @app.route('/')
# def index():
#     imagenes = ['sercotec1.jpg', 'sercotec2.jpg', 'sercotec3.jpg', 'sercotec4.']
#     return render_template('carousel.html', imagenes=imagenes)



# @app.route('/insertar_empresas')
# def insertar_empresas():
#     # Datos de ejemplo
#     empresas = [
#         {"nombre": "Empresa 1", "email": "empresa1@gmail.com", "categoria": "Tecnología", "producto_servicio": "Software"},
#         {"nombre": "Empresa 2", "email": "empresa2@gmail.com", "categoria": "Tecnología", "producto_servicio": "Hardware"},
#         {"nombre": "Empresa 3", "email": "empresa3@gmail.com", "categoria": "Alimentación", "producto_servicio": "Productos orgánicos"},
#         {"nombre": "Empresa 4", "email": "empresa4@gmail.com", "categoria": "Transporte", "producto_servicio": "Logística"},
#         {"nombre": "Empresa 5", "email": "empresa5@gmail.com", "categoria": "Turismo", "producto_servicio": "Paquetes vacacionales"},
#         {"nombre": "Empresa 6", "email": "empresa6@gmail.com", "categoria": "Servicios financieros", "producto_servicio": "Préstamos"},
#         {"nombre": "Empresa 7", "email": "empresa7@gmail.com", "categoria": "Salud", "producto_servicio": "Medicina alternativa"},
#         {"nombre": "Empresa 8", "email": "empresa8@gmail.com", "categoria": "Educación", "producto_servicio": "Cursos en línea"},
#         {"nombre": "Empresa 9", "email": "empresa9@gmail.com", "categoria": "Arte y diseño", "producto_servicio": "Diseño gráfico"},
#         {"nombre": "Empresa 10", "email": "empresa10@gmail.com", "categoria": "Marketing", "producto_servicio": "Publicidad en línea"}
#     ]
#     # Insertar las empresas en la base de datos
#     for empresa in empresas:
#         nueva_empresa = Empresas(nombre=empresa['nombre'], email=empresa['email'], categoria=empresa['categoria'], producto_servicio=empresa['producto_servicio'])
#         db.session.add(nueva_empresa)
#     db.session.commit()
#     return 'Empresas insertadas correctamente'














