import sys
from dashboardServer import create_app

reload(sys)
sys.setdefaultencoding('utf-8')

app = create_app()

# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
if __name__ == '__main__':
    app.run()
