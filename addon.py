from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "http://www.ucy.tv/Feeds/Archives.aspx?name=The_Anti-Media_Radio&num=150"

@plugin.route('/')
def main_menu():
    items = [
   {
            'label': plugin.get_string(20000), 
            'path': "http://cdn.voscast.com/resources/?key=fd6db7a60caace8bf9ffe1ac14d6d205&c=wmp",
            'thumbnail': "http://www.ucy.tv/uploads/images/TAMRiTunes.png"}
            'is_playable': True,
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "http://www.ucy.tv/uploads/images/TAMRiTunes.png"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('episodes'),
            'thumbnail': "http://www.ucy.tv/uploads/images/TAMRiTunes.png"},
   ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
