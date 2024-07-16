# Pyventory

Logviewer is a simple Python app to read log in browser.

## Install

Need python 3.10 or higher and [nicegui](https://nicegui.io/) installed.

```bash
pip install nicegui
```

Init and clone in /var/log directory on your system:
```shell
git init
git clone https://github.com/podzit/log_viewer.git
```
## Create a .gitignore file to exclude other files:

```shell
*
!log_viewer.py
```

## Customize your environment
Edit log_viewer.py to custom your environment:
```python
HOST = 'your_server_ip'
PORT = 8092 # Or another custom port
```

## Start app


```python
python3 ./log_viewer.py
```

## Start as a service

For Ubuntu create log_viewer.service in /etc/systemd/system/ with this lines:

```shell
[Unit]
Description=log_viewer
After=syslog.target network.target

[Service]
WorkingDirectory=[your_working_directory]
ExecStart=python3.10 [path_to_log_viewer.py]

Restart=always
RestartSec=120

[Install]
WantedBy=multi-user.target
```

Then reload daemon:

```shell
sudo systemctl daemon-reload
```

After that you can start stop and status with:
```shell
sudo service log_viewer start
sudo service log_viewer status
sudo service log_viewer stop
```

If you want to start service at boot :

```shell
sudo systemctl enable log_viewer.service
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
