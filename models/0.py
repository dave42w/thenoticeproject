from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'The Notice Project'
settings.subtitle = 'powered by web2py'
settings.author = 'Dave Warnock'
settings.author_email = 'dave@warnock.me.uk'
settings.keywords = ''
settings.description = 'Digital Noticeboards made easy'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '2176e1cb-ee75-47c5-899e-f5a93c6323a3'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
