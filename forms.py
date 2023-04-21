
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import SubmitField
from wtforms import EmailField


class EmpresasForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    comuna = StringField('Comuna', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    categoria = StringField('Categoría', validators=[DataRequired()])
    producto_o_servicio =  StringField('Producto/Servicio', validators=[DataRequired()])
    descripcion =  StringField('Descripcion', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
