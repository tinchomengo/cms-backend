from app.database import session
from app.models.admin import Admin

def create_admin(email, password, role):
    new_admin = Admin(email=email, password=password, role=role)
    session.add(new_admin)
    session.commit()
    return new_admin
