import requests
import sys
import hashlib

def postData():
    host = 'http://devcci.p-enterprise.com/api/ecommerce/payment_result.php'
    m = hashlib.md5()
    appcode = 'ccit2p@gmail.com'
    invoice_no = '1902150001'
    amount = '10'
    txid = '123456'
    return_code = '0'
    channel = 'online'

    m.update("{}{}{}{}{}{}fc1efdbe71ce153e702892537f3a97ca".format(appcode, invoice_no, amount, txid, return_code, channel).encode())
    md5 = m.hexdigest()

    try:
        result = requests.post(host,
                               data={
                                   'AppCode': appcode,
                                   'InvoiceNo': invoice_no,
                                   'Amount': amount,
                                   'TXID': txid,
                                   'ReturnCode': return_code,
                                   'Channel': channel,
                                   'Sum': md5
                               })
        print(result.status_code)
        print(result.text)
    except Exception as e:
        pass


if __name__ == '__main__':
    postData()
