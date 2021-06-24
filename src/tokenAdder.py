import json

if __name__ == "__main__":
    dest = open('tokens.py', 'a')
    sushiswapTokenList = open('sushiswapTokenList.txt', 'r')
    uniswapDefaultList = open('uniswapDefaultList.txt', 'r')
    
    uni = json.loads(uniswapDefaultList.read())
    sushi = json.loads(sushiswapTokenList.read())
    
    lists = [uni, sushi]
    symbols = []
    
    for l in lists:
        for token in l.get('tokens'):
            duplicate = False
            
            if (token.get('symbol') in symbols):
                duplicate = True
                break
            
            if duplicate == False:
                token_desc = token.get('symbol') + " = {\n"
                token_desc += "\'symbol\': \'" + token.get('symbol') + "\',\n"
                token_desc += "\'name\': \'" + token.get('name') + "\',\n"
                token_desc += "\'address\': hex(" + token.get('address') + "),\n"
                token_desc += "\'cksum_address\': w3.toChecksumAddress(\'" + token.get('address') + "\'),\n"
                token_desc += "\'decimals\': " + str(token.get('decimals')) + ",\n"
                token_desc += "}\n"
                
                symbols.append(token.get('symbol'))
                dest.write(token_desc)