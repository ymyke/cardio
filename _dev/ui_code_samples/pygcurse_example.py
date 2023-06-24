import pygcurse
win = pygcurse.PygcurseWindow(100, 50)
for k in pygcurse.colornames:
    win.write('This is the color %s\n' % (k), fgcolor=k)
pygcurse.waitforkeypress()
