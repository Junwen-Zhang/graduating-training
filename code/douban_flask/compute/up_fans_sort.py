# 将百大up主按照粉丝数重新排序
from config import db
sql="create table sorted_up select * from up order by fans desc"
result = db.session.execute(sql)

print(result)