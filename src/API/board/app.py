import __init__ as setup
import pages as pg

if __name__ == "__main__":
    app = setup.FrencheraniApp()

    json = {"english": ["How are you?"], "french": "Ça va?"}
    
    pg.setWords(json)

    server = app.getServer()
    server.run(host=setup.HOST_ADDRESS, port=setup.HOST_PORT, debug=True)
