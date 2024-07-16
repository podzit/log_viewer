import os
from nicegui import ui

HOST = 'your_server_ip'
PORT = 8092
LOG_LIST = []
LOG_DIR = os.path.dirname(__file__)

for logfile in os.listdir(LOG_DIR):
    if logfile.endswith('.log'):
        log_path = os.path.join(LOG_DIR,logfile)
        LOG_LIST.append(log_path)

def display_log():
    for logfile in LOG_LIST:
        with open(logfile, mode='r') as f:
            content = f.readlines()
            if content:
                with ui.expansion(logfile).classes('text-lg bg-gradient-to-r from-sky-200 to-cyan-100'):
                    with ui.label():
                        i = 0
                        for line in content[::-1]:
                            if i < 31:
                                ui.label(f'{line}').classes('text-sm')
                                i += 1

display_log()

ui.run(host=HOST, port=PORT, title='Log Viewer', uvicorn_reload_dirs=LOG_DIR, uvicorn_reload_includes='*.log', uvicorn_reload_excludes='daemon.log')
