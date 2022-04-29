import subprocess
import shutil
from git import Repo

FOLDER_TO_CLONE = './project_to_check'
CHECK_REQS_OUTPUT_PREFIX = 'Extra requirements:'

def clone_repo(repo_url):
    '''
    The function clone GitHub repo using GitPython
    param repo_url: url of repo
    type repo_url: Text
    '''
    Repo.clone_from(repo_url, FOLDER_TO_CLONE)

def get_reqs_count():
    '''
    The function count libraries in requirements.txt file
    '''
    return len([line.strip("\n") for line in open(f'{FOLDER_TO_CLONE}/requirements.txt', "r") if line != "\n"])

def get_extra_reqs():
    '''
    The function running reqs check using pip-check-reqs
    '''
    output = subprocess.run(["pip-extra-reqs", FOLDER_TO_CLONE], capture_output=True)
    return len(output.stderr.decode('utf-8').split('\r\n'))-2


def calaulate_score():
    '''
    The function calaulate GitHub repo score
    returns repo's score as Number (0-1)
    '''
    extra_reqs = get_extra_reqs()
    total_reqs = get_reqs_count()
    return (total_reqs - extra_reqs) / total_reqs

    

def get_score(repo_url):
    clone_repo(repo_url)
    score = calaulate_score()
    shutil.rmtree(FOLDER_TO_CLONE)
    return score
print(calaulate_score())