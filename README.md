# Github_Scripts
Python scripts to query Github API and complete various tasks

codespaces.py

- Lists all your active codespaces 

- Github website makes this hard/nearly impossible to do unless you use Github CLI or are part of an organization

- Personal Access Token requires "Codespaces" repository permissions (read)

actions.py

- Lists your repositories that have actions (workflows) which are active. If you want this script to also work for your private repositories, you will need to add additional permissions

- This is done via several requests and you may be rate-limited by the Github API

- Additional work and improvements can be made to this script as well (such as going through all repos in a timely fashion)

- Personal Access Token requires:
    
    * "Metadata" repository permissions (read) 

    * "Actions" repository permissions (read)