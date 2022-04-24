from application import app

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://food:passWORD@localhost/EFFP"