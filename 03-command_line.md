# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwn = show current working directory path  
> > mkdir = creating a directory  
> > rmdir = deleting a directory
> > touch newfile.txt = creating a file using touch command
> > rm filetoremove.txt = deleting a file
> > mv old_file_name.txt new_file_name.txt = renaming a file
> > ls -a = listing hidden files
> > cp file_to_be_copied.txt dest_loc/file_to_be_copied.txt = copying a file from one directory to another
> > 
> > I've been building a linux cheat sheet for a long time.  Here are the first 20 entries out of many
> > 1)  pwd = print working directory
> > 2)  df -h -t = list filesystems and sizes
> > 3)  cat = will print the contents of a file
> > 4)  ls -la = list contents of directory with extra information (-l) and hidden files (-a)
> > 5)  clear = clear terminal
> > 6)  cd = change directory
> > 7)  mkdir = made a folder in your current location
> > 8)  rmdir = delete a folder in your current location
> > 9)  touch = make a file in your current location
> > 10) rm = delete a file in your current location
> > 11) cp -v = copy a file with output telling you what is going on
> > 12) mv = move a file; also allows you to rename the file
> > 13) grep = search a file for something that may be contained within it (words, etc)
> > 14) diff = will compare 2 files and tell you the differences between the two files
> > 15) passwd = to change your current password
> > 16) echo = just displays something on the screen (use $ to let echo now you want to display a variable
> > 17) info = get some info on a command; use control z to get out of info screen
> > 18) less/more = just like cat but after viewing contents of a file it removes the text from the terminal;allow you to page through a file; type in 'q' to go back to the prompt; less allows you to page up and down the file but more only allows you to go down
> > 19) chmod or chown = change the permissions of a file/folder (use u,g,o for user, group, and other plus permissions r,w,x or use the shorthand three digit number of 4 is read, 2 is write, 1 is execute, o is no permissions
> > 20) sha1sum = checksum for a file using the sha1 hash algorithm sha1sum filename | grep checksum from webpage

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls = list all contents in current working directory`
> > `ls -a = list all contents in current working directory including all hidden files`
> > `ls -l = list all contents in current working directory with extra info`
> > `ls -lh = list all contents in current working directory with extra info in human readable form (size in KB)`
> > `ls -lah = list all contents in current working directory with extra info, hidden files, in human readable form`
> > `ls -t = list all content in current working directory sorted by last date modified`
> > `ls -Glp = list all content in current working directory with extra info and all directories having a slash for piping. Seems like the -G flag adds what group membership the files have.`
---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `these are the ones that i use the most`
> > `ls -la`
> > `ls -h`
> > `ls -a`
> > `ls -p`
> > `ls -d`

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `it allows you to pass a bunch of arguments via standard input to a command that does not accept standard input.`
> > `find ./mydir -name "*.pdf" -print | xargs ls`

 

