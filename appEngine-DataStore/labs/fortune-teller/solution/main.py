#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import random
from movie import Movie
from google.appengine.ext import ndb

def get_fortune():
    fortune_list=['Tomorrow, you will meet a life-changing new friend.',
                  'Fame and Instagram followers are headed your way.',
                  'On the Tuesday after next, an odd meeting will lead to a new opportunity.',
                  'Despite dry skies, bring an umbrella tomorrow.',
                  'A thrilling time is in your immediate future.',
                  'Someone has Googled you recently.',
                  'Stay alert. You will be part of a rescue mission.',
                  'You will beat Watson in a game of Jeopardy. Start studying though']
    return(random.choice(fortune_list))


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/fortune_welcome.html")
        self.response.write(start_template.render())

    def post(self):
        random_fortune = get_fortune()
        astro_sign = self.request.get('user_astrological_sign')
        my_dict={'the_fortune':random_fortune, 'the_astro_sign':astro_sign}
        end_template=jinja_current_directory.get_template("templates/fortune_results.html")
        #astro_sign = request.form.get('user_astrological_sign')
        self.response.write(end_template.render(my_dict))

class DataFormHandler(webapp2.RequestHandler):
    def get(self):
        data = {'movies': Movie.query().fetch()}
        start_template=jinja_current_directory.get_template("templates/formtemp.html")
        self.response.write(start_template.render(data))

    def post(self):
        movie_title = self.request.get('title')
        movie_runtime = float(self.request.get('runtime'))
        movie_rating = float(self.request.get('rating'))
        movie = Movie(title = movie_title, runtime = movie_runtime, rating = movie_rating)
        movie.put()
        self.get()

        # q = Movie.query()
        # movies = q.fetch()
        # self.response.out.write('<br> <br>')
        # for movie in movies:
        #     self.response.out.write("{m} <br>".format(m=movie.title))
class DataUpdateHandler(webapp2.RequestHandler):
    def post(self):
        movie_id = self.request.get("movie_id")
        change = Movie.get_by_id(int(movie_id))
        change.title = str(self.request.get("updatevalue"))
        change.put()

class DataDeleteHandler(webapp2.RequestHandler):
    def post(self):
        movie_id = self.request.get("movie_id")
        movie_to_delete = Movie.get_by_id(int(movie_id))
        movie_to_delete.key.delete()

class TestDataHandler(webapp2.RequestHandler):
    def get(self):
        test_movie = Movie(title = 'Bill & Ted', runtime = 90, rating = 8.9)
        test_movie.put()

app = webapp2.WSGIApplication([
    ('/', FortuneHandler),
    ('/form', DataFormHandler),
    ('/test', TestDataHandler),
    ('/delete', DataDeleteHandler),
    ('/update', DataUpdateHandler),
], debug=True)
