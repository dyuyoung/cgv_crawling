from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url="http://www.cgv.co.kr/movies/?lt=1&ft=0"
html=urlopen(url).read()


soup=bs(html, "lxml")

movies=soup.find_all("strong", attrs={"class":"title"})
print("<무비차트>----예매율 순")
k=[]
for movie in movies :
  k.append(movie.get_text('\n'))
for i in range(1, 20) :
  print(i, k[i-1])

#개봉일 출력 프로그램

ticket=int(input("개봉일을 알고싶은 영화의 순위를 입력해주세요>>> "))

day=soup.find_all("em", attrs={"class":"dday"})
ps=soup.find_all("span", attrs={"class":"txt-info"})
j=[]
for p in ps :
  j.append(p.get_text())
print(j[ticket-1])

