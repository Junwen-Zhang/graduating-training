from dbmodel.animation import Animation
from config import db


def getTagsDict():
    datalist = db.session.query(Animation).all()
    taglist=[]
    for data in datalist:
        tags=data.label
        if tags!=None:
            for tag in tags.split():
                taglist.append(tag)

    # print('taglist: ',taglist)
    tags_set=set(taglist)
    dict={}
    for item in tags_set:
        dict.update({item:taglist.count(item)})
    return dict

def get100TagsDict():
    datalist2 = db.session.query(Animation).all()
    taglist = []
    for data in datalist2[0:100]:
        tags = data.label
        if tags != None:
            for tag in tags.split():
                taglist.append(tag)

    # print('taglist: ', taglist)
    tags_set = set(taglist)
    dict = {}
    for item in tags_set:
        dict.update({item: taglist.count(item)})
    # print(dict)
    return dict

get100TagsDict()