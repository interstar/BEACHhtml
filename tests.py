# Unit tests

import unittest
from html import html, head, body, p, div, table, th, td, tr, ul, ol, li, dd, dt, h1, h2, h3, h4, h5, h6

class TestHtml(unittest.TestCase) :
    def test(self) :
        self.assertEquals(p('hello world'),"<p>hello world</p>")
        self.assertEquals(div('hello world'),"<div>hello world</div>")
        self.assertEquals(div({'class':'myclass','id':'myd'},'hello world'),
                              """<div class="myclass" id="myd">hello world</div>""")

        self.assertEquals(div('a','b'),'<div>ab</div>')

        self.assertEquals(p(),'<p/>')

        self.assertEquals(html(
            head(),
            body(
                h2("Header"),
                p('para1'),
                p('para2')
                )),
            """<html><head/><body><h2>Header</h2><p>para1</p><p>para2</p></body></html>""")

if __name__ == '__main__' :
    unittest.main()
    
