We can use `git log pretty=format:" " ` to format git log outputs

For example:
```shell
git log --pretty=format:"%h - %an, %ar : %s"
>>> ca82a6d - Scott Chacon, 6 years ago : Change version number 
>>> 085bb3b - Scott Chacon, 6 years ago : Remove unnecessary test 
>>> a11bef0 - Scott Chacon, 6 years ago : Initial commit
```

The format specifier is given as the following table:

Specifier  |   Description
--- | --------
%H  |  Commit hash 
%h  | Abbreviated commit hash
%T  | Tree hash
%t  |  Abbreviated tree hash
%P  |  Parent hashes
%p  |  Abbreviated parent hashes
%an |  author name
%ae |  author email
%ad |  author date
%ar | auther relative date
%cn |   committer name
%ce | committer email
%cd |  committer date
%cr |  committer relative date
%s  |  subject
