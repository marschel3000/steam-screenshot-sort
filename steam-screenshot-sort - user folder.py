#!/usr/bin/env python
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
        
        for img in os.listdir(root):
                if img.endswith('.png'):
                    img_splt = img.split('_')
                    
                    if len(img_splt) > 1:
                        game_id = img_splt[0]

                        game_name = None
                        try: 
                            game_name = getSteamName(game_id)
                            game_name = re.sub(ur'[^a-zA-Z0-9-_]', ' ', game_name).strip()
                        except:
                            pass

                    if (game_name):
                            new_folder = os.path.join(root, game_name)
                            if not os.path.isdir(new_folder):
                                    os.mkdir(new_folder)

                            shutil.move(os.path.join(root, img), os.path.join(new_folder, img))


if __name__ == '__main__':
        main()
