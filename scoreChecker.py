import os
import subprocess
import shutil
from git import Repo

BASE_FOLDER = 'projects_to_check/'
CHECK_REQS_OUTPUT_PREFIX = 'Extra requirements:'

#if os.path.exists(BASE_FOLDER) and os.path.isdir(BASE_FOLDER):
    #shutil.rmtree(BASE_FOLDER)

def remove_special_chars(text):
    return ''.join(e for e in text if e.isalnum()) 


def clone_repo(repo_url):
    '''
    The function clone GitHub repo using GitPython
    param repo_url: url of repo
    type repo_url: Text
    '''
    folder_path = BASE_FOLDER + remove_special_chars(repo_url.split('/')[-2])   
    subprocess.run(["git", "clone", repo_url, folder_path])
    return folder_path

def get_reqs_count(repo_url):
    '''
    The function count libraries in requirements.txt file
    '''
    return len([line.strip("\n") for line in open(f'{repo_url}/requirements.txt', "r") if line != "\n"])

def get_extra_reqs(repo_url):
    '''
    The function running reqs check using pip-check-reqs
    '''
    output = subprocess.run(["pip-extra-reqs", "."], capture_output=True, cwd=repo_url)
    parsed_output = output.stderr.decode('utf-8').split('\r\n')
    if parsed_output[0] == CHECK_REQS_OUTPUT_PREFIX:
        return len(parsed_output)-2
    raise Exception(f"Error while running pip-extra-reqs \nException:{output.stderr.decode('utf-8')}")


def calaulate_score(repo_url):
    '''
    The function calaulate GitHub repo score
    returns repo's score as Number (0-1)
    '''
    extra_reqs = get_extra_reqs(repo_url)
    total_reqs = get_reqs_count(repo_url)
    return (total_reqs - extra_reqs) / total_reqs

    

def get_score(repo_url):
    folder_path = clone_repo(repo_url)
    #try:
    score = calaulate_score(folder_path)
    # finally:
    #     shutil.rmtree(FOLDER_TO_CLONE)
    return score