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
        self.project_list()

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
