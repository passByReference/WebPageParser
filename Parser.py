from urllib import request, parse
from html.parser import HTMLParser

class AdItem(object):
    def __init__(self, tag, pos, attr_name, value):
        self._tag = tag
        self._pos = pos
        self._attr_name = attr_name
        self._value = value

class Parser(HTMLParser):
    def __init__(self):
        super(Parser, self).__init__()
        self._html_page = None
        self._ad_elements = []

    def feed(self, data):
        super(Parser, self).feed(data)
        self._html_page = data
        print('\nTotal number of Ads found: {}'.format(len(self._ad_elements)))

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            try:
                if attr and 'ad' in attr[-1]:
                    print('Ad found')
                    self._add_AdItem(tag, self.getpos(), attr[0], attr[-1])
            except IndexError:
                print('Error in attr')
            except:
                print('Unexpected error')

    def handle_startendtag(self, tag, attrs):
        for attr in attrs:
            try:
                if attr and 'ad' in attr[-1]:
                    print('Ad found')
                    self._add_AdItem(tag, self.getpos(), attr[0], attr[-1])
            except IndexError:
                print('Error in attr')
            except:
                print('Unexpected error')
    def get_html_page(self):
        if self._html_page:
            return self._html_page
        else:
            print('No html page fed to the parser')
            return None

    def get_ad_elements(self):
        return len(self._ad_elements)

    def _add_AdItem(self, tag, pos, attr_name, attr_value):
        print('tag       :{}'.format(tag))
        print('pos       :{}'.format(pos))
        print('attr_name :{}'.format(attr_name))
        print('attr_value:{}'.format(attr_value))
        print()
        self._ad_elements.append(AdItem(tag, pos, attr_name, attr_value))


def main():
    url = 'https://www.theatlantic.com/politics/archive/2017/05/if-there-are-white-house-recordings-they-could-be-subpoeanaed/526632/'
    u = request.urlopen(url)

    res = u.read().decode('utf-8')
    # p = Parser(res)
    p = Parser()
    script = '<script src="https://securepubads.g.doubleclick.net/gampad/ads?gdfp_req=1&amp;correlator=4160027710901272&amp;output=json_html&amp;callback=googletag.impl.pubads.callbackProxy2&amp;impl=fifs&amp;json_a=1&amp;eid=108809080%2C108809152%2C21060013&amp;sc=1&amp;sfv=1-0-8&amp;iu_parts=4624%2CTheAtlanticOnline%2Cchannel_politics&amp;enc_prev_ius=%2F0%2F1%2F2&amp;prev_iu_szs=300x600&amp;rcs=1&amp;prev_scp=pos%3Dboxtop%26mnetPageID%3D0%26mnetCC%3DUS%26mnetUGD%3D4%26mnetDW%3D4%26mnetCrid%3D583019428%26mnetbidID%3D33%26mnetbidderID%3Dmnet%26mnetbidPrice%3D1.11%26mnet_placement%3Dad-boxtop%26mnetCID%3D8CUD82U22%26mnetAct%3Dcache%26mnetScpvid%3D4%26mnetTd%3D0%25257Cm%25253Dref%25257C%26mnetSize%3D300x250&amp;eri=1&amp;cust_params=kuid%3Drke6qwz2w%26src%3Darticle%26rubric%3Dpolitics%26title%3Dif-there-are-white-house-recordings-they-could-be-subpoenaed%26type%3Dnon-mag-reg%26id%3D526632%26cat%3Dtrumps-fbi%26device%3Ddesktop-big%26subscriber%3Dloggedout%26interests%3D18209%252C27372%252C7377%252C19840%252C2441%252C18863%252C30347%252C865%252C32510%252C17281%252C17353%252C27815%252C2850%252C28478%252C17308%252C17305%252C17303%252C17309%252C17307%252C17306%252C17304%252C24653%252C24725%252C22980%252C17476%252C18890%252C17504%252C17468%252C18861%252C21865%252C22295%252C24077%252C24008%252C24009%252C24542%252C2988%252C27371%252C30352%252C8947%252C1913%252C30346%252C22061%252C3100%252C27087%252C8972%252C32497%252C27845%26amznslots%3Da3x2p12%252Ca7x9p12%252Ca3x6p10%252Ca9x2p12&amp;cookie=ID%3D17e3cd07072f7aa6%3AT%3D1489270186%3AS%3DALNI_MYDOC_N300ZbKBHsgEsrEtD3N1o_w&amp;abxe=1&amp;lmt=1494818471&amp;dt=1494818471229&amp;cc=100&amp;frm=20&amp;biw=1440&amp;bih=461&amp;oid=3&amp;adxs=900&amp;adys=725&amp;adks=3452988264&amp;gut=v2&amp;ifi=7&amp;u_tz=-240&amp;u_his=4&amp;u_h=900&amp;u_w=1440&amp;u_ah=823&amp;u_aw=1440&amp;u_cd=24&amp;u_nplug=4&amp;u_nmime=5&amp;u_sd=2&amp;flash=0&amp;url=https%3A%2F%2Fwww.theatlantic.com%2Fpolitics%2Farchive%2F2017%2F05%2Fif-there-are-white-house-recordings-they-could-be-subpoeanaed%2F526632%2F&amp;ref=https%3A%2F%2Fwww.theatlantic.com%2F&amp;dssz=102&amp;icsg=8590065664&amp;std=0&amp;vrg=117&amp;vrp=117&amp;ga_vid=1466052960.1489270178&amp;ga_sid=1494818337&amp;ga_hid=1128935240"></script>'
    p.feed(res)
    # print(p)

    return


main()