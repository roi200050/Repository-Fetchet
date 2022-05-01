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
