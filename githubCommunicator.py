from github import Github

def is_requirements_exist(repo):
    try:
        repo.get_contents("requirements.txt")
        return True
    except Exception:
        return False

def get_repos():
    '''
    The function gets GitHub repos using PyGithub
    param amount: amount of repos
    type amount: Number
    returns Instance of repos
    '''

    g = Github("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")

    return g.search_repositories(query='language:python')
