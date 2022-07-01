from config import db
sql="create table guichu_submithour_count select hour(submit_time),count(url) from guichu group by hour(submit_time);"
result = db.session.execute(sql)

print(result)