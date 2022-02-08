import re
from course import db
from course.models import *
from matplotlib import colors
from flask import flash


def format_tel(phone):
    if phone != "":
        clean_phone = re.sub("[^0-9]+", "", phone)
        formatted_phone = (
            re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1-", "%d" % int(clean_phone[:-1]))
            + clean_phone[-1]
        )
        return formatted_phone
    else:
        return ""


def populate_states():
    states = [
        ["Alabama", "AL"],
        ["Alaska", "AK"],
        ["Arizona", "AZ"],
        ["Arkansas", "AR"],
        ["California", "CA"],
        ["Colorado", "CO"],
        ["Connecticut", "CT"],
        ["Delaware", "DE"],
        ["District Of Columbia", "DC"],
        ["Florida", "FL"],
        ["Georgia", "GA"],
        ["Hawaii", "HI"],
        ["Idaho", "ID"],
        ["Illinois", "IL"],
        ["Indiana", "IN"],
        ["Iowa", "IA"],
        ["Kansas", "KS"],
        ["Kentucky", "KY"],
        ["Louisiana", "LA"],
        ["Maine", "ME"],
        ["Maryland", "MD"],
        ["Massachusetts", "MA"],
        ["Michigan", "MI"],
        ["Minnesota", "MN"],
        ["Mississippi", "MS"],
        ["Missouri", "MO"],
        ["Montana", "MT"],
        ["Nebraska", "NE"],
        ["Nevada", "NV"],
        ["New Hampshire", "NH"],
        ["New Jersey", "NJ"],
        ["New Mexico", "NM"],
        ["New York", "NY"],
        ["North Carolina", "NC"],
        ["North Dakota", "ND"],
        ["Ohio", "OH"],
        ["Oklahoma", "OK"],
        ["Oregon", "OR"],
        ["Pennsylvania", "PA"],
        ["Rhode Island", "RI"],
        ["South Carolina", "SC"],
        ["South Dakota", "SD"],
        ["Tennessee", "TN"],
        ["Texas", "TX"],
        ["Utah", "UT"],
        ["Vermont", "VT"],
        ["Virginia", "VA"],
        ["Washington", "WA"],
        ["West Virginia", "WV"],
        ["Wisconsin", "WI"],
        ["Wyoming", "WY"],
    ]

    if len(states) != States.query.count():
        for st in states:
            abr = st[1]
            state = st[0]

            cnt = States.query.filter(States.abr == abr).count()
            if cnt == 0:
                new = States(abr=abr, state=state)
                db.session.add(new)
                db.session.commit()


def shorten_url(longurl):
    import requests
    import json

    url = "https://api-ssl.bitly.com/v4/shorten"
    dbtoken = db.session.query(apitoken).filter(apitoken.name == "bitley").first().token

    payload = json.dumps({"domain": "bit.ly", "long_url": f"{longurl}"})
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {dbtoken}"}

    response = requests.request("POST", url, headers=headers, data=payload)

    fulljson = json.loads(response.text)
    link = fulljson["link"]
    return link