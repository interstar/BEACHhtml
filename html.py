
# HTML library
# basic level 

def tag(name,x,*argv) :
	if x is None :
		return u"<"+name+u"/>"
	if argv != (None,) : 
		inside = u''.join(argv)
	else :
		inside = u''
	if isinstance(x,dict) :
		# we're passing a dictionary of attributes for the tag
		s = u"<%s " % name 
		s = s + ' '.join(['%s="%s"'%(k,v) for (k,v) in x.iteritems()])
		s = s +u">%s</%s>" % (inside,name)
		return s

	# or there are no attributes, just inner
	return u"<%s>%s%s</%s>"% (name,x,inside,name)


tags = ['html','head','body','script','p','div','table','tr','th','td',
	'ul','ol','li','dt','dd','h1','h2','h3','h4','h5','h6', 'style','b',
	'pre','hr']

loc = locals()
def setit(loc,t) :
	loc[t] = lambda x=None,*argv : tag(t,x,*argv)

for t in tags :
	setit(loc,t)

# Use like this 
html(
	head(),
	body(),
)

def p_ul(x,ys=None) :
    """Turn a python list into a UL list tag"""
    if ys : 
        if isinstance(x,dict) :
            ys = [li(y) for y in ys]
            return ul(x,u''.join(ys))
    return ul(u''.join([li(ox) for ox in x]))
        

def p_table(x,ys=None) :
    """Turn a nested python list into a table tag"""
    tab = x
    if ys : 
        if isinstance(x,dict) :
            tab = ys
            
    s = u""

    for row in tab:
        s += u"""
<tr>"""+u''.join([td(i) for i in row])+u"""</tr>"""

    if ys :
        return table(x,s)
    else :
        return table(s)             




