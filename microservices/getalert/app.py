from pprint import pprint
from gdacs.api import GDACSAPIReader
from datetime import datetime, timedelta
from time import sleep
from amqp_helper import Rabbitmq
from datetime import datetime, timedelta

import json
import dateparser
import servicehelper

def get_alert():
    client = GDACSAPIReader()
    events = client.latest_events()
    events_dict = events.dict()

    events = []
    for i in events_dict['features']:

        _from = dateparser.parse(i['properties']['fromdate'].replace('T',' '))
        _to = dateparser.parse(i['properties']['todate'].replace('T',' '))
        _now = datetime.now()-timedelta(hours=8)
        _name = i['properties']['name']
        _description = i['properties']['description']
        _geometry = i['geometry']
        _eventtype = i['properties']['eventtype']
        _country = i['properties']['country']
        _country_short = i['properties']['iso3']
        _isHappening = _from <= _now <= _to
        _isToday = _now-timedelta(hours=16) <= _to
        _alertlevel = i['properties']['alertlevel']
        _alertscore = i['properties']['alertscore']

        event = {
            'name':_name,
            'location':_geometry,
            'description': _description,
            'type':_eventtype,
            'country':_country,
            'country_short':_country_short,
            'from':_from.strftime("%Y/%m/%d %H:%M:%S"),
            'to':_to.strftime("%Y/%m/%d %H:%M:%S"),
            'isHappening': _isHappening,
            'isToday': _isToday,
            'alertlevel':_alertlevel,
            'alertscore':_alertscore
        }

        events.append(event)
    
    return events

def main():
    while servicehelper.isServiceReady("createdisaster"):
        sleep(1)
    alert_list = []
    rabbitmq = Rabbitmq()
    rabbitmq._setup()
    print('------------- Get alerts running -------------')
    servicehelper.serviceIsReady("getalert")
    while True:
        sleep(5)
        try:
            alerts = get_alert()
            new_alerts = [alert for alert in alerts if alert not in alert_list]
            print(new_alerts)
            if len(new_alerts)>0:
                alert_list+=new_alerts
                rabbitmq.publish_message(json.dumps(new_alerts),'gdac.alert')
        except Exception as e:
            print(e)
    
if __name__ == "__main__":
    main()