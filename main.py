from extractor import extractFromAcled
from utils import queryBuilder as qb
from common import appName as ap
import json

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
app=ap.get_app()

@app.route("/")
def select_alld():
    data=json.dumps(dict(qb.select_all(app)))
    return data

@app.route("/totalEventByCountry")
def total_event_by_country():
    data=json.dumps(dict(qb.group_by_ev_cnty(app)))
    return data

@app.route("/totalEventByAdmin1")
def total_event_by_admin1():
    data=json.dumps(dict(qb.group_by_ev_ad1(app)))
    return data

@app.route("/totalEventByAdmin2")
def total_event_by_admin2():
    data=json.dumps(dict(qb.group_by_ev_ad2(app)))
    return data

@app.route("/totalEventByLocation")
def total_event_by_location():
    data=json.dumps(dict(qb.group_by_ev_loc(app)))
    return data

@app.route("/totalEventByEventType")
def total_event_by_event_type():
    data=json.dumps(dict(qb.group_by_ev_evType(app)))
    return data

@app.route("/totalByActor1")
def total_by_actor1():
    data=json.dumps(dict(qb.group_by_actor1(app)))
    return data
@app.route("/totalByActor2")
def total_by_actor2():
    data=json.dumps(dict(qb.group_by_actor2(app)))
    return data
#--------------------------------filter by country-------------------------------------

@app.route("/totalEventByCountryName/<country>")
def total_event_by_country_name(country):
    data=json.dumps(dict(qb.total_event_by_country_name(app,country)))
    return data

@app.route("/totalEventByAdmin1CountryName/<country>")
def total_event_by_admin1_country_name(country):
    data=json.dumps(dict(qb.group_by_ev_ad1_country_name(app,country)))
    return data

@app.route("/totalEventByAdmin2CountryName/<country>")
def total_event_by_admin2_country_name(country):
    data=json.dumps(dict(qb.group_by_ev_ad2_country_name(app,country)))
    return data

@app.route("/totalEventByLocationCountryName/<country>")
def total_event_by_location_country_name(country):
    data=json.dumps(dict(qb.group_by_ev_loc_country_name(app,country)))
    return data

@app.route("/totalEventByEventTypeCountryName/<country>")
def total_event_by_event_type_country_name(country):
    data=json.dumps(dict(qb.group_by_ev_evType_country_name(app,country)))
    return data

@app.route("/totalByActor1CountryName/<country>")
def total_by_actor1_country_name(country):
    data=json.dumps(dict(qb.group_by_actor1_country_name(app,country)))
    return data

@app.route("/totalByActor2CountryName/<country>")
def total_by_actor2_country_name(country):
    data=json.dumps(dict(qb.group_by_actor2_country_name(app,country)))
    return data

if __name__ == "__main__":
    app.run()