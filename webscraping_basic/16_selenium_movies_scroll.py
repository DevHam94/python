# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies?hl=ko&pli=1"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#            "Accept-Language":"ko-KR,ko"
#            }

# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class":""})
# print(len(movies))

# # with open("movie.html", "w", encoding="utf8") as f:
# #   # f.write(res.text)
# #   f.write(soup.prettify()) # html 문서를 예쁘게 출력 

# for movie in movies:
#   title = movie.find("div", attrs={"class":""}).get_text()
#   print(title)

from selenium import webdriver
browser = webdrvier.Chrome()
browser.maximize.window()

# 페이지 이동 
url = "https://play.google.com/store/movies?hl=ko&pli=1"
browser.get(url)
 
# 스크롤 내리기
browser.execute_script("window.scrollTo(0, 1080)")
 
 
 