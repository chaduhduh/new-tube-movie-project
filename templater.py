def open_template(template_name):
    VIEW_PATH = "./views/"
    template_name = template_name
    template_path = VIEW_PATH + template_name + ".html"
    rtnstr = open(template_path, 'r').read()
    return rtnstr

