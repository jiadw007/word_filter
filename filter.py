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
import json
class Filter(webapp2.RequestHandler):

    """Word filter class"""

    #default wordList
    wordList = ["maverick","ranger","rocket","chicago","bear","wizard","seattle",
                "atlanta","miami","austin","boston","pittsburgh","heat","saint",
                "hawk","king"]
    defaultList = ["maverick","ranger","rocket","chicago","bear","wizard","seattle",
                "atlanta","miami","austin","boston","pittsburgh","heat","saint",
                "hawk","king"]
    def post(self):

        """ Post method to filtering """
        #set wordList, if user set
        list = self.request.get('list')
        if len(list) != 0:
            self.__class__.wordList = list.split(" ")
        else:
            self.__class__.wordList = self.__class__.defaultList
        #get user input text
        text = self.request.get('param')
        textList = str(text).split(" ")
        result = []
        for word in textList:

            length = len(word)
            if word in self.__class__.wordList: #if word is in wordList REPLACE WORD WITH *
                result.append('*' * length)
            else:   #if word is not in wordList, splice word to check whether the substring in the word is in the wordList
                start = 1
                while start < length:
                    front_part = word[:start]
                    end_part = word[start:]
                    #if two parts in the word are in the wordList, REPLACE WORD WITH *
                    if front_part in self.__class__.wordList and end_part in self.__class__.wordList:
                        result.append('*' * length)
                        break
                    start = start + 1
                #if all substring combination are not in the wordList, append word to result list
                if start == length:
                    result.append(word)
        #construct result word List
        word = " ".join(result)
        output = {'list': " ".join(self.__class__.wordList), 'result' : word}
        output = json.dumps(output)
        self.response.out.write(output)

        ##self.response.out.write(str(text) + " Hello World!")


application = webapp2.WSGIApplication([("/filter", Filter)],debug = True)