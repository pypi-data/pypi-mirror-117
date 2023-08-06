# -*- coding: utf-8 -*-
import time
import json
import uuid

class PrimaryAccountInitService(object):

    def __init__(self):
        self.register_headers  = {
            "x-line-application": "ANDROID\t11.14.0\tAndroid OS\t10.0.1",
            "x-le": self.le,
            "x-lcs": self._encryptKey,
            "User-Agent": "Line/11.14.0",
            "content-type": "application/x-thrift; protocol=TBINARY",
            "x-lpv": "1",
        }
        self.uuid = uuid.uuid4().hex
    
    def setPrimaryUuid(self, uuid):
        self.uuid = uuid
        
    def openPrimarySession(self):
        _headers = {
            'x-lpqs': "/acct/pais/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('openSession') + [0, 0, 0, 0]
        sqrd += [12, 0, 1]
        sqrd += [13, 0, 1, 11, 11] + self.getIntBytes(0)
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent('https://ga2.line.naver.jp', data=data, headers=self.register_headers)
        data = self.decData(res.content)
        return self.tryReadData(data)
        
    def getCountryInfo(self, authSessionId, simCard=None):
        _headers = {
            'x-lpqs': "/acct/pais/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('getCountryInfo') + [0, 0, 0, 0]
        sqrd += [11, 0, 1] + self.getStringBytes(authSessionId)
        sqrd += [0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent('https://ga2.line.naver.jp', data=data, headers=self.register_headers)
        data = self.decData(res.content)
        return self.tryReadData(data)
        
    def getPhoneVerifMethod(self, authSessionId, phoneNumber, countryCode, deviceModel="SM-N950F"):
        _headers = {
            'x-lpqs': "/acct/pais/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('getPhoneVerifMethod') + [0, 0, 0, 0]
        sqrd += [11, 0, 1] + self.getStringBytes(authSessionId)
        sqrd += [12, 0, 2]
        sqrd += [11, 0, 1] + self.getStringBytes(self.uuid)
        sqrd += [11, 0, 2] + self.getStringBytes(deviceModel)
        sqrd += [0]
        sqrd += [12, 0, 3]
        sqrd += [11, 0, 1] + self.getStringBytes(phoneNumber)
        sqrd += [11, 0, 2] + self.getStringBytes(countryCode)
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent('https://ga2.line.naver.jp', data=data, headers=self.register_headers)
        data = self.decData(res.content)
        return self.tryReadData(data)
        
    def sendPinCodeForPhone(self, authSessionId, phoneNumber, countryCode, deviceModel="SM-N950F"):
        _headers = {
            'x-lpqs': "/acct/pais/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('sendPinCodeForPhone') + [0, 0, 0, 0]
        sqrd += [11, 0, 1] + self.getStringBytes(authSessionId)
        sqrd += [12, 0, 2]
        sqrd += [11, 0, 1] + self.getStringBytes(self.uuid)
        print(f"UUID: {self.uuid}")
        sqrd += [11, 0, 2] + self.getStringBytes(deviceModel)
        sqrd += [0]
        sqrd += [12, 0, 3]
        sqrd += [11, 0, 1] + self.getStringBytes(phoneNumber)
        sqrd += [11, 0, 2] + self.getStringBytes(countryCode)
        sqrd += [0]
        sqrd += [8, 0, 4] + self.getIntBytes(2)
        sqrd += [0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent('https://ga2.line.naver.jp', data=data, headers=self.register_headers)
        data = self.decData(res.content)
        return self.tryReadData(data)
        
    def verifyPhone(self, authSessionId, phoneNumber, countryCode, pinCode, deviceModel="SM-N950F"):
        _headers = {
            'x-lpqs': "/acct/pais/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('verifyPhone') + [0, 0, 0, 0]
        sqrd += [11, 0, 1] + self.getStringBytes(authSessionId)
        sqrd += [12, 0, 2]
        sqrd += [11, 0, 1] + self.getStringBytes(self.uuid)
        sqrd += [11, 0, 2] + self.getStringBytes(deviceModel)
        sqrd += [0]
        sqrd += [12, 0, 3]
        sqrd += [11, 0, 1] + self.getStringBytes(phoneNumber)
        sqrd += [11, 0, 2] + self.getStringBytes(countryCode)
        sqrd += [0]
        sqrd += [11, 0, 4] + self.getStringBytes(pinCode)
        sqrd += [0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent('https://ga2.line.naver.jp', data=data, headers=self.register_headers)
        data = self.decData(res.content)
        return self.tryReadData(data)
        
    def validateProfile(self, authSessionId, displayName):
        _headers = {
            'x-lpqs': "/acct/pais/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('validateProfile') + [0, 0, 0, 0]
        sqrd += [11, 0, 1] + self.getStringBytes(authSessionId)
        sqrd += [11, 0, 2] + self.getStringBytes(displayName)
        sqrd += [0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent('https://ga2.line.naver.jp', data=data, headers=self.register_headers)
        data = self.decData(res.content)
        return self.tryReadData(data)
        
    def exchangeEncryptionKey(self, authSessionId, publicKey, nonce, authKeyVersion=1):
        _headers = {
            'x-lpqs': "/acct/pais/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('exchangeEncryptionKey') + [0, 0, 0, 0]
        sqrd += [11, 0, 1] + self.getStringBytes(authSessionId)
        sqrd += [12, 0, 2]
        sqrd += [8, 0, 1] + self.getIntBytes(authKeyVersion)
        sqrd += [11, 0, 2] + self.getStringBytes(publicKey)
        sqrd += [11, 0, 3] + self.getStringBytes(nonce)
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent('https://ga2.line.naver.jp', data=data, headers=self.register_headers)
        data = self.decData(res.content)
        return self.tryReadData(data)
        
    def setPassword(self, authSessionId, cipherText, encryptionKeyVersion=1):
        _headers = {
            'x-lpqs': "/acct/pais/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('setPassword') + [0, 0, 0, 0]
        sqrd += [11, 0, 1] + self.getStringBytes(authSessionId)
        sqrd += [12, 0, 2]
        sqrd += [8, 0, 1] + self.getIntBytes(encryptionKeyVersion)
        sqrd += [11, 0, 2] + self.getStringBytes(cipherText)
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent('https://ga2.line.naver.jp', data=data, headers=self.register_headers)
        data = self.decData(res.content)
        return self.tryReadData(data)
        
    def registerPrimaryUsingPhone(self, authSessionId):
        _headers = {
            'x-lpqs': "/acct/pais/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1] + self.getStringBytes('registerPrimaryUsingPhone') + [0, 0, 0, 0]
        sqrd += [11, 0, 2] + self.getStringBytes(authSessionId)
        sqrd += [0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.server.postContent('https://ga2.line.naver.jp', data=data, headers=self.register_headers)
        data = self.decData(res.content)
        return self.tryReadData(data)
        
    def getPhoneVerifMethodV2(self, authSessionId, phoneNumber, countryCode, deviceModel="SM-N950F"):
        params = [
            [12, 1, [
                [11, 1, authSessionId],
                [12, 2, [
                    [11, 1, self.uuid],
                    [11, 2, deviceModel]
                ]],
                [12, 3, [
                    [11, 1, phoneNumber],
                    [11, 2, countryCode]
                ]],
            ]]
        ]
        sqrd = self.generateDummyProtocol('getPhoneVerifMethodV2', params, 3)
        return self.postPackDataAndGetUnpackRespData("/acct/pais/v1" ,sqrd, 3, headers=self.register_headers)
        
    def requestToSendPhonePinCode(self, authSessionId, phoneNumber, countryCode, verifMethod=1):
        params = [
            [12, 1, [
                [11, 1, authSessionId],
                [12, 2, [
                    [11, 1, phoneNumber],
                    [11, 2, countryCode]
                ]],
                [8, 3, verifMethod],
            ]]
        ]
        sqrd = self.generateDummyProtocol('requestToSendPhonePinCode', params, 3)
        return self.postPackDataAndGetUnpackRespData("/acct/pais/v1" ,sqrd, 3, headers=self.register_headers)
        
    def verifyPhonePinCode(self, authSessionId, phoneNumber, countryCode, pinCode):
        params = [
            [12, 1, [
                [11, 1, authSessionId],
                [12, 2, [
                    [11, 1, phoneNumber],
                    [11, 2, countryCode]
                ]],
                [11, 3, pinCode],
            ]]
        ]
        sqrd = self.generateDummyProtocol('verifyPhonePinCode', params, 3)
        return self.postPackDataAndGetUnpackRespData("/acct/pais/v1" ,sqrd, 3, headers=self.register_headers)
        
    def verifyAccountUsingPwd(self, authSessionId, identifier, countryCode, cipherText):
        params = [
            [12, 1, [
                [11, 1, authSessionId],
                [12, 2, [
                    [8, 1, 1], # type
                    [11, 2, identifier],
                    [11, 3, countryCode]
                ]],
                [12, 3, [
                    [8, 1, 1], # encryptionKeyVersion
                    [11, 2, cipherText]
                ]],
            ]]
        ]
        sqrd = self.generateDummyProtocol('verifyAccountUsingPwd', params, 3)
        return self.postPackDataAndGetUnpackRespData("/acct/pais/v1" ,sqrd, 3, headers=self.register_headers)
        
    def registerPrimaryUsingPhoneWithTokenV3(self, authSessionId):
        params = [
            [11, 2, authSessionId]
        ]
        sqrd = self.generateDummyProtocol('registerPrimaryUsingPhoneWithTokenV3', params, 3)
        return self.postPackDataAndGetUnpackRespData("/acct/pais/v1" ,sqrd, 3, headers=self.register_headers)
        
    def registerPrimaryWithTokenV3(self, authSessionId):
        params = [
            [11, 2, authSessionId]
        ]
        sqrd = self.generateDummyProtocol('registerPrimaryUsingPhoneWithTokenV3', params, 3)
        return self.postPackDataAndGetUnpackRespData("/acct/pais/v1" ,sqrd, 3, headers=self.register_headers)