import os
import subprocess
import shutil

FOLDER_TO_CLONE = 'project_to_check'
CHECK_REQS_OUTPUT_PREFIX = 'Extra requirements:'

def clone_repo(repo_url):
    '''
    The function clone GitHub repo using GitPython
    param repo_url: url of repo
    type repo_url: Text
    '''  
    subprocess.run(["git", "clone", repo_url, FOLDER_TO_CLONE])

def parse_reqs_result(output):
    '''
    The function parse pip-check-reqs output
    returns Number of unused packages
    '''
    parsed_output = output.stderr.decode('utf-8').split('\n')
    if parsed_output[0] == CHECK_REQS_OUTPUT_PREFIX:
        return len(parsed_output)-2
    raise Exception(f"Error while running pip-extra-reqs \nException:{output.stderr.decode('utf-8')}")


def get_extra_reqs(repo_url):
    '''
    The function running reqs check using pip-check-reqs
    '''
    output = subprocess.run(["pip-extra-reqs", "."], capture_output=True, cwd=repo_url)
    return parse_reqs_result(output)
    


def calaulate_score(repo_url):
    '''
    The function calaulate GitHub repo score
    returns repo's score as Number
    '''
    extra_reqs = get_extra_reqs(repo_url)
    return f"{extra_reqs}"

    

def get_score(repo_url):
    clone_repo(repo_url)
    try:
    	score = calaulate_score(FOLDER_TO_CLONE)
    except Exception as e:
        print(f'Error while scoring {repo_url}')
        print(e)
        print("----------------------------------------")
    finally:
    	shutil.rmtree(FOLDER_TO_CLONE)
    return score
