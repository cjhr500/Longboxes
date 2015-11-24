def login():
    """
    exposes:
    http://..../[app]/default/user/login
    """
    return dict(form=auth.login())

def register():
    """
    exposes:
    http://..../[app]/default/user/register
    """
    return dict(form=auth.register())

def logout():
    return dict(form=auth.logout())
