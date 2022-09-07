# Shell redirections and shortcuts
  - ### 0-hello_world ### - Print “Hello, World”, followed by a new line to the standard output.
  - ### 1-confused_smiley ### -  Display a confused smiley "(Ôo)'.
  - ### 2-hellofile ### - Display the content of the /etc/passwd file.
  - ### 3-twofiles ### - Display the content of /etc/passwd and /etc/hosts.
  - ### 4-lastlines ### - Display the last 10 lines of /etc/passwd.
  - ### 5-firstlines ### - Display the first 10 lines of /etc/passwd.
  - ### 6-third_line ### -  Displays the third line of the file iacta.You’re not allowed to use sed.
  - ### 7-file ### - Create a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) with text Best School ending by a new line.
  - ### 8-cwd_state ### - Writes into the file ls_cwd_content the result of the command ls -la.
  - ### 9-duplicate_last_line ### - Duplicates the last line of the file iacta.
  - ### 10-no_more_js ### - Delete all the regular files (not the directories) with a .js extension present in current directory and all its subfolders.
  - ### 11-directories ### - Counts the number of directories and sub-directories (including hidden) in the current directory.(Without counting current directory)
  - ### 12-newest_files ### - Displays the 10 newest files in the current directory.
    	#### Requirements:

		-One file per line
    	       	-Sorted from the newest to the oldest

  - ### 13-unique ### - Takes a list of words as input and prints only words that appear exactly once.

    		  - Input format: One line, one word
    		  - Output format: One line, one word
    		  - Words should be sorted

  - ### 14-findthatword ### - Display lines containing the pattern “root” from the file /etc/passwd
  - ### 15-countthatword ### - Display the number of lines that contain the pattern “bin” in the file /etc/passwd
  - ### 16-whatsnext ### - Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
  - ### 17-hidethisword ### - Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
  - ### 18-letteronly ### - Display all lines of the file /etc/ssh/sshd_config starting with a letter.
  - ### 19-AZ ### - Replace all characters A and c from input to Z and e respectively.
  - ### 20-hiago ### - Removes all letters c and C from input.
  - ### 21-reverse ### - Reverse input.
  - ### 22-users_and_homes ### - Displays all users and their home directories, sorted by users.Based on the the /etc/passwd file.
  - ### 100-empty_casks ### - Finds all empty files and directories in the current directory and all sub-directories.

    			- Only the names of the files and directories should be displayed (not the entire path)
    			- Hidden files should be listed
   			- One file name per line
    			- The listing should end with a new line
    			- You are not allowed to use basename, grep, egrep, fgrep or rgrep
  
   - ### 101-gifs ###  - Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

     	 	       	 - Hidden files should be listed
    			 - Only regular files (not directories) should be listed
    			 - The names of the files should be displayed without their extensions
    			 - The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
    			 - One file name per line
			 - The listing should end with a new line
    			 - You are not allowed to use basename, grep, egrep, fgrep or rgrep

    -### 102-acrostic ### - An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.

    	 	      - decodes acrostics that use the first letter of each line.

    		      	- The ‘decoded’ message has to end with a new line
    			- You are not allowed to use grep, egrep, fgrep or rgrep
- ### 103-the_biggest_fan ### -  parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

      			- Order by number of requests, most active host or IP at the top
    			- You are not allowed to use grep, egrep, fgrep or rgrep







