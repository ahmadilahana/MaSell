from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://penduduk_mos:penduduk_mos#51161@203.161.184.104:3306/penduduk_mos")
# engine = create_engine("mysql+pymysql://[username]:[password]@203.161.184.104:[port]/[dbname]")

meta = MetaData()

conn = engine.connect()