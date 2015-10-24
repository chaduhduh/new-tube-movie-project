def open_template(template_name):
    VIEW_PATH = "./views/"
    template_name = template_name
    template_path = VIEW_PATH + template_name + ".html"
    rtnstr = open(template_path, 'r').read()
    return rtnstr

def fill_template(template_name, args):
	rtnstr = ''
	args = args
	template = open_template(template_name)
	if(args):
		rtnstr = template.format(args)
	else:
		rtnstr = template
	return rtnstr


