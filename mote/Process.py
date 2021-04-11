import multiprocessing

print("""Curia Angels - Raspberry Pi Server Rack""")

for bot in ('Fire', 'Blinkt', 'Enviro'):
    p = multiprocessing.Process(target=lambda: __import__(bot))
    p.start()
