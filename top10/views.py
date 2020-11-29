from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import pandas
from requests.compat import quote_plus

image_url = 'https://www.google.com/search?q={}&tbm=isch&hl=en&nfpr=1&sa=X&ved=2ahUKEwjvyci8mZntAhWYOewKHXTkCGgQBXoECAEQIg&biw=1519&bih=722'



# Create your views here.

def top10_movies(request):


    data = requests.get('https://www.imdb.com/chart/top/').text
    soup = BeautifulSoup(data, features='html.parser')
    data=soup.body.find('table').tbody.find_all('tr')
    output=[]
    for i in data[0:10]:
        output+=[[i.td.find('a').img['alt'],i.find('strong').text,i.td.find('a').img['src']]]
    
    return render(request,'top/movies.html',{'ip':output})

def top10_rich(request):


    data = requests.get('https://en.wikipedia.org/wiki/The_World%27s_Billionaires#2020').text
    soup = BeautifulSoup(data,features='html.parser')
    data = soup.find('table',{'class':"wikitable sortable"})
    data = pandas.read_html(str(data),header=0)[0]
    final_list= data.values.tolist()
    data2=[]
    for i in final_list[0:10]:
        image = requests.get(image_url.format(quote_plus(i[1]))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        data2.append(i+[image_src])

    return render(request,'top/rich.html',{'data':data2})

def top10_instgram(request):

    
    data = requests.get('https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts').text
    soup = BeautifulSoup(data, features='html.parser')
    data = soup.find('table')
    data = pandas.read_html(str(data), header=0)[0]
    final_list = data.values.tolist()
    data2 = []
    for i in final_list[0:10]:
        image = requests.get(image_url.format(quote_plus(i[2]))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        data2.append(i+[image_src])
    return render(request,'top/insta.html',{'data':data2})

def top10_youtube_channels(request):

    
    data = requests.get('https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels').text
    soup = BeautifulSoup(data,features='html.parser')
    data = soup.find('table',{'class':"wikitable sortable"})
    data = pandas.read_html(str(data),header=0)[0]
    final_list= data.values.tolist()
    data2=[]
    for i in final_list[0:10]:
        i[1]=i[1][:len(i[1])-4]
        image = requests.get(image_url.format(quote_plus(f'youtube channel logo {i[1]}'))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        data2.append(i+[image_src])
    print(data2[1])

    return render(request,'top/youtube_channels.html',{'data':data2})


def top10_Influential_Persons(request):
    data = requests.get('https://en.wikipedia.org/wiki/The_100:_A_Ranking_of_the_Most_Influential_Persons_in_History').text
    soup = BeautifulSoup(data, features='html.parser')
    data_soup = soup.find('table', {'class': "wikitable"})
    data = pandas.read_html(str(data_soup), header=0)[0]
    final_list = data.values.tolist()
    s=0
    for i in data_soup.find_all('a',{'class':'image'}):
        final_list[s].append(i.img['src'])
        s+=1

    return render(request,'top/influential_persons.html',{'data':final_list})


def top10_internet_companies(request):

    data = requests.get('https://en.wikipedia.org/wiki/List_of_largest_Internet_companies').text
    soup = BeautifulSoup(data, features='html.parser')
    data = soup.find('table')
    data = pandas.read_html(str(data), header=0)[0]
    final_list = data.values.tolist()
    data2 = []
    for i in final_list[0:10]:
        image = requests.get(image_url.format(quote_plus(f'{i[1]} logo'))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        data2.append(i+[image_src])
    return render(request,'top/internet_companies.html',{'data':data2})



def top10_videos(request):
    data = requests.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos').text
    soup = BeautifulSoup(data, features='html.parser')
    data = soup.find('table')
    data = pandas.read_html(str(data), header=0)[0]
    final_list = data.values.tolist()
    data2 = []
    for i in final_list[0:10]:
        i[1]=i[1][:len(i[1])-4]
        image = requests.get(image_url.format(quote_plus(f'{i[1]} youtube video image'))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        data2.append(i+[image_src])
    data2[-1][-1]='data:image/jpeg;base64,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'
    return render(request,'top/videos.html',{'data':data2})

def top10_series(request):


    data = requests.get('https://www.imdb.com/chart/toptv/').text
    soup = BeautifulSoup(data, features='html.parser')
    data=soup.body.find('table').tbody.find_all('tr')
    output=[]
    for i in data[0:10]:
        output+=[[i.td.find('a').img['alt'],i.find('strong').text,i.td.find('a').img['src']]]
    
    return render(request,'top/series.html',{'ip':output})


def top10_popluations(request):

    data = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population').text
    soup = BeautifulSoup(data, features='html.parser')
    data = soup.find('table')
    data = pandas.read_html(str(data), header=0)[0]
    final_list = data.values.tolist()
    data2 = []
    for i in final_list[0:10]:
        if '[' in i[1]:
            i[1]=i[1][:len(i[1])-3]
        image = requests.get(image_url.format(quote_plus(f'{i[1]} flag'))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        data2.append(i+[image_src])
    return render(request,'top/popluations.html',{'data':data2})

def top10_largest_contries(request):

    data = requests.get('https://the-top-10.fandom.com/wiki/Top_10_Biggest_Countries').text
    soup = BeautifulSoup(data, features='html.parser')
    data = soup.find('table')
    data = pandas.read_html(str(data), header=0)[0]
    final_list = data.values.tolist()
    data2 = []
    for i in final_list[0:10]:
        image = requests.get(image_url.format(quote_plus(f'{i[1]} flag'))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        data2.append(i+[image_src])
    return render(request,'top/largest_contries.html',{'data':data2})


def top10_cheap_laptops(request):
    data = requests.get('https://wiki.ezvid.com/best-budget-laptops')
    data_soup = BeautifulSoup(data.text, features='html.parser')
    data = data_soup.find_all('div', {'class': 'item-container'})
    data2 = []
    for i in data:
        image = i.find('div', {'class': 'image-box'}).find('amp-img')['src']
        name = i.find('h3', {'class': 'item-title'}).text
        link = i.find('div',{'class':'item-btn amzn'}).a['href']
        discrption = i.find('div', {'class': "item-review"}).text.replace('\n    \t  \t ','').replace(' \n    \t  \t','')
        data2 += [[ name, discrption,link, image]]

    return render(request,'top/cheap_laptops.html',{'data':data2[::-1]})


def top10_phones(request):
    data = requests.get('https://www.tomsguide.com/best-picks/best-phones')
    data_soup = BeautifulSoup(data.text, features='html.parser')
    data = data_soup.find_all('div', {'class': 'buying-guide-block'})
    final_list= []
    data2=[]
    for i in data:
        name = i.h3.span.text
        link = i.find('div', {'class': 'hawk-affiliate-link-button'}).a['href']
        discrption = i.p.text
        data2 += [[name, discrption, link,]]
    for i in data2:
        image = requests.get(image_url.format(quote_plus(f'{i[0]}'))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        final_list.append(i+[image_src])
    return render(request,'top/best_phones.html',{'data':final_list})


def top10_gaming_laptops(request):
    data = requests.get('https://www.laptopmag.com/articles/best-gaming-laptops')
    data_soup = BeautifulSoup(data.text, features='html.parser')
    data = data_soup.find_all('div', {'class': 'buying-guide-block'})
    data2 = []
    final_list=[]
    for i in data:
        name = i.h3.span.text
        link = i.find('div', {'class': 'hawk-affiliate-link-button'}).a['href']
        discrption = i.find('p',{'class':'specs__container'}).text
        data2 += [[name, discrption, link,]]
    for i in data2[0:10]:
        image = requests.get(image_url.format(quote_plus(f'{i[0]} laptop'))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        final_list.append(i+[image_src])
    return render(request,'top/gaming_laptops.html',{'data':final_list})


def top10_useful_apps(request):
    data = requests.get(
        'https://greatperformersacademy.com/interesting/top-30-most-useful-apps-you-need-on-your-phone-right-now').text
    data_soup = BeautifulSoup(data, features='html.parser')
    data = data_soup.find_all('h3')
    name = []
    link = []
    for i in data[1:11]:
        name += [i.a.text]
        link += [i.find('a')['href']]
    data = data_soup.find_all('p')
    discrption = []
    for i in data[3:]:
        if len(i.text) > 100:
            discrption += [i.text]
    final_list = []
    for i in range(0, 10):
        final_list += [[name[i], link[i], discrption[i]]]
    final_list2=[]
    for i in final_list:
        image = requests.get(image_url.format(quote_plus(f'{i[0]} app logo'))).text
        image_soup = BeautifulSoup(image, 'html.parser')
        image_src=image_soup.find('img',{'class':'t0fcAb'})['src']
        final_list2.append(i+[image_src])
    return render(request,'top/useful_apps.html',{'data':final_list2})


def home(request):
    return render(request,'base.html')