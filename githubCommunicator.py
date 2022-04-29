from github import Github

def get_repos(amount):
    '''
    The function gets GitHub repos using PyGithub
    param amount: amount of repos
    type amount: Number
    '''

    repos = []

    g = Github()

    repositories = g.search_repositories(query='language:python')

    for repo in repositories:
        repos.append(repo)
        if len(repos) == amount:
            break