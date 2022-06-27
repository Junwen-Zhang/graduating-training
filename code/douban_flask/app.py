#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: app_test.py

from config import app

from views.index_view import index

# from views.animation_view import animation
from views.guichu_view import guichu
# from views.up_view import up
# from views.video_view import video

# app.register_blueprint(animation, url_prefix="/animation")
app.register_blueprint(guichu, url_prefix="/guichu")
#app.register_blueprint(index, url_prefix="/")
# app.register_blueprint(up, url_prefix="/up")
# app.register_blueprint(video, url_prefix="/video")

# from views.animation_view import animation
# from views.guichu_view import guichu
# from views.up_view import up


# app.register_blueprint(animation, url_prefix="/animation")
app.register_blueprint(guichu, url_prefix="/guichu")
#app.register_blueprint(index, url_prefix="/")
# app.register_blueprint(up, url_prefix="/up")
# app.register_blueprint(video, url_prefix="/video")


if __name__ == '__main__':
    app.run(debug=True)
