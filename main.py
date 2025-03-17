from pypresence.presence import Presence
from datetime import datetime
from time import sleep

CLIEND_ID = "1218599022688862288"
NOWRUZ = datetime(2025, 3, 20, 12, 31, 30) # In case of changes (2025, 3, 20, 12, 31, 30)
NOWRUZ_UNIX = int(NOWRUZ.timestamp())

pres = Presence(CLIEND_ID)

pres.connect()
print(NOWRUZ - datetime.now())

while True:
    remaining = NOWRUZ - datetime.now()
    if remaining.days > 0:
        timeout = 120
        pres.update(
            large_text="Waiting for Nowruz of 1404",
            large_image="nowruz1404",
            state=f"{remaining.days} days to Nowruz!",
            end=NOWRUZ_UNIX,
        )
    elif remaining.days == 0 and remaining.seconds > 60*60:
        rem = str(remaining).split(":")
        pres.update(
            large_text="Waiting for Nowruz of 1404",
            large_image="nowruz1404",
            state=f"{rem[0]}h and {rem[1]}m till Nowruz!",
            end=NOWRUZ_UNIX,
        )
        timeout = 2
    elif remaining.days == 0 and remaining.seconds > 120:
        rem = str(remaining).split(":")
        pres.update(
            large_text="Waiting for Nowruz of 1404",
            large_image="nowruz1404",
            state=f"{int(rem[1])} minutes till Nowruz!",
            end=NOWRUZ_UNIX,
        )
        timeout = 30
    else:
        pres.update(
            large_image="nowruz1404",
            state=f"{remaining.seconds} seconds till Nowruz!",
            end=NOWRUZ_UNIX,
        )
        timeout = 1
    
    if remaining.seconds <= 0:
        break

    sleep(timeout)

print("\nHappy Nowruz mate!\nWish you a better year ;)")
print("\nYou can close the app now.")

pres.update(
    large_image='nowruz1404',
    large_text='Nowruz of 1404',
    state="Happy Nowruz!",
    start=NOWRUZ_UNIX
)

try:
    while True:
        pass
except KeyboardInterrupt:
    quit()