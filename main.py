import bottle

app = bottle.Bottle()

@app.get("/")
def index():
    return "It works"

def run():
    bottle.run(app=app, server = 'waitress', host="0.0.0.0", port=80)

if __name__ == "__main__":
    run()