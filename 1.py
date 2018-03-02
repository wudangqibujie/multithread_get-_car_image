import requests
from lxml import etree
import datetime
import time

def get_link():
    url = "https://www.che168.com/shenzhen/benchi/#pvareaid=102179"
    header = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",}
    r = requests.get(url,headers=header)
    html = etree.HTML(r.text)
    link = html.xpath('//li[@isafteraudit="10"]/a/@href')
    links = ["https://www.che168.com"+str(i) for i in link]
    return links

def get_img_link(car_url):
    r = requests.get(car_url)
    html = etree.HTML(r.text)
    img_url = html.xpath('//div[@class = "fc-piclist fn-clear"]/ul/li/a/img/@src2')
    img_urls = ["http:"+str(i) for i in img_url]
    return img_urls

def get_image(img_urls):
    i = 2
    for url in img_urls:
        r = requests.get(url,stream = True)
        image = r.content
        with open ("%d.jpg"%i,"wb") as f:
            f.write(image)
        i = i+1

if __name__ == "__main__":
    t1 = time.time()
    one_car_links = get_link()
    all_image_links = []
    for one_car_link in one_car_links:
        all_image_links.extend(get_img_link(one_car_link))
    get_image(all_image_links[:50])
    t2 = time.time()
    print("总工耗时间：%f"%(t2-t1))







    # thread = []
    #
    # for i in range(0,250,25):
    #     geturl = url + "/start=" + str(i)                     #要获取的页面地址
    #     print("Now to get " + geturl)
    #     t = threading.Thread(target=crawler,
    #                          args=(s,i,url,header,image_dir,worksheet,txtfile))
    #     thread.append(t)
    #
    # for i in range(0,10):
    #     thread[i].start()
    #
    # for i in range(0,10):
    #     thread[i].join()
    #
    # end = datetime.now()    #结束计时
    # print(end)
    # print("程序耗时： " + str(end-now))
    # txtfile.close()
    # workbookx.close()
