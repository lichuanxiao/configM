import requests


class Gitlab():
    '''
    GitLab 基础类，获取 api 和 token 参数，
    自动获取 projects 列表
    '''
    def __init__(self, api_url, token):
        self.baseurl = api_url
        self.token = token
        self.projects = []
        
    def create_project(self,name,namespaces,description):
        _rel = self.search_namespaces(namespaces)
        if _rel[0]:
            params = {"private_token":self.token, "name":name, "namespace_id":_rel[1], "description":description}
            requests.post(self.baseurl+"projects",params=params)
            params = {"private_token":self.token, "search":name}
            _project_list = requests.get(self.baseurl+"projects",params=params).json()
            for _project in _project_list:
                if _project["name"] == name and _project["namespace"]["id"] == _rel[1]:
                    _rel.append(_project["id"])
                    _rel.append(_project["http_url_to_repo"])
                    return _rel           
        return _rel

    def project_list(self):
        for i in range(200):
            params = {"private_token":self.token, "page":i+1}
            project_list_json = requests.get(self.baseurl+"projects",params=params).json()
            if not project_list_json:
                break
            for k in range(len(project_list_json)):
                single_project_info = project_list_json[k]
                single_project_dic = {"repo_id":single_project_info["id"],"repo_name":single_project_info["name"],"repo_group":single_project_info["namespace"]["name"],"repo_description":single_project_info["description"], "repo_url":single_project_info["http_url_to_repo"]}
                self.projects.append(single_project_dic)

    def get_namespaces(self):
        params = {"private_token":self.token}
        return requests.get(self.baseurl+"namespaces",params=params).json()
    
    def search_namespaces(self,namespaces):
        params = {"private_token":self.token,"search":namespaces}
        namespaces_list_json = requests.get(self.baseurl+"namespaces",params=params).json()
        if not namespaces_list_json:
            return (False,"没有 namespaces")
        for _name in namespaces_list_json:
            print(_name,namespaces)
            if _name["name"] == namespaces:
                return [True,_name["id"]]
        return (False,"找不到该 namespace")
