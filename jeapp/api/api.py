import pandas as pd
import os
import time
import numpy as np

#사용하는 라이브러리
from bs4 import BeautifulSoup   # 웹문서 처리 라이브러리
import requests                 #웹에서 요청/ 응답을 처리하는 라이브러리
from openpyxl.workbook import Workbook
import pandas as pd

def traffic_bus(tra_id):

    url = "http://apis.data.go.kr/6260000/BusanBIMS/bitArrByArsno?arsno={}&serviceKey={}"

    apikey="z%2BMThYhsIiJ1ITaPe4ltugLn1nmbggse6XnxKEq%2Fg3ulDnIAkdtrPJ6aUhOaJD3jW2DFBHQELOrr7vF91vpddQ%3D%3D"
    num = tra_id

    api_url =url.format(num, apikey)
    # print(api_url, "\n\n")
    
    rs_data = requests.get(api_url)
    time.sleep(2)
    
    rs_text = rs_data.text

    rs_xml = BeautifulSoup(rs_text, "lxml")
    print(rs_xml)
    
    time.sleep(2)
    
    bstopid=[]        #정류소ID
    bustype=[]        #버스종류
    bstopidx=[]   #순번
    lineno= [] #버스번호
    lineid= []  #노선ID
    gpsx= []    # 정류소 경도, lon
    gpsy= []       # 정류소 위도, lat
    nodenm= []        # 정류소명
    carno1= []   #차량번호
    min1= []         #남은도착시간
    lowplate1= []      #일반/저상버스
    station1= []     # 남은정류소 수
    seat1= []        #빈 좌석 수
    carno2= []    #차량번호
    min2= []        #남은도착시간
    station2= []   #남은 정류소 수
    carno2= []    #차량번호

    for i in range(len(rs_xml.find_all("bstopid"))):
        try :
            bstopid.append(rs_xml.find_all("bstopid")[i].text)         #정류소ID
        except:
            bstopid.append(np.NaN)
        try :
            bustype.append(rs_xml.find_all("bustype")[i].text)          #버스종류
        except:
            bustype.append(np.NaN)
        try :
            bstopidx.append(rs_xml.find_all("bstopidx")[i].text)       #순번
        except:
            bstopidx.append(np.NaN)         
        try :
            lineno.append(rs_xml.find_all("lineno")[i].text)           #버스번호
        except:
            lineno.append(np.NaN) 
        try :
            lineid.append(rs_xml.find_all("lineid")[i].text)           #노선ID
        except:
            lineid.append(np.NaN) 
        try :
            gpsx.append(rs_xml.find_all("gpsx")[i].text)             # 정류소 경도, lon
        except:
            gpsx.append(np.NaN) 
        try :
            gpsy.append( rs_xml.find_all("gpsy")[i].text)             # 정류소 위도, lat
        except:
            gpsy.append(np.NaN) 
        try :
            nodenm.append(rs_xml.find_all("nodenm")[i].text)          # 정류소명
        except:
            nodenm.append(np.NaN) 
        try :
            carno1.append(rs_xml.find_all("carno1")[i].text)           #차량번호
        except:
            carno1.append(np.NaN) 
        try :
            min1.append(rs_xml.find_all("min1")[i].text)                #남은도착시간
        except:
            min1.append(np.NaN) 
        try :
            lowplate1.append(rs_xml.find_all("lowplate1")[i].text)       #일반/저상버스
        except:
            lowplate1.append(np.NaN) 
        try :
            station1.append(rs_xml.find_all("station1")[i].text)       #남은 정류소 수일반/저상버스
        except:
            station1.append(np.NaN) 
        try :
            seat1.append(rs_xml.find_all("seat1")[i].text)            #빈 좌석 수
        except:
            seat1.append(np.NaN) 
        try :
            carno2.append(rs_xml.find_all("station1")[i].text)       #차량번호
        except:
            carno2.append(np.NaN) 
        try :
            min2.append(rs_xml.find_all("min2")[i].text)             #남은도착시간
        except:
            min2.append(np.NaN) 
        try :
            station2.append(rs_xml.find_all("station2")[i].text)       #남은 정류소 수
        except:
            station2.append(np.NaN) 
        try :
            carno2.append(rs_xml.find_all("station1")[i].text)       #차량번호
        except:
            carno2.append(np.NaN)
            
#         print(bstopid,bustype,bstopidx,lineno,lineid,gpsx,gpsy,nodenm,carno1,min1,lowplate1)
        
        
        time.sleep(2)

    return(bstopid,bustype,bstopidx,lineno,lineid,gpsx,gpsy,nodenm,carno1,min1,lowplate1,station1)

