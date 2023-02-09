print("hello world")
Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (abc)
$ git init
Initialized empty Git repository in C:/Users/Acer-i5-860/Desktop/New folder (5)/.git/

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ touch qwertykeyboard.txt

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git add qwertykeyboard.txt

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   qwertykeyboard.txt


Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git commit -m'first commit'
[master (root-commit) e4f9408] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 qwertykeyboard.txt

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git branch newfeature1

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git branch -a
* master
  newfeature1

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git branch newfeature2

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git branch -a
* master
  newfeature1
  newfeature2

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git branch -d newfeature1
Deleted branch newfeature1 (was e4f9408).

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git branch -a
* master
  newfeature2

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git checkout newfeature2
Switched to branch 'newfeature2'

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (newfeature2)
$ git checkout master
Switched to branch 'master'

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git checkout -b newfeature3
Switched to a new branch 'newfeature3'

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (newfeature3)
$ git checkout master
Switched to branch 'master'

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (master)
$ git checkout -b staging
Switched to a new branch 'staging'

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (staging)
$ git merge newfeature3
Already up to date.

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (staging)
$ ^C

Acer-i5-860@Acer-i5-860 MINGW64 ~/Desktop/New folder (5) (staging)
$
