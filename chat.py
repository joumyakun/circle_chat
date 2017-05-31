import tornado.ioloop
import tornado.web
import tornado.websocket
import os

class ChatHandler(tornado.websocket.WebSocketHandler):
    clients = []

    def open(self):
        print("connect")
        if self not in ChatHandler.clients:
            ChatHandler.clients.append(self)

    def on_message(self, message):
        print(message)
        for c in ChatHandler.clients:
            c.write_message(message)

    def on_close(self):
        if self in ChatHandler.clients:
            ChatHandler.clients.remove(self)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('main.html')

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/chat", ChatHandler),
    ])
    application.listen(8881)
    tornado.ioloop.IOLoop.current().start()
