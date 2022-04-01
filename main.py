from __future__ import print_function

import discord
import requests
from web3 import Web3, HTTPProvider
import time

global oldaddy 

oldaddy=['start','0xdacd61bce7ae049270a156e5f21f00ae1839d51e']

async def timer():
    while True:
        print('trying...')
        await get_token(oldaddy)
        time.sleep(60)
    return()



async def get_token(oldaddy):


    response = requests.get('https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock=14502540&toBlock=latest&address=0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f&topic0=0x0d3648bd0f6ba80134a33ba9275ac585d9d315f0ad8355cddefde31afa28d0e9&apikey=79XW92AXXB3SF979BM1QKHU2UGNYRJHQMW')
    print(response.status_code)
    jsonfy=response.json()

    no1= '0x0d3648bd0f6ba80134a33ba9275ac585d9d315f0ad8355cddefde31afa28d0e9'
    no2= '0x000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'

    x = jsonfy['result'][-1]['topics']

    addy='null'
    for i in x:
        if i != no1 and i != no2:
            addy = i
            addy= addy[26:]
            addy='0x'+addy

            print('addy', addy)
            print('old', oldaddy[-1])
            #print('list',oldaddy)

            if addy != oldaddy[-1]:
                oldaddy.append(addy)

                # print(oldaddy)

                # print(addy)
                await get_token_data(addy)

                return()

async def get_token_data(addy):
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/f5f59da316084e02a53b9c8a43692a98'))

    addy = addy
    tokencontract='null'
    contract='null'
    token_name='null'
    token_symbol='null'
    etherscan_url='null'

    print('about to get token data')

    tokencontract = w3.toChecksumAddress(addy)

    abi2 = [{"constant":True,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":False,"type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":False,"type":"function"},{"anonymous":False,"inputs":[{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":False,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":False,"inputs":[],"name":"Pause","type":"event"},{"anonymous":False,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"owner","type":"address"},{"indexed":True,"name":"spender","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]

    contract = w3.eth.contract(tokencontract, abi= abi2)

    token_name= contract.functions.name().call()

    token_symbol = contract.functions.symbol().call()

    etherscan_url = 'https://etherscan.io/address/'+addy

    print(token_name, token_symbol, etherscan_url)

    await tokenalert(token_name, token_symbol, etherscan_url)
    
    return()



TOKEN ="OTUwODQyNDg3ODUxODY4MjEw.YiezEg.tqeSIHrE4T8hESzf_BvIKahYULQ"

client = discord.Client()

@client.event
async def tokenalert(token_name, token_symbol, etherscan_url):
    channel = client.get_channel(950842060594905108)
    print(channel)
    print('preparing to send alert...')
    embed2 = discord.Embed(title = str(token_name), description= token_symbol +': created on Uniswap!', url = str(etherscan_url), color = 0xffd800 )
    
    print(embed2)
    await channel.send(embed = embed2)
    return()



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await timer()




client.run(TOKEN)



