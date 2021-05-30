class bulk:
    GRANT_TYPE='password'
    access_token=''
    instance_url=''
    auth_url=''
    DEFAULT_API_VERSION='v47.0'
    api_version=''
    job_url=''
    
    def __init__(self,client_id,client_secret,username,password,sandbox,api_version=DEFAULT_API_VERSION):
        #api_version=self.api_version if self.api_version else self.DEFAULT_API_VERSION;
        print('API='+api_version)
        self.api_version=api_version
        self.access_token=''
        self.instance_url='https://test.salesforce.com' if sandbox else 'https://login.salesforce.com'
        auth_url=self.instance_url + '/services/oauth2/token?grant_type='
        auth_url=auth_url+'{}&client_id={}&client_secret={}&username={}&password={}'.format(self.GRANT_TYPE,
                                                                                                client_id,
                                                                                                client_secret,
                                                                                                username,
                                                                                                password)
        print(auth_url)
        response=requests.post(auth_url)
        if 'access_token' not in response.json():
            print(response.json())
            print(response)
        else:
            self.access_token=response.json()['access_token'];
            self.job_url=response.json()['id']
            self.instance_url=response.json()['instance_url']
            print(self.access_token)
            print(self.job_url)
            #return access_token;
    
    def get_auth2_token(self):
        return self.access_token;
    
    def get_auth_url(self):
        print(auth_url)
        
    def create_job(self,object_api_name,operation):
        
        #Header
        headers={
            'Authorization':'Bearer {}'.format(self.access_token),
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json'
        }
        print(self.job_url)
        request_url=self.instance_url+"/services/data/{}/jobs/ingest".format(self.api_version)
        
        body={
            'operation': operation,
            'object':object_api_name,
            'contentType':'CSV'
        }
        
        
        response=requests.post(headers=headers,url=request_url,json=body)
        print(response.json())
        return response.json()['id']
        
    def upload_data(self,job,data):
        uri=self.instance_url+'/services/data/{}/jobs/ingest/{}/batches/'.format(self.api_version,job)
        #Header
        print(uri)
        header={
            'Authorization':'Bearer {}'.format(self.access_token),
            'Content-Type': 'text/csv',
            'Accept': 'application/json'
        }
        response=requests.put(headers=header,url=uri,data=data);
        print(response);
        return response
    
    def upload_complete(self,job):
        uri=self.instance_url+'/services/data/{}/jobs/ingest/{}/'.format(self.api_version,job)
        print(uri)
        header={
            'Authorization':'Bearer {}'.format(self.access_token),
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json'
        }
        body={
            'state':'UploadComplete'
        }
        
        response=requests.patch(headers=header,url=uri,json=body)
        print(response)
        return response;
    
    
        