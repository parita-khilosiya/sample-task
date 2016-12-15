
import cherrypy
import redis


class Nifty50Diplay(object):
    @cherrypy.expose
    def index(self):
        return open("public/index.html")


@cherrypy.expose
class Nifty50WebService(object):

    # @cherrypy.tools.accept(media='text/json')
    def GET(self):
        # conn = redis.Redis('localhost')
        # data = conn.get("nifty50Data")
        data = '{"lasupdatedtime": "2016-12-15 20:38:59", "count": 24, "data": [{"ltp": "478.75", "netPrice": "2.47", "lastCorpAnnouncement": "Annual General Meeting/ Dividend-Rs 5/- Per Share", "lastCorpAnnouncementDate": "07-Jul-2016", "series": "EQ", "symbol": "AXISBANK", "openPrice": "459.10", "previousPrice": "467.20", "lowPrice": "459.10", "turnoverInLakhs": "85,308.98", "tradedQuantity": "1,80,21,627", "highPrice": "479.40"}, {"ltp": "2,256.50", "netPrice": "2.22", "lastCorpAnnouncement": "Interim Dividend- Rs 6.50/- Per Share", "lastCorpAnnouncementDate": "24-Oct-2016", "series": "EQ", "symbol": "TCS", "openPrice": "2,202.00", "previousPrice": "2,207.60", "lowPrice": "2,202.00", "turnoverInLakhs": "48,484.01", "tradedQuantity": "21,47,705", "highPrice": "2,272.10"}, {"ltp": "206.15", "netPrice": "1.28", "lastCorpAnnouncement": "Bonus 1: 2", "lastCorpAnnouncementDate": "15-Dec-2016", "series": "EQ", "symbol": "ONGC", "openPrice": "202.80", "previousPrice": "305.30", "lowPrice": "201.35", "turnoverInLakhs": "20,462.77", "tradedQuantity": "1,00,11,138", "highPrice": "208.60"}, {"ltp": "1,084.95", "netPrice": "1.22", "lastCorpAnnouncement": "Annual General Meeting/ Dividend -Rs 4.50/- Per Share", "lastCorpAnnouncementDate": "23-Jun-2016", "series": "EQ", "symbol": "INDUSINDBK", "openPrice": "1,060.00", "previousPrice": "1,071.85", "lowPrice": "1,057.05", "turnoverInLakhs": "14,349.41", "tradedQuantity": "13,27,125", "highPrice": "1,092.90"}, {"ltp": "1,188.00", "netPrice": "1.20", "lastCorpAnnouncement": "Annual General Meeting/ Dividend - Rs 12/- Per Share", "lastCorpAnnouncementDate": "21-Jul-2016", "series": "EQ", "symbol": "M&M", "openPrice": "1,170.00", "previousPrice": "1,173.95", "lowPrice": "1,166.10", "turnoverInLakhs": "11,416.31", "tradedQuantity": "9,61,665", "highPrice": "1,196.80"}, {"ltp": "160.20", "netPrice": "1.17", "lastCorpAnnouncement": "Annual General Meeting", "lastCorpAnnouncementDate": "16-Jun-2016", "series": "EQ", "symbol": "BANKBARODA", "openPrice": "157.00", "previousPrice": "158.35", "lowPrice": "156.40", "turnoverInLakhs": "7,938.27", "tradedQuantity": "49,77,598", "highPrice": "161.40"}, {"ltp": "830.00", "netPrice": "1.12", "lastCorpAnnouncement": "Interim Dividend - Rs 6/- Per Share (Purpose Revised)", "lastCorpAnnouncementDate": "27-Oct-2016", "series": "EQ", "symbol": "HCLTECH", "openPrice": "822.00", "previousPrice": "820.80", "lowPrice": "822.00", "turnoverInLakhs": "23,345.35", "tradedQuantity": "28,00,815", "highPrice": "840.00"}, {"ltp": "183.95", "netPrice": "1.10", "lastCorpAnnouncement": "Dividend - Rs 1.51 Per Share", "lastCorpAnnouncementDate": "08-Sep-2016", "series": "EQ", "symbol": "POWERGRID", "openPrice": "181.00", "previousPrice": "181.95", "lowPrice": "180.50", "turnoverInLakhs": "5,432.84", "tradedQuantity": "29,55,360", "highPrice": "185.75"}, {"ltp": "2,674.50", "netPrice": "0.98", "lastCorpAnnouncement": "Annual General Meeting/ Dividend - Rs 5/- Per Share", "lastCorpAnnouncementDate": "14-Jul-2016", "series": "EQ", "symbol": "BAJAJ-AUTO", "openPrice": "2,668.00", "previousPrice": "2,648.50", "lowPrice": "2,628.85", "turnoverInLakhs": "6,616.52", "tradedQuantity": "2,47,366", "highPrice": "2,699.05"}, {"ltp": "265.35", "netPrice": "0.93", "lastCorpAnnouncement": "Dividend - Rs 2.60/- Per Share", "lastCorpAnnouncementDate": "03-Jun-2016", "series": "EQ", "symbol": "SBIN", "openPrice": "259.90", "previousPrice": "262.90", "lowPrice": "259.00", "turnoverInLakhs": "32,523.73", "tradedQuantity": "1,22,74,497", "highPrice": "267.50"}], "time": "Dec 15, 2016 16:00:00"}'
        return data
