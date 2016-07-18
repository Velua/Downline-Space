import re




def first_number(datstring):
	match = re.search(r'\d', datstring)

	return match


bby = first_number("fwjeiojfo333")
print dir(bby)