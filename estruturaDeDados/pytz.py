# Para instalar:  pip install pytz   e depois instale isso: python -m venv .env    source .env/bin/activate
import pytz
from datetime import datetime

data = datetime.now(pytz,timezone("Europe/Oslo"))
print(data)