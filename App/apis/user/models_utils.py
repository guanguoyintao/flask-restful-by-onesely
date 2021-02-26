from App.models.user import User


def get_user(user_ident):
    user=User.query.get(user_ident)
    if user:
        return user
    user=User.query.filter(User.email==user_ident).first()
    if user:
        return user
    user=User.query.filter(User.name==user_ident).first()
    if user:
        return user
    return None

