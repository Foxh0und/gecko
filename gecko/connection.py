import base64
import time
import hashlib
import hmac
import json
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

class Connection:
    def __init__( self, aAPIKey, aPrivateKey ):
        self.fAPIKey = aAPIKey
        self.fAPIPrivateKey = base64.b64decode( aPrivateKey )
        self.fBaseURL = 'https://api.btcmarkets.net'


    def signMessage( self, aMessage):
        presignature = base64.b64encode( hmac.new( self.fAPIPrivateKey, aMessage.encode('utf-8'), digestmod=hashlib.sha512).digest() )
        return  presignature.decode('utf8')


    def buildHeaders( self, aMethod, path, data):
        lCurrentTimeStamp = str( int( time.time() * 1000) )
        lMessage = aMethod + path + lCurrentTimeStamp
        if data is not None:
            lMessage += data

        signature = self.signMessage( lMessage )

        lHeaders = {
            "Accept": "application/json",
            "Accept-Charset": "UTF-8",
            "Content-Type": "application/json",
            "BM-AUTH-APIKEY": self.fAPIKey,
            "BM-AUTH-TIMESTAMP": lCurrentTimeStamp,
            "BM-AUTH-SIGNATURE": signature
        }

        return lHeaders

    def makeHTTPRequest( self, aMethod, aPath, aQueryString, data=None ):
        if data is not None:
            data = json.dumps( data )

        lHeaders = self.buildHeaders( aMethod, aPath, data)
        lFullPath = ''

        if aQueryString is None:
            lFullPath = aPath
        else:
            lFullPath = aPath + '?' + aQueryString

        try:
            lRequest = Request( self.fBaseURL + lFullPath, data, lHeaders, method = aMethod )

            if aMethod == 'POST' or aMethod == 'PUT':
                lResponse = urlopen( lRequest, data = bytes( data, encoding="utf-8" ) )
            else:
                response = urlopen( lRequest )

            return json.loads( str(response.read(), "utf-8") )

        except URLError as e:
            errObject = json.loads( e.read())
            if hasattr( e, 'code' ):
                errObject['statusCode'] = e.code

            return errObject
    
