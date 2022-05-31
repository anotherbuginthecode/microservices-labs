def extract_token(headers):
    bearer = headers.get('Authorization') 
    token = bearer.split()[1]
    return token