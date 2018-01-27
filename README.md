# tiebaSpider
## 百度贴吧标题爬虫(urllib2+beautifulsoup)
该爬虫主要是使用对百度贴吧的帖子列表的标题信息进行爬取

由四个函数组成：

    main函数：主要功能是输入所爬的目标贴吧的名称，爬取的起始页码以及截止页码，并组合成目标url 
    
    loadpages函数：主要功能是使用urllib2模块来抓取网页
    
    sparse函数：主要功能是利用BeautifulSoup模块来进行网页解析，定位标题位置，返回标题内容  
    
    write_file函数：主要功能是将抓取到的标题写入文件 

    
    
