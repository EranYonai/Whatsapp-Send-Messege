import os.path
from enum import IntEnum

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


class SurfingClass_SurColors(IntEnum):
    tangerine = 6
    basil = 10
    sage = 2
    peacock = 6
    grape = 3
    flamingo = 4

    # 0 = tomato
    # 1 = lavender
    # 2 = marvel / מרבה
    # 3 = grape
    # 4 = flamingo
    # 5 = banana
    # 6 = tangerine
    # 7 = peacock
    # 8 = graft
    # 9 = blueberries
    # 10 = basil


surfingClass = {
    "שיעור גלישת גלים": int(SurfingClass_SurColors.grape),
    "שיעור גלישת ווינג": int(SurfingClass_SurColors.peacock),
    "שיעור גלישת רוח": int(SurfingClass_SurColors.sage),
    "שיעור סאפ": int(SurfingClass_SurColors.tangerine),
    "שיעור קייט סרפינג": int(SurfingClass_SurColors.basil),
    "שיעור שייט על קטמרן": int(SurfingClass_SurColors.flamingo),
    "השכרת קטמרן": int(SurfingClass_SurColors.flamingo)
}


def GetEverythingTogether(typeOfClass: str, name: str, phoneNum: str, personAmount: str, classNum: str,):
    totalName = typeOfClass + " " + classNum + " " + personAmount

    namePhone = name + " - " + phoneNum
    totalName = namePhone + " - " + totalName + " - יש לתאם מדריך"
    return totalName


def FixDate(date: str):
    if(date.find("/") == False):
        return date
    tempDate = date.split("/")
    newDate = ""
    for d in tempDate:
        newDate = d + "-" + newDate
    newDate = newDate[0:len(newDate) - 1]
    return newDate


def FixTime(time):
    tempTime = time.split(":")
    newTime = ""
    if len(tempTime) <= 2:
        for t in tempTime:
            if (len(t) == 1):
                t = "0" + t
            elif (len(t) == 0):
                t = "00"
            newTime = newTime + t + ":"
        newTime += "00"
    return newTime


def Add1HourToTime(time):
    # may be useful in the future
    tempTime = time.split(":")
    newTime = ""
    tempTime[0] = str(int(tempTime[0]) + 1)
    if (int(tempTime[0]) == 25):
        tempTime[0] = "1"

    if (10 > len(tempTime[0]) >= 0):
        tempTime[0] = "0" + tempTime[0]
    for t in tempTime:
        newTime = newTime + t + ":"
    newTime = newTime[0:len(newTime) - 1]
    return newTime


def CreateTypeOfClassInCalendar(className: str, totalName: str, date: str, timeStart: str, timeEnd: str):
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json")  # , SCOPES

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write((creds.to_json()))

    try:
        service = build("calendar", "v3", credentials=creds)

        classColor = surfingClass[className]

        date = FixDate(date)
        timeStart = FixTime(timeStart)
        dateTimeStart = date + "T" + timeStart + "+02:00"
        timeEnd = FixTime(timeEnd)
        dateTimeEnd = date + "T" + timeEnd + "+02:00"

        event = {
            "summary": totalName,  # summary is the name of the event
            "Location": "Somewhere Online",
            "description": "",
            "colorId": classColor,  # color of the event
            "start": {
                "dateTime": dateTimeStart,
                "timeZone": "GMT+2"  # there is not a time zone for israel
            },
            "end": {
                "dateTime": dateTimeEnd,
                "timeZone": "GMT+2"  # there is not a time zone for israel
            }  # ,
            # "recurrence": [
            #    "RRULE:FREQ=DAILY;COUNT=3" # how to do recurrence daily; for 3 times before stopping
            # ],
            # "attendees": [
            #    {"email": "Lioraran2006@gmail.com"}, # you can invite other people to the event
            # ]
        }
        calendarEventsId = 'ab3b86c5930edde918fffeb3da6f9b656471d0c5d6d64e652f534d31f002d26a@group.calendar.google.com'
        service.events().insert(calendarId=calendarEventsId, body=event).execute()
    except HttpError as error:
        print("An error occurred:", error)


# Example of a function call
#CreateTypeOfClassInCalendar("שיעור גלישת גלים", "עפרי שיפמן - 052-8082047", "פרטי", "נסיון", "14/12/2023", "10:00", "12:00")

# GetEverythingTogether("שיעור גלישת גלים", "ליאור ארן", "052-8082047", "פרטי", "נסיון")

# Gets 10 first items on calendar
# now = dt.datetime.now().isoformat() + "Z"
#
#         event_result = service.events().list(
#             calendarId="primary",
#             timeMin=now,
#             maxResults=10,
#             singleEvents=True,
#             orderBy="startTime"
#             )\
#             .execute()
#         events = event_result.get("items", [])
#
#         if not events:
#             print("No up coming events found!")
#             return
#         for event in events:
#             start = event["start"].get("dateTime", event["start"].get("date"))
#             print(start, event["summary"])
