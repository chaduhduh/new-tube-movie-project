""" Templater - a Templating Module.
	
	Simple module for opening and populating html
	templates.

	attributes: 
	VIEW_PATH: path to views folder

	functions:
	open_template: Takes param 'template_name' (without .html extension)-
	and returns html template as string.
	fill_template: Takes params 'template_name','args'. opens template-
	file of 'template_name' and fills template data using args param. Warning:
	templates requesting an undefined data key will result in an error in the 
	current build.
	Template Example: 
		args = { "variableName" : "variableValue" }
		templateToFill = '<p>This is a variable {0[variableName]}</p>'
		filledTemplate = fill_template(templateToFill, args); 
"""

def open_template(template_name):
	""" returns html file as string """
	VIEW_PATH = "./views/"
	template_name = template_name
	template_path = VIEW_PATH + template_name + ".html"
	rtnstr = open(template_path, 'r').read()
	return rtnstr

def fill_template(template_name, args):
	""" fills html file with data aka args """
	rtnstr = ''
	args = args
	template = open_template(template_name)
	if(args):
		rtnstr = template.format(args)
	else:
		rtnstr = template
	return rtnstr


