import bottle

app = bottle.Bottle()

@app.get("/")
def index():
    return "It works"

def run():
    bottle.run(app=app, server = 'waitress')

if __name__ == "__main__":
    run()