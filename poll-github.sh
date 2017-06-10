#!/usr/bin/env bash
#
# from here: https://gist.github.com/grant-roy/49b2c19fa88dcffc46ab

DIRPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
INTERVAL=5
ATTEMPTS=2
PWD="$(pwd)"

#while true
#for i in {1.."${ATTEMPTS}"}; do
for i in {1..2}; do

  cd "${DIRPATH}";
  git fetch;
  LOCAL=$(git rev-parse HEAD);
  REMOTE=$(git rev-parse @{u});

  printf "\n\tLOCAL [%s] REMOTE [%s]" "${LOCAL}" "${REMOTE}"

  #if our local revision id doesn't match the remote, we will need to pull the changes
  if [[ $LOCAL != $REMOTE ]]; then
    printf "\n\n\t\tChange\n\n"
    #pull and merge changes
    # git pull origin master;

    #build the new site, you must install jekyll on the server, alternatively you could put the built _site
    #repo under version control and just update based off the changes in that folder. Jekyll outputs build into /_site
    # jekyll build;

    #change back to home directory
    # cd

    # sudo service nginx stop

    #remove current site directory
    #sudo rm -rf /var/www/site.com/public_html;

    #copy the newly built site into the directory nginx will serve it from
    #sudo cp -r a_folder_created_off_home/the_git_repo_folder_you_cloned_in/_site /var/www/site.com/public_html

    # sudo service nginx start;
  fi
  sleep "${INTERVAL}"
done

printf "\n\tDone polling.\n"
[[ -d ${PWD} ]] && cd "${PWD}"
