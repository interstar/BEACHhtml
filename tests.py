# Unit tests

import unittest
from html import html, head, body, p, div, table, th, td, tr, ul, ol, li, dd, dt, h1, h2, h3, h4, h5, h6
from html import p_ul, p_table, inject, file_inject, Selector, breaks

class TestHtml(unittest.TestCase) :
    def test(self) :
        self.assertEquals(breaks("hello world"),"\nhello world\n")
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

    def testList(self) :
        xs = [1,2,"three"]
        self.assertEquals(p_ul(xs),"""<ul>
<li>1</li>
<li>2</li>
<li>three</li>
</ul>""")
        self.assertEquals(p_ul({"class":"myList"},xs),"""<ul class="myList">
<li>1</li>
<li>2</li>
<li>three</li>
</ul>""")

    def testTable(self) :
        xs = [["oranges","apples","lemons"],[43,65,54]]
        self.assertEquals(p_table(xs),"""<table>
<tr><td>oranges</td><td>apples</td><td>lemons</td></tr>
<tr><td>43</td><td>65</td><td>54</td></tr></table>""")
        self.assertEquals(p_table({"style":"border-width:3px;"},xs),u"""<table style="border-width:3px;">
<tr><td>oranges</td><td>apples</td><td>lemons</td></tr>
<tr><td>43</td><td>65</td><td>54</td></tr></table>""")

    def testTemplate(self) :
        tpl = "Hello $name"        
        self.assertEquals(inject(tpl,name="world"),"Hello world")
        
    def testTemplateFile(self) :
        fName = "test.tpl"
        s = file_inject(fName,adj="teenage",noun="America")
        self.assertEquals(s,"""Hello teenage America!
Another Green World
""")
        
    def testSelected(self) :
        sel = Selector(1)
        xs = [sel(x,lambda x : 99) for x in [0,1,2]]
        self.assertEquals(xs,[0,99,2])
        
        sel = Selector(3)
        xs = [sel(x, lambda x : div(x)) for x in [0,1,2,3,4,5,6]]
        self.assertEquals(xs,[0,1,2,"<div>3</div>",4,5,6])
        
        

if __name__ == '__main__' :
    unittest.main()
    
