from utils import db_connector
from Model.AcledModelData import Acled
from sqlalchemy import desc
# Press the green button in the gutter to run the script.


def ingestion_data(d,app):
    db=db_connector.get_db(app)

    acled=Acled(data_id=d[0],iso=d[1],event_id_cnty=d[2],event_id_no_cnty=d[3],event_date=d[4],year=d[5],
    time_precision=d[6],event_type=d[7],sub_event_type=d[8],actor1=d[9],assoc_actor_1=d[10],inter1=d[11],actor2=[12],
    assoc_actor_2=d[13],inter2=d[14],interaction=d[15],region=d[16],country=d[17],admin1=d[18],
    admin2=d[19],admin3=d[20],location=d[21],latitude=d[22],longitude=d[23],geo_precision=d[24],
    source=d[25],source_scale=d[26],notes=d[27],fatalities=d[28],timestamp=d[29],iso3=d[30]
    )

    print(f"donner ingere {acled} ")
    db.session.add(acled)
    db.session.commit()
    print("insertion reussi a success!!!!")

def select_all(app):
     db=db_connector.get_db(app)
     return db.session.query(Acled.country,db.func.count(Acled.country)).group_by(Acled.country).all()

#get data by country
def group_by_ev_cnty(app):
    db=db_connector.get_db(app)
    return db.session.query(Acled.country,db.func.count(Acled.event_type)).group_by(Acled.country).order_by(desc(db.func.count(Acled.event_type))).all()

#get data by admin1
def group_by_ev_ad1(app):
    db=db_connector.get_db(app)
    return db.session.query(Acled.admin1,db.func.count(Acled.event_type)).group_by(Acled.admin1).order_by(desc(db.func.count(Acled.event_type))).all()

#get data by admin2
def group_by_ev_ad2(app):
    db=db_connector.get_db(app)
    return db.session.query(Acled.admin2,db.func.count(Acled.event_type)).group_by(Acled.admin2).order_by(desc(db.func.count(Acled.event_type))).all()

#get data by location
def group_by_ev_loc(app):
    db=db_connector.get_db(app)
    return db.session.query(Acled.location,db.func.count(Acled.event_type)).group_by(Acled.location).order_by(desc(db.func.count(Acled.event_type))).all()

#get data by event type
def group_by_ev_cnty(app):
    db=db_connector.get_db(app)
    return db.session.query(Acled.country,db.func.count(Acled.event_type)).group_by(Acled.country).order_by(desc(db.func.count(Acled.event_type))).all()

#get data by event type
def group_by_ev_evType(app):
    db=db_connector.get_db(app)
    return db.session.query(Acled.event_type,db.func.count(Acled.event_type)).group_by(Acled.event_type).order_by(desc(db.func.count(Acled.event_type))).all()

def group_by_actor1(app):
    db=db_connector.get_db(app)
    return db.session.query(Acled.actor1,db.func.count(Acled.actor1)).group_by(Acled.actor1).order_by(desc(db.func.count(Acled.actor1))).all()

def group_by_actor2(app):
    db=db_connector.get_db(app)
    return db.session.query(Acled.actor2,db.func.count(Acled.actor2)).group_by(Acled.actor2).order_by(desc(db.func.count(Acled.actor2))).all()

#--------------------------------query for country------------------------------------------------

#total event by country filter by country name
def total_event_by_country_name(app,arg):
    db=db_connector.get_db(app)
    return db.session.query(Acled.country,db.func.count(Acled.event_type)).group_by(Acled.country).filter_by(country=arg).all()

#get data by admin1 of country
def group_by_ev_ad1_country_name(app,arg):
    db=db_connector.get_db(app)
    return db.session.query(Acled.admin1,db.func.count(Acled.event_type)).group_by(Acled.admin1,Acled.country).filter_by(country=arg).all()

#get data by admin2 of country
def group_by_ev_ad2_country_name(app,arg):
    db=db_connector.get_db(app)
    return db.session.query(Acled.admin2,db.func.count(Acled.event_type)).group_by(Acled.admin2,Acled.country).filter_by(country=arg).all()

#get data by location of country
def group_by_ev_loc_country_name(app,arg):
    db=db_connector.get_db(app)
    return db.session.query(Acled.location,db.func.count(Acled.event_type)).group_by(Acled.location,Acled.country).filter_by(country=arg).all()
#get data by event_type of country
def group_by_ev_evType_country_name(app,arg):
    db=db_connector.get_db(app)
    return db.session.query(Acled.event_type,db.func.count(Acled.event_type)).group_by(Acled.event_type,Acled.country).filter_by(country=arg).all()

#get data by country name
def group_by_actor1_country_name(app,arg):
    db=db_connector.get_db(app)
    return db.session.query(Acled.actor1,db.func.count(Acled.actor1)).group_by(Acled.actor1,Acled.country).filter_by(country=arg).all()

def group_by_actor2_country_name(app,arg):
    db=db_connector.get_db(app)
    return db.session.query(Acled.actor2,db.func.count(Acled.actor2)).group_by(Acled.actor2,Acled.country).filter_by(country=arg).all()