import requests
import json 
from pprint import pprint
from bs4 import BeautifulSoup 
page = requests.get("https://www.giveindia.org/certified-indian-ngos")
soup = BeautifulSoup(page.text , "html.parser")

def scrape_give_india() :
    d,li={},[]
    main_div = soup.find('table' , class_="jsx-697282504 certified-ngo-table")
    all_tr = main_div.find_all('tr',class_="jsx-697282504")
    for div,cause in zip(range(1,len(all_tr)),range(1,len(main_div)+1)):
        d['Name'] = all_tr[div].find('div',class_="col").text
        d['State']=all_tr[cause].find_all('td',class_='jsx-697282504')[-1].text
        d['Cause']=all_tr[cause].findAll('td',class_='jsx-697282504')[-2].text
        li.append(d.copy())

    with open ('NGO_details.json', 'w') as wr:
        wr.write(json.dumps(li,indent=4))
        wr.close()
    # pprint(li)
    a=input("Enter a name of NGOs, State or Cause:\n")
    for i in li:
        if a in  i.values():
            print(i)

scrape_give_india()











# import requests,pprint,json
# from bs4 import BeautifulSoup

# res=requests.get("https://www.giveindia.org/certified-indian-ngos")
# soup=BeautifulSoup(res.text,"html.parser")
# table=soup.find("table",class_="jsx-697282504 certified-ngo-table")
# tr=table.findAll("tr",class_="jsx-697282504")
# name,states,cause,data,dic=[],[],[],[],{}
# for i in range(1,len(tr)):
#     text=tr[i].findAll("td",class_="jsx-697282504")
#     all_data=[j.text for j in text]
#     name.append(all_data[0])
#     cause.append(all_data[1])
#     states.append(all_data[2])
#     # dic["name"]=all_data[0]
#     # dic["cause"]=all_data[1]
#     # dic["states"]=all_data[2]
#     # data.append(dic.copy())
#     f=open('Give_India_data.json','w')
#     json.dump(data,f,indent=4)
#     f.close()
# I=input("Enter the data filter (1.states or 2.cause): ")
# if I == "1":
#     states2=set(states)
#     dict2={x:[name[j] for j in range(len(name)) if x==states[j]] for x in states2}
#     file=open("Ngo_data.json","w+")
#     name=json.dump(dict2,file,indent=4)
#     file.close()
#     v=input("Enter the state: ")
#     for i in dict2:
#         if v == i:
#             pprint.pprint(dict2[i])
# elif I == "2":
#     cause2=set(cause)
#     dict3={x:[name[j] for j in range(len(name)) if x==cause[j]] for x in cause2}
#     file=open("Ngo_data.json","w+")
#     name=json.dump(dict3,file,indent=4)
#     file.close()
#     v=input("Enter the couse: ")
#     for i in dict3:
#         if v == i:
#             pprint.pprint(dict3[i])

