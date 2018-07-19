import scrapy

from scrapy.selector import Selector
from dyttCrawl.items import DyttcrawlItem


class DyttSpider(scrapy.Spider):
    name = "dytt"
    allowed_donaim = ["dytt8.net"]
    start_urls = ["http://www.dytt8.net/html/gndy/dyzz/index.html"]

    def parse(self, response):
        xp = '//table[@class="tbspan"]/tr[2]/td[2]/b/a/@href'
        sel = Selector(response)
        host = 'http://www.dytt8.net'
        detail_urls = sel.xpath(xp).extract()

        headers = {
            'Referer': 'http://www.dytt8.net/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }
        #     {
        #     "Connection": "keep-alive",
        #     "Cache-Control": "max-age=0",
        #     "Upgrade-Insecure-Requests": "1",
        #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #     "Referer": "http://www.dytt8.net/html/gndy/dyzz/index.html",
        #     "Accept-Encoding": "gzip, deflate",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     "Cookie": "UM_distinctid=16493f8484e1d6-0c73558f272ff6-1e2e130c-100200-16493f848502d3; XLA_CI=5ce55dec47018088802f4ef9d366a9d9; CNZZDATA1260535040=1303104925-1531489257-http%253A%252F%252Fwww.dytt8.net%252F%7C1531582594",
        #     "If-None-Match": "09b3b69819d41:328",
        #     "If-Modified-Since": "Thu, 12 Jul 2018 04:27:58 GMT"
        # }

        # for i in detail_urls:
        #     yield scrapy.Request(host + i, callback=self.parseDetail,headers=headers)
        i = detail_urls[0]
        yield scrapy.Request(host + i, callback=self.parseDetail,headers=headers)

        next_urls = sel.xpath('//a[.="下一页"]/@href')
        last_page = sel.xpath('//a[.="末页"]')


    def parseDetail(self, response):

        item = DyttcrawlItem()

        title = response.xpath('//div[@class="bd3r"]/div[@class="co_area2"]/div[@class="title_all"]/h1/font/text()')[0].extract()

        item['title'] = title

        content = response.xpath('//div[@id="Zoom"]/td/p/text()').extract()


        if  len(content):
            for each in content:
                if each.startswith('◎译\u3000\u3000名'):
                    print("yes")
                    # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
                    item['trans_name'] = each[6: len(each)].strip()
                elif each[0:5] == '◎片\u3000\u3000名':
                    # 片名
                    item['full_name'] = each[6: len(each)].strip()
                elif each[0:5] == '◎年\u3000\u3000代':
                    # 年份
                    item['decade'] = each[6: len(each)].strip()
                elif each[0:5] == '◎产\u3000\u3000地':
                    # 产地
                    item['country'] = each[6: len(each)].strip()
                elif each[0:5] == '◎类\u3000\u3000别':
                    # 类别
                    item['film_type'] = each[6: len(each)].strip()
                elif each[0:5] == '◎语\u3000\u3000言':
                    # 语言
                    item['language'] = each[6: len(each)].strip()
                elif each[0:5] == '◎字\u3000\u3000幕':
                    # 字幕
                    item['subtitles'] = each[6: len(each)].strip()
                elif each[0:5] == '◎上映日期':
                    # 上映日期
                    item['publish'] = each[6: len(each)].strip()
                elif each[0:7] == '◎IMDb评分':
                    # IMDb评分
                    item['IMDB_score'] = each[9: len(each)].strip()
                elif each[0:5] == '◎豆瓣评分':
                    # 豆瓣评分
                    item['douban_score'] = each[6: len(each)].strip()
                elif each[0:5] == '◎文件格式':
                    # 文件格式
                    item['format'] = each[6: len(each)].strip()
                elif each[0:5] == '◎视频尺寸':
                    # 视频尺寸
                    item['resolution'] = each[6: len(each)].strip()
                elif each[0:5] == '◎文件大小':
                    # 文件大小
                    item['size'] = each[6: len(each)]
                elif each[0:5] == '◎片\u3000\u3000长':
                    # 片长
                    item['duration'] = each[6: len(each)]
                elif each[0:5] == '◎导\u3000\u3000演':
                    # 导演
                    item['director'] = each[6: len(each)]
                elif each[0:5] == '◎主\u3000\u3000演':
                    # 主演
                    item['actor'] = each[6: len(each)]

        print(item)
        # https: // www.jianshu.com / p / c2b276c0d267
        pass
