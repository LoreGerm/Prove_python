from flask import Flask
from components.page import Page
app = Flask(__name__)



@app.route("/servizi")
def servizi_page():
    #return "<p>Hello, World!</p>"
    p = Page()
    #p.add_component(BadgePositioned('Servizi','12'))
    return p.draw()


if __name__ == '__main__':
    app.run()