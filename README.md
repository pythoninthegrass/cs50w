# CS50 Web Programming with Python and JavaScript


## Summary
From the [course authors](https://cs50.harvard.edu/web/2020/):
> This course picks up where CS50x leaves off, diving more deeply into the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Django, React, and Bootstrap. Topics include database design, scalability, security, and user experience. Through hands-on projects, students learn to write and use APIs, create interactive UIs, and leverage cloud services like GitHub and Heroku. By semester’s end, students emerge with knowledge and experience in principles, languages, and tools that empower them to design and deploy applications on the Internet.

**Table of Contents**
* [CS50 Web Programming with Python and JavaScript](#cs50-web-programming-with-python-and-javascript)
  * [Summary](#summary)
  * [Setup](#setup)
  * [Usage](#usage)
  * [Troubleshooting](#troubleshooting)
  * [Submissions](#submissions)
  * [TODO](#todo)
  * [Further Reading](#further-reading)

## Setup
* Install
    * [editorconfig](https://editorconfig.org/)
    * [asdf](https://asdf-vm.com/guide/getting-started.html#_2-download-asdf)
    * [poetry](https://python-poetry.org/docs/)
    * [docker-compose](https://docs.docker.com/compose/install/)
    * [k9s](https://github.com/derailed/k9s#installation)
    * [minikube](#kubernetes-k8s)
    * [helm](https://helm.sh/docs/intro/install/)
    * [devspace](https://devspace.sh/docs/getting-started/introduction)

## Usage
* [k9s](markdown/kubernetes.md#k9s)
* Minikube
    ```bash
    # install
    brew install minikube

    # set cluster driver permanently
    minikube config set driver docker

    # options
    minikube start --memory=2048 --cpus=2 -p minikube

    # profile list
    minikube profile list
    ```

## Troubleshooting
* `no such table: auctions_listing`
    ```bash
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc" -delete
    rm db.sqlite3
    python manage.py makemigrations
    python manage.py migrate
    python manage.py migrate --run-syncdb
    ```
    [python - "no such table" exception - Stack Overflow](https://stackoverflow.com/a/58362169)

## Submissions
* See [CS50W Projects](https://cs50.harvard.edu/web/2020/projects/) for details
    ```bash
    # create branch from spec (e.g., project 0: search)
    git checkout -b web50/projects/2020/x/search

    # add remote origin
    git remote add origin https://github.com/me50/USERNAME.git

    # move all relevant files to tld
    mv index.html image.html advanced.html styles.css ../../..

    # commit files
    git commit .

    # commit files and skip pre-commit
    git commit -m "search mvp" -m "Other than .dotfiles, just the project 0 website content" --no-verify

    # push to me50 repo
    git push -u origin https://github.com/me50/USERNAME.git
    ```

## TODO
* ~~Switch out DevSpace default image in `devspace.yaml`~~
* ~~Refactor [advanced.html](app/project/0/advanced.html) to match [Google Advanced Search](https://www.google.com/advanced_search)~~
* Go over [sanic](https://sanic.dev/en/) as ad hoc stand-in for stdlib http server

## Further Reading
[CS50's Web Programming with Python and JavaScript | edX](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript)

[Config Reference | DevSpace | Documentation](https://www.devspace.sh/docs/configuration/reference)
