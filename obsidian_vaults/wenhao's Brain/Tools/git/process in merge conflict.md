**Process to merge conflict**
1. if there are conflict at commits to merge, git will not create new merge commit, but will let you resolve the conflict. `git status` show which files are unmerged, after a merge conflict
2. git will add conflict-resolution markers in these files to mark the conflict, we need to manually replace those conflict blocks with new code, and run `git add` to mark it as resolved. (Staging a file marks it as resolved). For example, a conflict block like this will appear in the conflict file    
	```html
	<<<<<<< HEAD:index.html
	<div id="footer">contact : email.support@github.com</div> 
	=======
	<div id="footer">
		please contact us at support@github.com 
	</div>
	>>>>>>> iss53:index.html

	replace by:

	<div id="footer">
		please contact us at email.support@github.com 
	</div>
	```

3. `git commit` to finalize the merge commit