from githubCommunicator import get_repos, is_requirements_exist
from scoreChecker import get_score

def get_amount_of_repos():
    '''
    The function handle the communication with the user
    __I could use cli library to handle it but for now its just getting one input...__
    __I could also get this parameter when calling the cli__
    '''
    print("Enter amount of repoisories to fetch: ")
    try:
        amount_of_repos = int(input())
        return amount_of_repos
    except ValueError:
        print("Please enter a valid number!")
        print("Exiting...")
        quit()

def print_repo_details(repo_details):
    '''
    The function prints the repo details
    param repo_details: repo details such as author, url, score, etc...
    type repo_details: RepoDetails
    '''
    print("--------------------------------------------")
    print(f'Name: {repo_details.full_name.split("/")[1]}')
    print(f'Author: {repo_details.full_name.split("/")[0]}')
    print(f'Score: {int(repo_details.score*100)}/100')
    print("--------------------------------------------")

def display_repos(repos):
    '''
    The function iterate the repos
    param repos: list of repo details
    type repos: Array of RepoDetails
    '''
    for repo in repos:
        print_repo_details(repo)

def main():
    repo_details = []
    amount_of_repos = get_amount_of_repos()
    #Getting repos details
    repos = get_repos()
    for repo in repos:
        if is_requirements_exist(repo):
            try:
                #Calculating repos score
                repo.score = get_score(repo.clone_url)
                repo_details.append(repo)
                
                if len(repo_details) == amount_of_repos:
                    #Print repos output
                    display_repos(repo_details)
                    return
            except Exception as e:
                print(f'Error while scoring {repo}')



if __name__ == '__main__':
    main()