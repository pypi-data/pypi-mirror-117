import argparse
from pathlib import Path
import zipfile
import os
import pymsgbox


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pack', type=str)
    args = parser.parse_args()
        
    if args.pack.endswith('.zip'):
        try:
            with zipfile.ZipFile(args.pack, "r") as z:
                z.open("pack.mcmeta")
        except:
            pymsgbox.alert('This file is not formatting correctly, please make sure your file is zipped correctly', 'Warning')
            exit()
        with open("fabric.mod.json", "w+") as f:
            f.write("""{
        "schemaVersion":1,
        "environment":"*",
        "depends":{
            "fabric-api-base":"*",
            "fabric":"*",
            "minecraft":">=1.17"
        },
        "name":"My Pack",
        "id":"mypack",
        "version":"1.0.0",
        "description":"",
        "license":"Unknown",
        "pack_format":7
    }""")
        with open("MANIFEST.MF", "w+") as f:
            f.write("""Manifest-Version: 1.0""")

        with zipfile.ZipFile(args.pack, "a") as z:
            z.write("fabric.mod.json")
            z.write("MANIFEST.MF","META-INF\MANIFEST.MF")
        os.remove("fabric.mod.json")
        os.remove("MANIFEST.MF")
        path = Path(args.pack)
        os.rename(path.name, path.stem+".jar")
    else:
        pymsgbox.alert('This file is not a zip file', 'Warning')

