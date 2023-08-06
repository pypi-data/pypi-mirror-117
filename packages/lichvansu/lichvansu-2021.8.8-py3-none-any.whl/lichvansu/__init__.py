# trumxuquang@gmail.com
import math
import re
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import requests
import urllib3
urllib3.disable_warnings()

url_source = 'https://vansu.net/lich-van-nien.html'
vn_begin = '<div class="block-description-function change-calendar"><div class="kqua"><div class="result-change" style="margin-top:0px;"><p>'
vn_end = '<div class="lich-xem-chi-tiet" style="text-align: right; color: #d21c1b; text-decoration: underline; margin: 10px;">'
url_day = '?day='
url_mon = '&mon='
url_year = '&year='


class vansu:
    """ API class for EVN Online API  """

    INTERVAL_6MIN = "6min"
    INTERVAL_DAY = "day"

    def __init__(self, name=None):

        self._name = name


    def get_vansu(self):
        try:
            response = requests.get(url = url_source, verify = False).text

            #print(response)
            text_vn = response

            begin_index = text_vn.index(vn_begin)
            end_index = text_vn.index(vn_end)
            json_vn = text_vn[ begin_index + 149 : end_index - 59 ].strip()
            #print(json_vn)
            arr = json_vn.splitlines()
            
            #khai bao var
            amLich = "NA"
            saoTot = "NA"
            saoXau = "NA"
            gioTot = "NA"
            gioXau = "NA"
            truc = "NA"
            tuoiHop = "NA"
            tuoiXung = "NA"
            onlyDay = "NA"
            txt_tomo = "NA"
            ngayTotXau ="NA"
            # procesing
            saoTot = arr[3].replace('<b>', '').replace('</b>', '').replace('<br/>', '').strip()
            saoXau = arr[4].replace('<b>', '').replace('</b>', '').replace('<br/>', '').strip()
            amLich = arr[1].replace('<b>', '').replace('</b>', '').replace('<br/>', '').replace('<br>', '').strip()

            ##chia array 2
            arr2 = arr[2].split('<strong class="clr-red">')
            #print(arr2[1])
            gioTot = arr2[1].replace('</strong> <table><tbody><tr><td>', ' ').replace('</td><td>', ', ').replace('</td></tr><tr><td>', ', ').replace('</td></tr></tbody></table></p><p>', '').replace('</strong><div class="giohh-cs"> <table><tbody><tr><td>', '').replace('</td></tr></tbody></table></div></p><p>', '').strip()
            gioTot = self.tachhtml(gioTot)
            
            gioXau = arr2[2].replace('</strong> <table><tbody><tr><td>', ' ').replace('</td><td>', ', ').replace('</td></tr><tr><td>', ', ').replace('</td></tr></tbody></table></p><p>', '').strip()
            gioXau = self.tachhtml(gioXau)

            tuoiHop = arr2[3].replace('<p>', ' ').replace('</td><td>', ', ').replace('</td></tr><tr><td>', ', ').replace('</strong>', '').strip()

            tuoiXung = arr2[4].replace('<p>', ' ').replace('</td><td>', ', ').replace('</p>', ', ').replace('</strong>', '').strip()

            truc = arr2[5].replace('</strong><br>', ' ').replace('<br>', ', ').replace('</td></tr><tr><td>', ', ').replace('</p><p>', '').strip()

            ngayTotXau = arr2[0].replace('</p><p>', ' ').strip()

            # onlydate
            onlyDay = amLich.split("/")[0]
            if onlyDay.find("0") == 9:
                onlyDay = onlyDay[ -1  : ]
            else :
                onlyDay = onlyDay[ -2  : ]
            """
            print("$$$$$$$ : " + amLich)
            print("$$$$$$$ : " + saoTot)
            print("$$$$$$$ : " + saoXau)
            print("$$$$$$$ : " + gioTot)
            print("$$$$$$$ : " + gioXau)
            print("$$$$$$$ : " + ngayTotXau)
            print("$$$$$$$ : " + truc)
            print("$$$$$$$ : " + tuoiHop)
            print("$$$$$$$ : " + tuoiXung) """
            ######################
            tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
            arr_tomo = tomorrow.strftime('%Y-%-m-%-d').split('-')
            url_day = '?day=' + arr_tomo[2]
            url_mon = '&mon=' + arr_tomo[1]
            url_year = '&year=' + arr_tomo[0]

            # call request tomorrow
            url_tomo = url_source + url_day + url_mon +url_year
            response_tomo = requests.get(url = url_tomo, verify = False).text
            txt_tomo = response_tomo[ response_tomo.index('<b>Âm lịch:</b> ') + 16 : response_tomo.index('<b>Âm lịch:</b> ') + 18 ].strip()
            
            if txt_tomo.find("0") == 0:
                txt_tomo = txt_tomo[ 1  : 2]
            else :
                txt_tomo = txt_tomo[ 0  : ] 

        except:
            amLich = "NA"
            saoTot = "NA"
            saoXau = "NA"
            gioTot = "NA"
            gioXau = "NA"
            truc = "NA"
            ngayTotXau = "NA"
            tuoiHop = "NA"
            tuoiXung = "NA"
            onlyDay = "NA"
            txt_tomo = "NA"

        return {'amLich': amLich, 'saoTot': saoTot ,'saoXau': saoXau, 'gioTot': gioTot, 
            'gioXau': gioXau ,'ngayTotXau': ngayTotXau, 'truc':truc, 'tuoiHop':tuoiHop, 'tuoiXung':tuoiXung, 'ngay_homnay':onlyDay, 'ngay_mai' :txt_tomo }

    ##########
    def tachhtml(self, str):
        str = str.replace('</td></tr></tbody></table></div></p><p>','').replace('</strong><div class="giohh-cs"> <table><tbody><tr><td>','')
        return str.strip()

    #print(get_vansu())
