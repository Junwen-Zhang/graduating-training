#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: app_test.py

from config import app

from views.index_view import index
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 962e2362d293a0b2d1e82434eaeaec9caec31c2a


from views.animation_view import animation
from views.up_view import up

=======
from views.searchVideo_view import search
# from views.animation_view import animation
from views.guichu_view import guichu
# from views.up_view import up
# from views.video_view import video
>>>>>>> 98410bb84cd07b75313d573972a765d794d66fd9

# app.register_blueprint(animation, url_prefix="/animation")
app.register_blueprint(guichu, url_prefix="/guichu")
app.register_blueprint(index, url_prefix="/")
<<<<<<< HEAD
app.register_blueprint(up, url_prefix="/up")
<<<<<<< HEAD
=======
=======
app.register_blueprint(search,url_prefix="/searchVideo")
# app.register_blueprint(up, url_prefix="/up")
>>>>>>> 98410bb84cd07b75313d573972a765d794d66fd9
# app.register_blueprint(video, url_prefix="/video")
=======
# from views.animation_view import animation
from views.guichu_view import guichu
# from views.up_view import up
from views.video_view import video
from views.searchVideo_view import search
# app.register_blueprint(animation, url_prefix="/animation")
app.register_blueprint(guichu, url_prefix="/guichu")
app.register_blueprint(index, url_prefix="/")
# app.register_blueprint(up, url_prefix="/up")
app.register_blueprint(video, url_prefix="/video")
app.register_blueprint(search,url_prefix="/search")

<<<<<<< HEAD
>>>>>>> 962e2362d293a0b2d1e82434eaeaec9caec31c2a

=======
>>>>>>> d2d11bec2ac7d572e1f9f81297b8b86409d221d8
>>>>>>> 98410bb84cd07b75313d573972a765d794d66fd9

if __name__ == '__main__':
    app.run(debug=True,port="5002")
