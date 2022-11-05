import requests
import subprocess
import time
from utils import *


def fetch_urns():
    url = "https://www.linkedin.com/voyager/api/relationships/sentInvitationViewsV2?count=100&invitationType=CONNECTION&q=invitationType&start=0"

    subprocess.run(["clear"])
    t1 = time.perf_counter()
    print("\tFetching Sent Invitations...", end="\n")
    response = requests.get(url, headers=headers, cookies=cookies)
    t2 = time.perf_counter()

    print(f"\tFetched data in ... {round(t2-t1)} second(s)")

    with open("entityURNs.txt", "w") as file:
        for urn in response.json()["elements"]:
            first_name = urn['invitation']['toMember']['firstName']
            last_name = urn['invitation']['toMember']['lastName']
            print(f"\tSaved → {urn['invitation']['entityUrn']} -- {first_name} {last_name}")
            file.write(f"{urn['invitation']['entityUrn']}\n")

        print("\n\tOutput saved to → entityUrns.txt")


def withdrawl(urn):
    print(f"\tUrn → {urn} -- processing")
    url = "https://www.linkedin.com/voyager/api/relationships/invitations?action=closeInvitations"
    body = {
        "inviteActionType": "ACTOR_WITHDRAW",
        "inviteActionData": [
            {
                "entityUrn": f"{urn}",
                "genericInvitation": False,
                "genericInvitationType": "CONNECTION"
            }
        ]
    }

    response = requests.post(url, headers=headers, cookies=cookies, json=body)

    return f"\tUrn → {urn} -- completed"
