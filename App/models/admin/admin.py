from werkzeug.security import generate_password_hash, check_password_hash

from App.exts import db
from App.models import BaseModel
from App.models.admin.models_admin_constant import BLACK_USER, PERMISSION_NONE


class Admin(BaseModel):
    __tablename__ = 'admin'
    email = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256))
    is_delect=db.Column(db.Boolean,default=False)
    permision=db.Column(db.Integer,default=PERMISSION_NONE)
    @property
    def _password(self):
        raise Exception('禁止访问')

    @_password.setter
    def _password(self, password_value):
        self.password = generate_password_hash(password_value)
    def check_password(self,password_value):
        return check_password_hash(self.password,password_value)
    def check_permission(self,permission):
        if  BLACK_USER & self.permission==BLACK_USER:
            return False
        else:
            return permission & self.permision==permission

