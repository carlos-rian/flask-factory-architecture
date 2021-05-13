from app.model.tables import User, db
from app.model.serializer import SerialUser

# é uma forma de converter um objeto do banco(classe) para dict e vice-versa.
serial_user = SerialUser()


def select_user(username: str):
    user = (
        User.query.with_entities(User.username, User.id, User.email, User.name)
        .filter_by(username=username)
        .first()
    )
    return serial_user.dump(user)


def create_user(data: dict):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    db.session.flush()
    return {"message": "user created.", "user": serial_user.dump(user)}, 201


def update_user(data: dict, username: str):
    user = db.session.query(User).filter_by(username=username).first()
    if not user:
        return {"message": "user not exists."}, 400
    db.session.query(User).filter_by(username=username).update(data)
    db.session.commit()
    return serial_user.dump(user)


def delete_user(username: str):
    user = User.query.filter_by(username=username).first()
    db.session.delete(user)
    db.session.commit()
    return {"message": "user deleted."}