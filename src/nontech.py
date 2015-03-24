__author__ = 'alay'

from src.basehandler import BaseHandler
from src.handledoc import HandleDoc


class NonTechHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print(self.request)
        slugs = str(self.request.uri).lstrip('/').rstrip('/').split('/')
        slugs.remove('api')
        slugs.remove('nontech')
        if str(slugs) == "['all']":
            db = HandleDoc('non-tech')
            db.get_query()
            db.run_query()
            self.message = list()
            if db.doc is not None:
                for doc in db.doc:
                    del doc['value']['_id']
                    del doc['value']['_rev']
                    self.message.append(doc['value'])
                self.send_error(200)
            else:
                self.send_error(400)
        else:
            slugs = str(slugs).lstrip("['").rstrip("']")
            query_dict = dict(name=slugs)
            db = HandleDoc('non-tech', query_dict)
            db.get_query()
            db.run_query()
            if db.doc is not None:
                self.message = db.doc
                self.send_error(200)
            else:
                self.send_error(400)