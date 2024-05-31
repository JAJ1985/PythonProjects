# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 08:13:30 2021

@author: josjohn
"""

import xmltodict, json
obj=xmltodict.parse("""
<ValidateAddressResponse
	xmlns:xsd="http://www.w3.org/2001/XMLSchema"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <ReturnData>
    <Addressess>
      <Address>
        <StreetAddress>string</StreetAddress>
        <StreetAddress>string</StreetAddress>
        <StreetAddress>string</StreetAddress>
        <City>string</City>
        <PostalCode>string</PostalCode>
        <Country>AB</Country>
      </Address>
      <Address>
        <StreetAddress>string</StreetAddress>
        <StreetAddress>string</StreetAddress>
        <StreetAddress>string</StreetAddress>
        <PostalCode>string</PostalCode>
        <Country>AB</Country>
      </Address>
    </Addressess>
    <Messages>string</Messages>
  </ReturnData>
  <Errors>string</Errors>
</ValidateAddressResponse>
   """ )
print(json.dumps(obj))
