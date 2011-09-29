
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
