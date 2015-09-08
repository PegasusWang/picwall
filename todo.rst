bjfu 19740303 123456
1.把width作为参数传入，使用户自己控制。用脚本控制item和col宽度。

速度优化：
-leancloud查询使用include限定字段优化.
-异步查询。
**使用tornado-redis异步查询redis**,需要一次行初始化的放在Application里边，不要放在handler类里。
-redis缓存。hset classname page queryresult
（定时更新脚本,限定每个类页面数，计算占用空间)
-nginx处理静态文件。
-多进程启动tornado，配合nginx监听不同的端口。

程序优化：
-容错。什么时候用if判断，什么时候用try、catch，哪些地方会出现异常。哪些地方需要用if。存入redis的数据是否是有效的。
-数据库有些图片文件损坏或者无效导致显示不出来。或者没有width和height数据导致拿不到高和宽（考虑给赋一个default值，同时定期用脚本处理，没有设置的值重新设置）
-合理组织文件


用户优化：
-不同屏幕显示效果如何。
-有没有部分图片没有显示出来。
-gif消耗大，考虑用缩略图。
-有没有死链。是否带不带后/的域名都是可以访问的.
-404和500界面能用吗?

部署：
可能需要扩大文件描述符打开数量限制。

测试：
redis速度测试。空间占用问题
curl爬虫是否容易

todo:
测试不用redis和用redis缓存的效率。记录。redis快100倍左右,request per query。
len(query) == 2436, 100000条数据大概232.3MB
测试异步redis和同步redis的效率。(tornado-redis效果并不好，hset。采用非异步方式。
在leancloud的查询参数加上请求的名字，从而实现不同类的查询
把初始化放到Applicaitoin上, redis放在app上，leancloudapi还是放在(待定)
改用一步的redis实现
#debug下: 修改base页面,把出错信息返回到web页面, 上线后或许需要用500页面
#容错处理：没有weight和height的情况会出错，（包括leancloud和redis的数据）
    首先给leancloud没有高和宽度的图片默认的值，之后再缓存到redis里边。这样可以
    保证leancloud数据完整后redis里的一定是完整的数据，不需要另行处理redis的。
写定时脚本每天更新每个类的每个页面。和每次设置所有类前100张图片的高和宽度值。
