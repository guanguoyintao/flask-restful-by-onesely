from App.models.admin import Admin


def get_admin(user_ident):
    admin=Admin.query.get(user_ident)
    if admin:
        return admin
    admin=Admin.query.filter(Admin.email==user_ident).first()
    if admin:
        return admin
    admin=Admin.query.filter(Admin.name==user_ident).first()
    if admin:
        return admin
    return None

