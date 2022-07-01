## 代码运行说明

1、配置环境：包括mysql环境、flask包、爬虫相关的包。

2、建立数据库：需要用Bilibili.sql文件初始化数据库。

3、代码配置：需要在Bilibili目录下的config.py中设置自己的数据库链接、用户名和密码。

4、运行项目：点击运行Bilibili目录下的app.py文件即可。



## 代码分工说明

### Bilibili_Flask （网站代码）

```
│  app.py
│  config.py
├─compute (数据处理)
│  │  anime_tags.py                     张倩
│  │  fanju_area_analyse.py             兰庆秋
│  │  guichu_submithour.py              章俊文
│  │  MysqlConfig.py                    汪泽鸿
│  │  up_fans_sort.py                   兰庆秋       
│  │  up_trend_count.py                 汪泽鸿
│       
├─dbmodel(数据库类)
│  │  animation.py                      兰庆秋
│  │  guichu.py                         章俊文
│  │  up.py								兰庆秋
│  │  video.py                          章俊文
│          
├─LinkAnalysis(实时爬虫)
│  │  linkAnalys.py   					宁可馨                   
│  │  stopwords.txt                     宁可馨
│  │  
│  ├─Tools
│  │  │  cacu_DeltaT.py					宁可馨
│  │  │  cnt_DeltaT.py					宁可馨
│  │  │  spider_videoComment.py          张倩
│  │  │          
│      
├─static
│  └─assets  
│      ├─main(JS绘图)
│      │      animation_tags_analy.js      张倩
│      │      searchVideo_view.js          张倩	宁可馨
│      │      show_animation_area.js       兰庆秋
│      │      show_animation_score.js      兰庆秋
│      │      show_guichu_length.js        章俊文
│      │      show_guichu_submithour.js    章俊文
│      │      show_guichu_wordcloud.js     章俊文
│      │      show_most_popular_up_tags.js 兰庆秋 
│      │      show_up_fans.js              兰庆秋 
│      │      show_up_trend.js             兰庆秋 
│      │      show_video_time.js           章俊文
│      │      show_video_wordcloud.js      章俊文
│      │      show_up_tags.js              汪泽鸿
│ 	   │   	 test         
├─templates(html页面)
│  │  
│  │  bar-simple.html					汪泽鸿
│  │  guichu_main.html                  杨雅馨
│  │  searchVideo.html					杨雅馨
│  │  searchVideo_main.html             张倩	宁可馨
│  │  show-most-popular-up-2.html       兰庆秋 秦霄潇
│  │  show-up-fans-2.html               兰庆秋 秦霄潇
│  │  show-up-trend-2.html              兰庆秋 秦霄潇
│  │  show100animation.html             兰庆秋
│  │  show100up-2.html                  兰庆秋 秦霄潇
│  │  show_animation_area.html          兰庆秋
│  │  show_animation_main.html          兰庆秋 汪泽鸿
│  │  show_animation_score.html         兰庆秋
│  │  show_animation_tags.html          张倩
│  │  up-main-2.html                    兰庆秋 秦霄潇
│  │  video_hot.html                    章俊文	宁可馨
│  │  
│          
├─views(Flask路由)
│  │  animation_view.py                 兰庆秋 汪泽鸿
│  │  guichu_view.py                    章俊文
│  │  index_view.py						杨雅馨
│  │  searchVideo_view.py               张倩	宁可馨
│  │  up_view.py                        兰庆秋 秦霄潇
│  │  video_view.py                     章俊文
│        
```

### Spider  （爬虫代码）

```
张倩：
1.番剧数据爬取
  FirstPage.py
  secondPage.py
  spider.py
2.视频数据爬取（中间代码）
  spider_videoComment.py  
  spider_videoInfo.py  
```

```
宁可馨：
1.视频相关数据爬取
  spider_danmakuTime.py
  spider_vedioLink.py
  spider_vedioTime.py
2.视频爬取工具类
  ./Tools/cacu_DeltaT.py
  ./Tools/cnt_DeltaT.py
  ./Tools/get_DanmakuT.py
  ./Tools/getCID.py
 3.数据爬取调用
  spider.py
```

```
汪泽鸿：
1.热门视频url数据爬取
  pubdate_url.py
2.热门视频投放时间数据爬取
  pubdate.py
```

```
杨雅馨：
1.鬼畜相关数据爬取
  guichu_spider.py
```



