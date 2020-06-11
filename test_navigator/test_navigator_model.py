from test_navigator import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class UserData:
    @staticmethod
    def get(user_id):
        user = User.query.filter_by(id=user_id).first()
        return user

    @staticmethod
    def get_all():
        users = User.query.all()
        return users

    @staticmethod
    def create(user_name):
        user = User(name=user_name)
        if user:
            db.session.add(user)
            db.session.commit()
        else:
            return None
        return user
