## .gitignore

### Accessing the .gitignore file
When you don't want certain files tracked by git, you can specify them in your repo's .gitignore file.  This file is hidden by default on most operating systems so you will either need to use a text editor like [atom](https://atom.io), that will provide a browseable file navigator that displays hidden files.

Another option is to use [Vim](https://www.vim.org).  Vim is accessable through the command line, but you will likely not be familiar with using it.  Here is a [gamified tutorial on using Vim](https://vim-adventures.com).  Once you have cd'ed into your repos main directory you will be able to access your repo's .gitignore using the command `vim .gitignore`.

### Ignoring files using .gitignore

To ignore a specific file, you should add the filename and extension to your file
```
myfiletoignore.txt
```

To ignore an entire direction
```
directory_to_ignore/
```

To ignore all files based on their extensions you should add `*.<extension>` to your file
```
*.csv
```

Detailed [documentation](https://git-scm.com/docs/gitignore) on using .gitignore.





## Git revisions

Code excerpt taken from [gitlab](https://docs.gitlab.com/ee/topics/git/rollback_commits.html)

```
git commit -am "bug introduced"
git revert HEAD
# New commit created reverting changes
# Now we want to re apply the reverted commit
git log # take hash from the revert commit
git revert <rev commit hash>
# reverted commit is back (new commit created again)
```

## The 'elements' of Python

I began to introduce the fundemental aspects of working with Python as an Economist.  The Jupyter Notebook is included in this file directory and named `elements.ipynb`.
