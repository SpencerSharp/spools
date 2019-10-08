# import requests

# url = "https://rateyourmusic.com/httprequest"
# token = 'nExTxWyOpYo%2FqAvduByPmoSjN6mmlwa06Dwp4ok4CxnUMLKOnxaTCSoLZoJWdHzS1561948407859611'
# album_id = 3050748
# rating = 1
# username = 'cp3_4_mvp'

# payload = "action=CatalogSetRating&assoc_id={0}&rating={1}&request_token={2}&rym_ajax_req=1&type=l"
# payload = payload.format(album_id,rating,token)
# cookie_str = "sec_bs=1bbe93b6a34415f99fdb8ac3b0757fa2; sec_ts=1566585814; sec_id=90abfae55c85d696e36f6a747c23b19c; ulv={token}; is_logged_in=1; username={username}; __utmc=187111339; _pubcid=7c50b180-0f1b-41b2-8c89-59c7e32c4543; sovrn_cookie=ed5dc71114bd72c46fb9096c; districtm_cookie=8043065828311815218; __qca=P0-1477909557-1563137390728; pubmatic_cookie=309D743B-79A8-465D-8369-2BAF84558FFF; proper_tracker_cookie=eyJwaWQiOiIiLCJiaWRkZXJzIjp7InNvdnJuIjoxLCJkaXN0cmljdG0iOjEsInB1Ym1hdGljIjoxfSwicHJvcGVyX3VpZCI6IjdjNTBiMTgwLTBmMWItNDFiMi04Yzg5LTU5YzdlMzJjNDU0MyJ9; __utmz=187111339.1563250795.7.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=187111339.1034504250.1562990345.1563250795.1563329528.8; genre_vote_banner_seen=true"
# cookie_str = cookie_str.format(token=token,username=username)
# payload_len = len(payload)
# headers = {
#     'Accept': "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
#     'X-Requested-With': "XMLHttpRequest",
#     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
#     'Sec-Fetch-Mode': "cors",
#     'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "056a38ea-3bdb-4f6a-9ff3-047186b559f7,076f8953-ff30-4576-ac6c-4baefd91ef1c",
#     'Host': "rateyourmusic.com",
#     'Cookie': cookie_str,
#     'Accept-Encoding': "gzip, deflate",
#     'Content-Length': "{}".format(payload_len),
#     'Connection': "keep-alive",
#     'cache-control': "no-cache"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)