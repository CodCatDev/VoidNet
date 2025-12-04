from engine.window import Window

def mainGame():
    window = Window("Void.Net: ", [800, 600])
    window.buildWindow()
    while True:
        window.updEvents()
        window.isClose()
        if window.close:
            window.quit()
            return 
        window.upd()

if __name__ == "__main__":
    mainGame()