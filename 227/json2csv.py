import os
from pathlib import Path
import csv
import json
from json.decoder import JSONDecodeError

EXCEPTION = 'exception caught'
TMP = Path(os.getenv("TMP", "/tmp"))


def convert_to_csv(json_file: Path) -> None:
    """Read/load the json_file (local file downloaded to /tmp) and
       convert/write it to defined csv_file.
        The data is in mounts > collected

       Catch bad JSON (JSONDecodeError) file content, in that case print the defined
       EXCEPTION string ('exception caught') to stdout reraising the exception.
       This is to make sure you actually caught this exception.

       Example csv output:
       creatureId,icon,isAquatic,isFlying,isGround,isJumping,itemId,name,qualityId,spellId
       32158,ability_mount_drake_blue,False,True,True,False,44178,Albino Drake,4,60025
       63502,ability_mount_hordescorpionamber,True,...
       ...
    """  # noqa E501
    csv_file = TMP / json_file.name.replace('.json', '.csv')
    try:
        json_data = json.load(json_file.open())
        mounts_data = json_data["mounts"]["collected"]
        csv_key_list = list(mounts_data[0].keys())
        with csv_file.open('w', newline="") as csv_out_file:
            csv_writer = csv.DictWriter(csv_out_file, fieldnames=csv_key_list)
            csv_writer.writeheader()
            csv_writer.writerows(mounts_data)
    except JSONDecodeError:
        print(EXCEPTION)
        raise

    # you code
