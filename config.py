import os

root_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Database settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(root_dir, 'test_navigator_data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # GUI settings
    STATIC_DIR = root_dir + '/gui/static'
    TEMPLATES_DIR = root_dir + '/gui/templates'

    # Other settings
    SECRET_KEY = 'my-secret-key'
    JSON_AS_ASCII = False
    JSONIFY_PRETTYPRINT_REGULAR = True
