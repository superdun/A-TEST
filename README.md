![mahua](mahua-logo.jpg)
#股票爬虫（前端+后台+爬虫）



##有哪些功能？

抓取雅虎财经中的股票主要信息保存于数据库（splite）并显示在网页中
  
实现图片上传

##模块介绍
###myflask.py
后端主程序
实现基本的后台功能  
能从数据库test.db中读取股票信息，由AJAX更新页面
###fast_get.py
爬虫主程序快速版   
循环从索引页读取股票主要信息，并不分别进入各只股票页面爬取详细信息，存入临时数据库tst.db中，爬完   
一次后将tst.db替换掉老的test.db
###slow_get.py
爬虫主程序详细版   
循环从索引页读取股票名称，并分别进入各只股票页面爬取详细信息，存入临时数据库tst.db中，爬完   
一次后将tst.db替换掉老的test.db.目前代码爬取的详细信息和fast一样，可自己拓展
###图片上传
至static\uploaded_pics中，可以检测文件类型（jpg,png,bmp）
###前端
使用flask自带的jinjia2模板（因为是单页面，其实目前没什么用，但方便以后拓展），使用bootstrap  
布局

##使用方法
运行myflask.py，并且同时运行fast_get.py或slow_get.py   
访问127.0.0.1:8080

##不足&改进
由于时间有限，且我的网上雅虎特别慢，调试十分困难   
可后台中创建新进程将get的程序运行于其中，这样就不用手动打开两个py文件
可以将get写成分布式运行，在多台电脑中增加爬取速度

![mahua](https://github.com/superdun/A-TEST/raw/master/examp_pic/1.jpg)
![mahua](https://github.com/superdun/A-TEST/raw/master/examp_pic/2.jpg)

