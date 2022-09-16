from cmath import log
import os
from dotenv import load_dotenv
from loguru import logger
import socket
from zeroconf import IPVersion, ServiceInfo, Zeroconf

load_dotenv()

type = "_http._tcp.local."
host = os.getenv("HOST")
device = os.getenv("DEVICE_NAME", "IoT Edge Device")
company = os.getenv("DEVICE_COMPANY", "Unknown")
port = os.getenv("PORT", 8000)
name = f"{device}.{type}"
server = f"{device}.local."

if host is None:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()

properties = {
    "url": "https://" + host + ":" + str(port),
    "company": company,
    "name": device,
}

logger.info("host=" + host)
logger.info("port=" + str(port))
logger.info("device=" + device)
logger.info("company=" + company)
logger.info("name=" + name)
logger.info("server=" + server)

info = ServiceInfo(
    type,
    name,
    addresses=[socket.inet_aton(host)],
    port=port,
    properties=properties,
    server=server,
)

zeroconf = Zeroconf()
zeroconf.register_service(info)

logger.info("Started zeroconf service")

try:
    print("Press Ctrl+C to exit")
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    logger.info("Shutting down zeroconf service")
    zeroconf.unregister_all_services()
    zeroconf.close()
