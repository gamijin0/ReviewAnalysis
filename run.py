from Spider.getAppComments import getAndSaveAppComments
from Spider.getAppID import getAppID_most_popular
from Spider.saveAppInfo import saveAppInfo


from Module import session
from Module.modules.app import App,Comment

if(__name__=="__main__"):


    # id_list = getAppID_most_popular()
    #
    # for id in id_list:
    #     try:
    #
    #         if(session.query(App).filter(App.id==int(id)).count()== 0):
    #             saveAppInfo(ID=id)
    #         else:
    #             print("app with ID[%d] has existed." % int(id))
    #     except Exception as e:
    #         print(e)


    app_list = session.query(App).all()[::-1]
    print(len(app_list))
    for a in app_list:
        try:
            if (session.query(Comment).filter(Comment.app_id == a.id).count() == 0):
                getAndSaveAppComments(a)
            else:
                print("comments of  app with ID[%d] has existed." % a.id)
        except Exception as e:
            print(e)