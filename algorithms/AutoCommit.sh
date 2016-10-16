now="$(date)"
comment="Commiting changes as of $(date)"

git add -u
git commit -m "$comment"
git push origin master
