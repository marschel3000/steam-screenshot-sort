#!/usr/bin/env python3
import urllib2
import os
import json
import sys
import shutil
import re

def getSteamName(steamID):
        try:
                steamID = int(steamID)
                if steamID > 0 and steamID < 9223372036854775807:
                        r = urllib2.urlopen('https://store.steampowered.com/api/appdetails/?appids='+str(steamID))
                        data = json.load(r)

                        if (data[unicode(steamID)]['success']):
                                return unicode(data[unicode(steamID)]['data']['name'])
        except:
                pass


def main():
        root = os.getcwd()
        for dir_name in os.listdir(root):
                dir_path = os.path.join(root, dir_name)
                sreens_path = os.path.join(dir_path, 'screenshots')
                game_name = getSteamName(dir_name)

                if (game_name):
                        game_name = re.sub(ur'[^a-zA-Z0-9-_]', ' ', game_name).strip()
                        new_folder = os.path.join(root, game_name)
                        if not os.path.isdir(new_folder):
                                os.mkdir(new_folder)

                        for img in os.listdir(sreens_path):
                                if (not os.path.isdir(os.path.join(sreens_path, img))):
                                        shutil.copy2(os.path.join(sreens_path, img), new_folder)

                        shutil.rmtree(dir_path, True)

if __name__ == '__main__':
        main()