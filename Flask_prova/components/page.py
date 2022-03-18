import json


class Page:

    title = ''
    header = ''
    content = ''
    footer = ''

    def __init__(self):
        self.title = "Titolo Pagina"
        self.header = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"></head><body class="container">'
        self.content = ''
        self.footer = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script></body></html>'
        self.add_navigator()

    def draw(self):
        return self.header + self.content + self.footer

    def add_contante(self):
        f = Form()
        self.content += f.draw()

    def add_component(self,component):
        self.content += component.draw()


class Form:

    header = '<form method="POST" action="" style="margin-top: 50px;">'
    content = ''
    post_content = '</form>'


    def __init__(self,item_list):
        for item in item_list:
            email = '<div class="mb-3"><label class="form-label">Email address</label><input type="email" class="form-control">'
            password = '<div class="mb-3"><label class="form-label">Password</label><input type="password" class="form-control"></div>'
            self.content += email + password

    def draw(self):
        return self.before + self.title_navbar + self.pre_content + self.content + self.post_content

