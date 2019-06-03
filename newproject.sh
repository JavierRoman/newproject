#!/bin/bash
python create_remote_repo.py $1
mkdir ~/Projects/$1
cd ~/Projects/$1
echo "# $1" >> README.md
touch .gitignore
git init
git add README.md
git commit -m "First commit"
git remote add origin https://github.com/JavierRoman/$1.git
git push -u origin master
code .