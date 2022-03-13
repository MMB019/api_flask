from utils import queryBuilder as qb
import requests
import json




def get_acled_data(argument=""):
    donnes=requests.get("https://api.acleddata.com/acled/read?key=a0kZXycyBAkilS3e23wW&email=morgan.hanin@triggersreports.com"+argument).json()
    #data=json.dumps(donnes)
    return donnes

def insert_acled_data(arg):
    data=get_acled_data(arg)
    for i in range(len(data)-1):
        test_data=data['data'][i].values()
        print("insertion des données encours 1...")
        qb.ingestion_data(list(test_data))




if __name__=="__main__":
    print(donnes)
