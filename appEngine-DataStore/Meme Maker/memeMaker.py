
import webapp2
import json
from google.appengine.api import urlfetch
pics = []
class MainPage(webapp2.RequestHandler):

    def get(self):
        text = self.request.get('text')
        self.response.headers['Content-Type'] = 'text/html'
        # api_string = 'https://api.imgflip.com/get_memes'
        # r = urlfetch.fetch(api_string)
        # j = json.loads(r.content)
        # for meme in j['data']['memes']:
        #     pics.append(meme['url'])
        # self.response.write('<img src={}>'.format(pics[0]))

        api_string = 'https://api.imgflip.com/caption_image?template_id={id}&username={u}&password={p}&text0={t0}&text1={t1}'
        new_string = api_string.format(id=102156234, u='cssilab', p='cssipass', t0='text0', t1='text1')
        r = urlfetch.fetch(new_string)
        j = json.loads(r.content)
        self.response.write('<img src={}>'.format(j['data']['url']))


app = webapp2.WSGIApplication([
    # ('/save', SavePage),
    # ('/random', RandomPage),
    ('/.*', MainPage),
], debug=True)
