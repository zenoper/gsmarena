from bs4 import BeautifulSoup
import requests


ip_addresses = []
with open("ip_addresses.txt", "r") as f:
    for i in range(100):
        ip_addresses.append(f.readline()[0:-1])
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}



brand_links = []
with open("brand_links.txt", "r") as f:
    for i in range(82): #change here to select how many pages to surf
        brand_links.append(f.readline()[0:-1])


i = 0
phone_links = []
for link in brand_links:
    proxy = {'http': 'http://' + ip_addresses[i]}
    html = requests.get(link, proxies=proxy, headers=headers).content
    soup = BeautifulSoup(html,'lxml')
    phone_tags = soup.select('div.makers ul li a')
    for phone in phone_tags:
        links = "https://www.gsmarena.com/"+phone['href']
        phone_links.append(links)
        # print(f"links -> {links}")
    i = i+1
    # print(f"{link}, {html}")
    print(f"{i} links are done")


with open("phone_links1.txt","w") as f:
    for i in phone_links:
        f.write(f'{i}\n')