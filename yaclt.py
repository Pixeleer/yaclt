import sys
import os
try:
    import requests
except:
    print('Requests import not found, installing...')
    os.system(f'{sys.executable} -m pip install requests')

if os.path.exists('yaclt_repos.txt') != True:
    print('Repos file not found. Creating... ')
    f = open('yaclt_repos.txt', 'w')
    f.close()

if os.name == 'nt':
    osindent = 'NT'
else:
    osident = 'UNIX'

savelocation = ''

args = sys.argv[1:] 

if args[0] == 'get':
    if args[2:] == True:
        for arg in args[2:]:
            if arg == '-global' or '--global':
                osident = 'GLOBAL'
            elif arg == '-savelocation' or '--savelocation':
                savelocation = input('Enter save location: ')
            else:
                print(f'Bad argument "{arg}"')
    
    try:
        with open('yaclt_repos.txt', 'r') as f:
            f2 = f.readlines()
            for line in f2:
                f2 = f2.replace('\n', '')
                print(f'Attempting to get from repo {line}...')
                try:
                    r = requests.GET(f'{line}/static/{osident}/{args[2]}')
                    if r.status_code != '200':
                        print(f'    Package not found in {f2}')
                        continue
                    if os.path.exists(savelocation+'package-'+f2):
                        _ = input('The file you are attempting to download already exists. Would you like to replace it? [y]/[n]')
                        if _ == 'y':
                            print('Continuing with replacing the file...')
                            os.remove(savelocation+'package-'+f2)
                        else:
                            print('Task completed.')
                            sys.exit()
                    print('    Downloading file...')
                    open('package-'+f2, 'w').write(r.content)
                    print('Task completed.')
                    sys.exit()
                except:
                    print('    Repo didn\'t respond.')
    except Exception as e:
        print(f'Error downloading package. {e}')

if args[0] == 'addrepo':
    if args[1] != True:
        print('Repo address not passed. Aborting...')
        sys.exit()

    with open('yaclt_repos.txt', 'a') as rf:
        rf.write(f'{args[1]}\n')
        print('Repo added.')

    print('Task completed.')
    sys.exit()