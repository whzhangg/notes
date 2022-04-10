# Pro Git
Created: September 28, 2021 9:08 PM
Description: Scott Chacon and Ben Straub, 2020
Tags: Git, Programming
## Git introduction
Git is a Distributed Version Control Systems, every client has a full clone of all the data. Everything in Git is checksummed with SHA-1 hash, which is a 40-character string

There are four main states for tracked files in Git:
1. *Modified*: files in working tree, a single version of the project
2. *Staged*: files in the staging area
3. *Committed*: files in Git directory .git
4. *Untracked*: files not seen by Git

**git config file**:
There are three level of config files: 
1. `/etc/gitconfig` 
2. `~/.gitconfig` 
3. `.git/config`

each level of config overwrite the values in the previous level
The configurations used by Git can be shown using commend: 
```bash
git config --list --show-origin
```

## Git Basics
**.gitignore file**
Rules for `.gitignore`, see [[Rule for git ignore file]]

**add**
- Staging a file by `git add` will stage the file as it is at the moment it is stages.

**git diff**
- `git diff` shows what you've changed but not yet staged
- `git diff —staged` shows what you staged that will go into your next commit (`git diff —cached` is the same)

**remove file** 
- `git rm filename` remove the file from the current working tree, and also from the tracked files (staging area).
- `git rm --cached filename` remove the file from the tracked files. To remove file from git, we need to remove it from tracked files and then commit by `git rm`.

**Log and status**
status:
- `git status -s` or `git status --short` show a short summary of status

Log:
- `git log --patch` shows all the difference in the commits
- `git log --stat` shows how much each files are changed `(———+++++++++++++)`
- `git log --pretty=short, full, fuller, oneline` show formated history 
- `git log --pretty=format` formats the output with defined options
- `git log --pretty=format:"%h %s" --graph` graph option show branch history, useful with formatted log. For format specifier and example, see [[Git log formatting]]
- `git log -- path/to/file` will limit the log output to commits that introduce a change to those files, `"--"` separate the path from the options
- `git log -n` shows last n commit
- `git log --since="2020-01-15"` or`--until="2020-01-10"` limit the time log is shown
- `git log --author='whzhangg'` limit the log by authors

**Undo things**

`git commit --amend` let you modify your previous commit, when you forgot to add a file or made a small mistake, the old commit will be replaced by the new commit as if the previous commit never happened. For example:
```shell
git commit -m 'Initial commit' 
git add forgotten_file
git commit --amend
# you end up with a single commit, with the second commit 
# replace the result of th first
```

**Unstage**
- `git restore` restore modified file to its previous version. (usually, git status will show the recommended command to undo the changed)

