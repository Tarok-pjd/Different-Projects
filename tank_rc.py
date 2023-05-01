import socket, tkinter

def forward():
    client.send(b"forward")

def s():
    client.send(b"s")

def a():
    client.send(b"a")

def d():
    client.send(b"d")

def stop():
    client.send(b"o")

def connection():
    global client
    client = socket.create_connection(("10.42.42.17", 1234))

def end():
    client.send(b"e")
    client.close()
    main.destroy()


main = tkinter.Tk()

btn_start = tkinter.Button(main, text="start", command=connection)
btn_start.pack()
btn_w = tkinter.Button(main, text="w", command=forward)
btn_w.pack()
btn_s = tkinter.Button(main, text="s", command=s)
btn_s.pack()
btn_a = tkinter.Button(main, text="a", command=a)
btn_a.pack()
btn_d = tkinter.Button(main, text="d", command=d)
btn_d.pack()
btn_stop = tkinter.Button(main, text="stop", command=stop)
btn_stop.pack()
btn_end = tkinter.Button(main, text="end", command=end)
btn_end.pack()

#key bindings
btn_start.bind('<KeyPress-0x77>', forward)
btn_start.bind('<KeyRelease-0x77>', stop)



main.mainloop()