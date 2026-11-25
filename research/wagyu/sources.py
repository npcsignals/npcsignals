from collect import call
import concurrent.futures
urls={
'wagyu_docs':'https://docs.wagyu.xyz/',
'bridge_docs':'https://docs.wagyu.xyz/bridge',
'bridge_terms_docs':'https://docs.wagyu.xyz/api-reference/bridge/terms',
'hip1':'https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-1-native-token-standard.md',
'multisig_docs':'https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/multi-sig.md',
'info_docs':'https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint.md',
'hosting_home':'https://1984.hosting/',
'hosting_announcements':'https://1984.hosting/announcements/',
'cert_home':'https://cert.is/',
'operator_oct_mirror':'https://www.nitter.cf/PerpetualCow/status/2123711967055458711',
'wayback_index':'https://web.archive.org/cdx/search/cdx?url=wagyu.xyz&output=json&filter=statuscode:200&filter=mimetype:text/html&collapse=timestamp:6&filter=timestamp:202[56].*&limit=30',
'hip1_sdk':'https://raw.githubusercontent.com/hyperliquid-dex/hyperliquid-python-sdk/master/hyperliquid/info.py'
}
list(concurrent.futures.ThreadPoolExecutor(max_workers=5).map(lambda x:call(x[0],None,x[1]),urls.items()))
