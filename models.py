from database import db


class Empresas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    telefono = db.Column(db.Integer)
    comuna = db.Column(db.String(250))
    email = db.Column(db.String(250))
    categoria= db.Column(db.String(250))
    producto_o_servicio = db.Column(db.String(250))

    def __str__(self):
        return (
            f'Id: {self.id},'
            f'Nombre: {self.nombre},' 
            f'Telefono: {self.telefono},'
            f'Comuna: {self.comuna},'
            f'Email: {self.email}'
            f'Categoria: {self.categoria}'
            f'Progucto_o_Servicio: {self.producto_o_servicio}'
        )
