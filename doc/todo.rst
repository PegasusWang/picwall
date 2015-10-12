bjfu 19740303 123456
1.把width作为参数传入，使用户自己控制。用脚本控制item和col宽度。
2.设置大图版本和小图版本, 使用不同的url。

速度优化：
-异步查询。
-redis缓存。hset classname page queryresult
（定时更新脚本,限定每个类页面数，计算占用空间, redis设置conf)

程序优化：
-容错。什么时候用if判断，什么时候用try、catch，哪些地方会出现异常。哪些地方需要用if。存入redis的数据是否是有效的。
-数据库有些图片文件损坏或者无效导致显示不出来。或者没有width和height数据导致拿不到高和宽（考虑给赋一个default值，同时定期用脚本处理，没有设置的值重新设置）


用户优化：
-不同屏幕显示效果如何。手机版适配.
-有没有部分图片没有显示出来。
-有没有死链。是否带不带后/的域名都是可以访问的.
-随意输入url会不会重定向?
-404和500界面能用吗?

部署：
可能需要扩大文件描述符打开数量限制。ulimit.
#debug下: 修改base页面,把出错信息返回到web页面, 上线后或许需要用500页面

测试：
redis速度测试。空间占用问题
#容错处理：没有weight和height的情况会出错，（包括leancloud和redis的数据）
    首先给leancloud没有高和宽度的图片默认的值，之后再缓存到redis里边。这样可以
    保证leancloud数据完整后redis里的一定是完整的数据，不需要另行处理redis的。
写定时脚本每天更新每个类的每个页面查询redis。和每次设置所有类前1000张图片的高和宽度值。

定期工作：
更新类名字.
图片筛选测试：只有长度和宽度大于特定的才要.是在handle还是用脚本跑

todo:
运行redisupdate之前先运行update_leancloud
如果是从redis取得数据的可以设置查询参数


declaretion:
Dedicated to carrying the hottest online image compilation of Sexy Asian women for Entertainment purposes. In no way are we implying that any of the women on this site are actual
"doumi girls", it is just our name. We do not own images displayed on this site, and credit is due to the respectful owners of the photos. Photos will be taken down promptly if requested
by the rightful owners (Ask me anything). Intended for mature audiences due to the erotic nature of some of the poses (PG-13).

匹配qq的正则
[1-9][0-9]{4,}
配置好redis内存


注意:修改了leancloudhandle的接口后,backend里边的update_redis也要相应修改

todo：
写下载接口,对不同类别混图.
添加新的分类，潮流，，壁纸,高清
注意:修改了leancloudhandle的接口后,backend里边的update_redis也要相应修改
相册页面下边加上来源,给每个类建立个字段
手机页面
写声明页面，写上github链接,版权信息等。下一步规划,合作开发,代码疑问
整理app类别，去掉不用的图片分类，节省空间和费用。


SEO:
把其他所有域名都用dnspod转发到一个显性转发.或者使用nginx配置下可以301转发.
加友链找合作，友链页面。
sendcloud接口
按照百度统计建议,图片信息需要alt信息，给每个字段加上alt字段，大致给个分类信息.
