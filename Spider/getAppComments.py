from Module import COMMENT_URL,session
from Module.modules.comment import Comment
from Module.modules.app import App
import requests
import json

def getAndSaveAppComments(app:App):

    for i in range(1,10):
        res_json = requests.get(url=COMMENT_URL % (i,app.id))
        js = json.loads(res_json.text)
        review_list = js['feed']['entry']
        for r in review_list[1:]:
            one = Comment()
            one.app_id = app.id
            one.app = app
            one.author_name = r['author']['name']['label']
            one.title = r['title']['label']
            one.rate_level = int(r['im:rating']['label'])
            one.content = r['content']['label']

            try:
                session.add(one)
                session.commit()
                print("App[%d] comment[%d] saved successfully." % (app.id,one.comment_id))
            except Exception as e:
                print(e)

