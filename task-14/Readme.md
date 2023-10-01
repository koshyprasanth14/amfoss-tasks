bandit0

i used the ssh -p command to switch to a remote login.

The ssh command in Linux is used for secure remote login to a remote system. The -p option is used to specify the port number to connect to when establishing an SSH (Secure Shell) session.

I ran the “ls” command to see if I find any useful files. 

The ls command in Linux is used to list the files and directories in the current directory (folder). When you run ls without any arguments, it displays a simple list of the names of files and directories in the current directory.

I read the file using "cat" command.

The cat command in Linux is short for "concatenate" and is primarily used to display the contents of files on the terminal.

bandit01

i used cat ./- to open the file

bandit02

 ran " cat spaces\ in\ this\ filename"  and received the next password

bandit03

I ran "ls -alps" to see all of the files including the hidden ones. 
then i used cat to open the hidden file.

bandit04

i used -find . type -f |xargs file

type -f specifies that the type is file
| this symbol shows that im using another command
xargs file goes through the elements given by find and determines the type of each file.

bandit05

i used find -type f -size 1033c ! -executable

here thefind filters and displays fils with size 1033 bytes and not executable.

bandit06

the command i used was find -user bandit7 -group bandit6 -size 33c

here it filters and shows files with these specific user and group

bandit07

cat data.txt | grep millionth

grep is used to go through every element given by the first comand (cat) and find the word 'millionth'

bandit08

i used sort data.txt |uniq -c

which gave me the sorted list with how many times each key repeats and found the unique one manually.

bandit09

i used cat data.txt | grep "="

bandit10

i used base64 --d data.txt

base64 convetrs bash coe into normal text
