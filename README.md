# QuackAttack
This project automates several open source technologies to dump and exfiltrate saved user credentials using a USB Rubber Ducky.

## Features
* Disable Windows Defender real-time monitoring
* Add an exception to Windows Defender for the `C:\Users\` folder
* Download a custom-compiled version of [LaZagne](https://github.com/AlessandroZ/LaZagne)
* Download and launch the wrapper/exfiltration executable 
* Save credential report to [PasteBin](https://pastebin.com/doc_api)
* Save PasteBin report URL to MySQL database

## Build executables
Executable files generated with PyInstaller are specific to the active operating system, so a Windows 10 VM with Python3 is required for this step.
```
python -m pip install -r requirements.txt
python -m PyInstaller --onefile lazagne.spec
python -m PyInstaller --onefile qa.py
```

The generated executables will be saved to the `dist\` directory.

## Deploy infrastructure
This webapp is responsible for hosting the generated executables and for keeping track of all PasteBin links. While building the executables requires a Windows machine, Linux or macOS is recommended for the webserver host. 

Place the generated executables in the `web/php/src/` directory on the webserver host.

Download [ngrok](https://ngrok.com/download) and extract it to the `web/tools/` directory. If you want a custom subdomain you will have to upgrade to a Basic plan, but the Free plan should be fine for short engagements.

[Docker Compose](https://www.docker.com/products/docker-desktop) is used to deploy containers for Apache/PHP, MySQL, and PHPMyAdmin.
```
cd web/
docker-compose up --build -d
./tools/ngrok http 80 -subdomain=quackattack
```

## Prepare USB Rubber Ducky
1. Update `duckyscript.txt` with your webapp's URL. Make sure the .exe files are reachable.
2. Browse to `/ducky_encoder.php` and paste the contents of `duckyscript.txt` into the textfield on the webpage.
3. Press **Generate Payload** and download the `inject.bin` file it generates.
4. Copy `inject.bin` to the root of the Rubber Ducky’s microSD card.

## Resources
[Deploy Apache, PHP, and MySQL using Docker Containers](https://www.section.io/engineering-education/dockerized-php-apache-and-mysql-container-development-environment/)

[PyInstaller Usage](https://pyinstaller.readthedocs.io/en/latest/usage.html)

[ngrok Usage](https://ngrok.com/docs)