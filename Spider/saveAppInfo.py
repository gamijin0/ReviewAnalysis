import requests
from Module import COMMENT_URL,APPINFO_URL,session
from Module.modules.app import App
import json


def saveAppInfo(ID:int):

    res = requests.get(APPINFO_URL % (ID))
    results = json.loads(res.text)['results'][0]
    one = App()
    one.id = results['trackId']
    one.name = results['trackCensoredName']
    one.fileSizeBytes = int(results['fileSizeBytes'])
    one.version = results['version']
    one.description = str(results['description'])
    one.releaseDate = results['currentVersionReleaseDate']
    if("formattedPrice" in results):
        one.formattedPrice = results['formattedPrice']
    one.minimumOsVersion = results['minimumOsVersion']
    one.averageUserRating = float(results['averageUserRating'])
    one.userRatingCount = int(results['userRatingCount'])

    session.add(one)
    session.commit()
    print("One App's info saved successfully.")