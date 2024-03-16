from discordrp import Presence
from datetime import datetime
from time import sleep


CLIENT_ID = '1218599022688862288'
NOWRUZ_UNIX:int = 1710903986

with Presence(CLIENT_ID) as presence:
    print("CONNECTED")
    presence.set(
        {
            "details": "Waiting for Nowruz...",
            "timestamps": {"end": NOWRUZ_UNIX},
            "assets" : {"large_image": "nowruz1403", "large_text": "Its not Nowruz yet!"}
        }
    )
    print("Presence updated")

    now = datetime.now().timestamp()

    while now < NOWRUZ_UNIX:
        sleep(1)
        now = datetime.now().timestamp()
    
    presence.set(
            {
                "details": "Happy Nowruz!",
                "timestamps": {"start": NOWRUZ_UNIX},
                "assets" : {"large_image": "nowruz1403", "large_text": "Happy Nowruz!"}
            }
            )
    print("Presence updated. HAPPY NOWRUZ!")

    print("\nYou can close the app now btw...")

    while True:
        sleep(30)