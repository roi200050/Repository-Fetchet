from github import Github

def get_repos(amount):
def is_requirements_exist(repo):
    try:
        repo.get_contents("requirements.txt")
        return True
    except Exception:
        return False
    '''
    The function gets GitHub repos using PyGithub
    param amount: amount of repos
    type amount: Number
    returns Array of repos
    '''

    repos = []

    g = Github()

    repositories = g.search_repositories(query='language:python')

    for repo in repositories:
        repos.append(repo)
        if len(repos) == amount:
            return repos