**Reverting some part of the file**
- `git checkout commit1 file` swap the file in `commit1` to the corrent working directory. using the option `-p` allows you to choose which part to revert. [ref](https://stackoverflow.com/questions/5669358/can-i-do-a-partial-revert-in-git/23401018)

**detached HEAD**
If you make changes and create a commit, the tag will stay the same, but your new commit won't belong to any branch and will be unreachable, except by commit hash. Thus, if we need to make changes (eg, fix bug for an older version) we need to create a new branch by `git checkout -b <branchname> <tag>`.

**Aliases**
creating an alias: `git config --global alias.<c> <command>` creates an alias \<c\> for \<command\>. For example, the command:
```shell
git config --global alias.unstage 'reset HEAD --'
```
will make `git unstage fileA` equivalent to `git reset HEAD -- fileA`

### Working with Remotes
**listing**
- `git remote` list the short names of each remote handles, (origin is the default name of where you cloned from)
- `git remote -v` shows the urls and protocols
- `git remote add <shortname> <url>` adds a new remote repository. Shortname is an alternative of the whole url
- `git fetch <remote>` gets data from the remote repository. It download all the data from that remote project, `git fetch` only downloads all data to the local repository, it does not merge or modify the files in the working tree
- `git pull` automatically fetch and then *merge* that remote branch into your current branch. By default, `git clone` will sets up the local master branch to track the remote master branch (or main)
- `git push <remote> <branch>` will push the chosen branch into the remote repository

**Inspecting Remotes**
- `git remote show <remote>` shows the information, such as which branch is pushed by git push command, etc.

**Renaming Remotes**
- `git remote rename name1 name2` will change the remote's shortname

**Removing Remotes**
- `git remote remove <remote>` will remove a remote, all remote-tracking brancnes and configuration settings associated with it are also removed

### Tags
**Adding tags for current commits**
- `git tag` list existing tags
- `git tag -l "v1.8.5*"` '-l' option use wildcards to match returned tags
- `git tag <tag>` create a *lightweight tag* for the current commit. Lightweight tag is a pointer to a specific commit
- `git tag -a <tag> -m "version 1.2"` created an *annotated tag*. Annotated tags are similar to a commit in that they contain tag messenger, tagger name, emails and they are checksummed
- `git tag <tag> <hash>` tags a previous commit
- `git tag -d <tag>`: delete a tag (locally)

**Remote tags**
we need to explicitly push tags to a remote repository after they are created, both kinds of tag will be pushed (lightweight, annotated):
- `git push origin <tagname>` push a specific tags
- `git push origin --tags` push all the tags
- `git push origin --delete <tagname>` delete a remote tag

**Check out a tag**
- `git checkout <tag>` will let you view previous tags

## Commits and Branching
> git encourage workflow that branch and merge often.
> It is most important to remember that commits are the "snapshot" of the states of the files: *branches, heads etc. are just pointers*.

**Commit**
commit is represented by a commit object, which contains a pointer to the directory tree, commit information (author, time) and pointers to commit or commits directly came before this commit. 
![[commit_structure.png|500]]


**Branch**
A branch in git is simply a *lightweight movable pointer* to one of the **successive commits** (a simple file containing the SHA-1 checksum of the commit it points to). Git will initiate a default branch (master or main), but they are not different from other branches

- `git branch <newbranch>` create a new branch *pointing* to the current commit (a new pointer to move around). **Therefore, branches are separate from commits**
- `git branch -d <branch>` delete a existing branch: the pointer is deleted, the commits are not deleted but they can no longer be refered by a branch

It is safe to delete branch once they are merged: as in the following case, iss53 branch is merged into master. since a branch is just a pointer, iss53 is no longer necessary, master branch keep track of all its previous commits, including everything from C3 to C5. commit and merge history can be displaced with `--graph` option of `git log`
![[branch_path.png|500]]
git will issue warning message when attempting to delete unmerged branches

**HEAD**
HEAD is a *special pointer* to the *local branch* you are currently working on. `git log` shows the HEAD and branch: `commit 40a580a50af73c217c878b6a8446848b3390b1f0 (HEAD -> main, origin/main, origin/HEAD)`

**Switching branches**
- `git checkout -b <newbranch>` create and switch to a new branch.
- `git checkout <branch>` switch to an existing branch, which *move the head to \<branch\>*. git will generally refuse to switch branch if there are uncommitted changes. 
- By default, git log shows the history of the current branch, `git log <branchname>` shows log for other branch

commiting at a checked branch will move this branch forward with commits (a branch is a separate line of development)

**git switch** can be used instead of `git checkout` to: 
- switch to an existing branch `git switch <branch>`
- create a new branch and switch to it `git switch -c <new-branch>`
- return to previously checked out branch `git switch -`

**Merging**
Suppose we are on branch master and a new branch is created from the commit:
```bash
git checkout -b 'fix'
git commit
```

to merge fix with master, we switch backinto master and merge:
```bash
git checkout master
git merge fix
```

The merge will be a *fast forward merge*, since the latest commit of branch fix directly follows the latest commit of branch master, so it will simply point master to the current commit.

Suppose we have another branch that is parallel to master. the development history has diverged, git will attempt to perform a *three way merge* (two commits pointed to by the branch tips and their common ancestor). In this case, git will create a new commit, called "merge commit" that result from the three way merge. this commit will have more than one parent. See [[process in merge conflict]] on how to perform a three way merge. 
    
**Branch Management**
- `git branch` list all the local branches.
- `-v` option shows the last commit, `*` points to the head, `--merged` and `--no-merged` option filter the branches you have or have not merged into the branch.
- `git branch --move <oldbranch> <newbranch>` renames a local branch
- to make the same changes to remote branch, we first push `git push --set-upstream origin <newbranch>`. the command will push \<newbranch\> to origin repository. now both \<newbranch\> and \<oldbranch\> exist on the remote. We delete the old one: `git push origin --delete <oldbranch>`

**Managing Remote branches**
On the remote repositories, there are remote pointers including branches, tags and so on.
Remote tracking branches are references to the state of remote branches, they cannot be changed locally and *represent the states of the remote branches at last connection (see figure below). The name of the remote tracking branch is in the form \<remote\>/\<branch\>*. 

![[with_remote.png|500]]

`git fetch <remote>` syn the remote repository, updates the local copy and move the origin/master pointer up to date

![[fetch_origin.png|500]]

**Pushing**

`git push <remote> <branch>`, which push the local <branch> to update the remote's <branch>

if the local branch is not tracking any remote branch, `git push <remote> <branch>` will add <branch> to remote, but will not set up upstream branch.

to set upstream at the same time, use `git push --set-upstream`

`git push <remote> <branch1>:<branch2>` will push the local <branch1> to <branch2> on the remote repository. the first case is an automatic expansion of the second command <branch> → <branch>:<branch>

**Only local branches is editable**, as a above figure show, when you just fetch the remote branch, remote/master is points to another commit

we can either merge: `git merge origin/master`

or we can make a local branch that copy origin/master: `git checkout -b localmaster origin/master` , in this case, we make a new branch pointer pointing to the commit, further change will move our local pointer along the development but the origin/master will stay where it is until next fetch

`git checkout -b <branch> <remote>/<branch>`  from a remote branch automatically create tracking branch. **Tracking branch are local branches** that is linked to a remote branch. On a tracking branch, git pull will automatically where to fetch and which branch to merge 

`git checkout —track origin/<branch>` set a local tracking branch from the branch on the server

`git checkout <branch>` will also attempt to create a tracking branch if the branchname does not exist locally but match the one on the remote. 

`git checkout -b <localname> origin/<branch>` will create a tracking branch called <localname>

`git branch -u origin/<branch>` will change the upstream branch currently tracking (`-u` or `--set-upstream-to` ) **If the current branch is not tracking any upstream branch, we can also use it (`--set-upstream-to`) to set the tracking**

`git branch --unset-upstream` will stop the current branch tracking its upstream branch. ([Ref](https://stackoverflow.com/questions/3046436/how-do-you-stop-tracking-a-remote-branch-in-git))

`git branch -vv` shows all tracking branches you have setup

**Pulling**

`git pull` is just a combination of `git fetch` followed by `git merge`

**Deleting remote branches**

`git push <server> --delete <branch>` will delete a remote branch, which remove the pointer on the remote repository

**Prune**

If remote branches are deleted, but still showing in `git branch -a`, it indicates that we still have local copy of the deleted remote branch. 

In this case, we can use `git remote prune <remote>`  

- Reference
    
    [https://stackoverflow.com/questions/5094293/git-remote-branch-deleted-but-still-it-appears-in-branch-a](https://stackoverflow.com/questions/5094293/git-remote-branch-deleted-but-still-it-appears-in-branch-a)
    

 

**Rebase**

git rebase offer another way to combine two branches, by tracking the changes up to a common ancestor, and applying all the changes to another branch
	
![[rebase_1.png|500]]

`git checkout experiment`

`git rebase master`

git will remember all the changes from C2 → C4, and apply the same changes to the branch C3 (to rebase upon), 


![[rebase_2.png|500]]

But the commit history of C4 will be lost, it is as if you switch to branch master, manually modified C3 so that it look like C4 and do a commit. The branch history of experiment will therefore change (single parent). which will not happend in the case of merge since merge will remember two parents and all their commits