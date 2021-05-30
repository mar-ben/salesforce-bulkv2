class bulk:
    GRANT_TYPE='password'
    access_token=''
    instance_url=''
    
    def __init__(self,client_id,client_secret,username,password,sandbox):
        try:
            instance_url='https://www.test.salesforce.com' if sandbox else 'https://www.login.salesforce.com'
            auth_url=instance_url + '/services/oauth2/token?grant_type='
            auth_url=auth_url+'{}&client_id={}&client_secret={}&username={}&password={}'.format(GRANT_TYPE,
                                                                                                client_id,
                                                                                                client_secret,
                                                                                                username,
                                                                                                password)
            print(auth_url)
            if 'access_token' not in response.json():
                print(response.json())
                print(response)
                #return response.json()
            else:
                access_token=response.json()['access_token']
            print(access_token)
            #return access_token;
        except:
            print(sys.exc_info())
            #return 'exception'
    
    def get_access_token():
        return access_token
        
    
    