import pyinotify
import tornado.ioloop

def on_file_modify():
    print("File Modified")

class IWm:
    def __init__(self):
        self.wm = pyinotify.WatchManager()
    
    def add_watch(self, path, mask=pyinotify.IN_MODIFY, callback_function=None):
        self.wm.add_watch(
            path=path,
            mask=mask,
            proc_fun=callback_function
        )
    
    def start_watching(self):
        self.ioloop = tornado.ioloop.IOLoop.instance()
        self.notifier = pyinotify.TornadoAsyncNotifier(self.wm, self.ioloop)
        self.ioloop.start()

if __name__ == '__main__':
    iwm = IWm()
    iwm.add_watch(
        path="some.log",
        call_backfunction=on_file_modify,
    )
    iwm.start_watching()
    