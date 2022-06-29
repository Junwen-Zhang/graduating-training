#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: app_test.py

from config import app

from views.index_view import index
<<<<<<< HEAD
=======

>>>>>>> 962e2362d293a0b2d1e82434eaeaec9caec31c2a


from views.animation_view import animation
from views.up_view import up


app.register_blueprint(animation, url_prefix="/animation")
# app.register_blueprint(guichu, url_prefix="/guichu")
app.register_blueprint(index, url_prefix="/")
app.register_blueprint(up, url_prefix="/up")
<<<<<<< HEAD
=======
# app.register_blueprint(video, url_prefix="/video")
# from views.animation_view import animation

>>>>>>> 962e2362d293a0b2d1e82434eaeaec9caec31c2a


if __name__ == '__main__':
    app.run(debug=True)
