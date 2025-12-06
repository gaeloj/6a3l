import xbmcplugin
import xbmcgui
import sys

handle = int(sys.argv[1])

# Item de vídeo do Google Drive
li = xbmcgui.ListItem("Vídeo de teste")
url = "https://drive.google.com/uc?export=download&id=19ZVWLWZXKJJZUmr0KRmfehoFIPBNmahL"
xbmcplugin.addDirectoryItem(handle=handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(handle)

