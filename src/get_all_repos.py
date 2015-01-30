import sys
import os
from requests import get
from classroom import Classroom

def collect_repos(auth, university, course, get_repos_filepath):

    call_dir = os.getcwd()
    repos_filepath = os.path.join(call_dir, get_repos_filepath, "%s_all_repos" % course)
    if not os.path.isdir(repos_filepath):
        os.makedirs(repos_filepath)
    else:
        if os.listdir(repos_filepath) != []:
            print "There are already repos in this folder, pleace \
                    remove them before cloning new into this folder"
            sys.exit(0)

    org = "%s-%s" % (university, course)
    url_orgs = 'https://api.github.com/orgs/%s' % (org)
    url_repos = 'https://api.github.com/repositories/'
    classroom = Classroom(auth, url_orgs)
    repos = classroom.get_repos()

    # Create the SSH links
    SSH_links = []
    for repo in repos:
        if course in repo['name'].encode('utf-8'):
            r = get(url_repos + str(repo['id']), auth=auth)
            SSH_links.append(r.json()['ssh_url'])

    # Change to destination folder
    os.chdir(repos_filepath)
    
    # Clone into the repos
    for SSH_link in SSH_links:
        result = os.system('git clone ' + SSH_link)
        #print(result)

    # Change back to call dir
    os.chdir(call_dir)
