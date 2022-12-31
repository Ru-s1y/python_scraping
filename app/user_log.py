from datetime import datetime

class user_log:

    def save(response):
        now = datetime.now()
        path = './logs/' + now.strftime("%Y_%m_%d_%H_%M_%S") + '.html'

        f = open(path, 'w')
        f.write(response.text)
        f.close()
