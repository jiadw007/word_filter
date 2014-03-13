#-------------------------------------------------------------------------------
# Name:        filter.py
# Purpose:     word filter
# Author:      Dawei Jia
#
# Created:     03/12/2014
# Copyright:   (c) DaweiJia 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import webapp2

class Filter(webapp2.RequestHandler):

    """Word filter class"""

    #default wordList


    def post(self):

        """ Post method to filtering """
        text = self.request.get('param')
        self.response.out.write(str(text) + " Hello World!")


application = webapp2.WSGIApplication([("/filter", Filter)],debug = True)