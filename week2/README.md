# Summary 

## Installition of git

1. Installed git see [guide](https://github.com/seidelj/python-course/wiki/Github-Guide).

2. Created github.com account

## Working with git and github

For creating github repos so the wiki's [github guide](https://github.com/seidelj/python-course/wiki/Github-Guide).  In general once, once you have created a github repo
your workflow will be as follows.

1. Navigate to your git repo's project folder through iTerm or Anaconda PS Prompt. For example

```
cd helloworld
```

2. Check the status of the git repo on your local machine. 

```
git status
>On branch main
>nothing to commit, working tree clean
```

3. Retrieve any updates from the remote server (github.com).
```
git pull origin master
```

4. Make your changes locally.  (Adding files or modifying code)

5. Add the changes to your local machine's git.

```
git add . --all
git commit -m "short description of changes"
```

6. Push the changes to the remote server (github.com)
```
git push origin master
```
