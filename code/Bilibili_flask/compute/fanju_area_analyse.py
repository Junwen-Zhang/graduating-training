# 统计番剧地区和数量
from config import db
sql="create table fanju_area_count select area,count(area) from fanju group by area"
result = db.session.execute(sql)

print(result)