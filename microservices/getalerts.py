from pprint import pprint
from gdacs.api import GDACSAPIReader
from datetime import datetime, timedelta
from time import sleep
from amqp_helper import Rabbitmq
from datetime import datetime

import json
import dateparser
import pika


def get_alert():
    client = GDACSAPIReader()
    events = client.latest_events()
    events_dict = events.dict()
    # pprint(events_dict)
    events = {}
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
        _isToday = _from.date() == _now.date()-timedelta(days=1)
        _alertlevel = i['properties']['alertlevel']
        _alertscore = i['properties']['alertscore']

        event = {
            'name':_name,
            'location':_geometry,
            'description': _description,
            'type':_eventtype,
            'country':_country,
            'country_short':_country_short,
            'from':_from.strftime("%d/%m/%Y %H:%M"),
            'to':_to.strftime("%d/%m/%Y %H:%M"),
            'isHappening': _isHappening,
            'isToday': _isToday,
            'alertlevel':_alertlevel,
            'alertscore':_alertscore
        }

        if _isToday:
            pprint(event)
        if events.get(_name,False):
            if _name in events:
                events[_name].append(event)
        else:
            events[_name] = [event]
    
    return events

def main():
    rabbitmq = Rabbitmq()
    while True:
        alert = get_alert()
        rabbitmq.publish_message(json.dumps(alert),'gdac.alert')
        sleep(10)
    
if __name__ == "__main__":
    main()