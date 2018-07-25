
import webapp2
import json
import jinja2
from google.appengine.api import urlfetch
import random

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)

pics = []
imgLink = ''
get_meme_url = 'https://api.imgflip.com/get_memes'
random_meme = 61579
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
        #self.response.write('<img src={}>'.format(j['data']['url']))
        imgLink = j['data']['url']

class MemePage(webapp2.RequestHandler):
    def get(self):
        global random_meme
        template = template_env.get_template('Templates/format.html')
        self.response.write(template.render())

        result = urlfetch.fetch(get_meme_url)
        memes = json.loads(result.content)
        random_meme = random.choice(memes['data']['memes'])['id']

    def post(self):
        text0 = self.request.get('use-first-line')
        text1 = self.request.get('use-second-line')
        type = self.request.get('meme-type')

class MemeResult(webapp2.RequestHandler):
    def post(self):
        global random_meme
        text0 = self.request.get('use-first-line')
        text1 = self.request.get('use-second-line')
        type = self.request.get('meme-type')
        template = template_env.get_template('Templates/meme-result.html')
        meme_info = {'type': type,
                  'text0': text0,
                  'text1': text1}

        result = urlfetch.fetch(get_meme_url)
        memes = json.loads(result.content)
        
        self.response.write(template.render(meme_info))

        random_meme = type
        api_string = 'https://api.imgflip.com/caption_image?template_id={id}&username={u}&password={p}&text0={t0}&text1={t1}'
        new_string = api_string.format(id=random_meme, u='cssilab', p='cssipass', t0=text0, t1=text1)
        r = urlfetch.fetch(new_string)
        j = json.loads(r.content)
        self.response.write('<img src={}>'.format(j['data']['url']))

# class RecipeBrowser(webapp2.RequestHandler):
#     def get(self):
#         template = template_env.get_template('Templates/recipes.html')
#         recipe = {'ingrediants': ['cottage cheese', 'pineappe'],
#                   'cuisine': 'indonesian'}
#         self.response.write(template.render(recipe))

app = webapp2.WSGIApplication([
    # ('/recipe', RecipeBrowser),
    ('/memetemp', MemePage),
    ('/MemeResult', MemeResult),
    ('/.*', MainPage),
], debug=True)
