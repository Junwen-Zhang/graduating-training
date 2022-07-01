### git使用方法

```
git clone https://github.com/Junwen-Zhang/graduating-training.git (克隆项目)

git add -A (暂存所有已修改的文件)
git commit -m ...说明信息 (提交暂存的文件)
git push (向仓库推送)
git pull (拉去最新的版本)

平时记得多pull一下，看看别人有没有跟新。
若本地文件有修改，先add再commit，然后pull下来，如有冲突手动merge，最后再push上去。
```

### 文件目录说明

```
-个人工作(存放个人非正式的一些成果)
-项目交付工作（从wps共享文件夹迁移过来的正式交付材料）
-code（正式的代码成果，后期再细分目录）
-data-excel(用于存放exel数据文件)
-data-database(用于存放数据库文件)
```

### 代码运行说明

1、配置环境：包括mysql环境、flask包、爬虫相关的包。

2、建立数据库：需要用data-database文件夹下的Bilibili.sql文件初始化数据库

3、代码配置：需要在code/Bilibili目录下的config.py中设置自己的数据库链接、用户名和密码。

4、运行项目：点击运行code/Bilibili目录下的app.py文件即可。

