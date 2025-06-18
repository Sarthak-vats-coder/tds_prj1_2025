# Lost data in laptop while working on Git bash
_Slug: _

---
**Post ID:** 627925  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/lost-data-in-laptop-while-working-on-git-bash/175382/1  

while solving the 18th question


Download q-list-files-attributes.zip and extract it. Use `ls` with options to list all files in the folder along with their date and file size.


What’s the total size of all files at least 16 bytes large and modified on or after Fri, 18 Jul, 1997, 4:43 am IST?


i even cant recall that what exactly code i wrote in git bash due to which this happened as i  was trying many times …


but i think i did some mistake with directory selection again i am not very sure as  simultaneously i was also working on  powershell and colab…


my data in downloads desktop documents is completely lost …its completely blank


plz if  anyone have any idea to retrive my data please do support…i was having many important documents there.. .

---
**Post ID:** 628228  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/lost-data-in-laptop-while-working-on-git-bash/175382/2  

It may have merged with the extracted folder. Check if any new folder was created in the process.

---
**Post ID:** 628374  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/lost-data-in-laptop-while-working-on-git-bash/175382/3  

this is very good reason to work in wsl instead of directly on your local machine. git bash I presume is a direct install on windows (a bash terminal for windows). bash is a very powerful tool and has to be used with care. unless you really know what you are doing, it is far better to work in isolated VMs like wsl or other similar setups or containers. It may be recoverable, but for future make sure you have regular backups of your work in the cloud like on OneDrive or Google Drive. Then recovery from fatal erasures is trivial.


As far as how to recover the files totally depends on what happened and if you have any recovery systems in place. It is hard to give generic advice without knowing your system. If there is Roll back or File History in your system it is quite possible to recover the files. Or if your work is all within OneDrive for example.


Kind regards

---
**Post ID:** 628380  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/lost-data-in-laptop-while-working-on-git-bash/175382/4  

![That's a simple image of a white uppercase letter "K" centered on a slate-gray background.
](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/kritika0806/48/13610_2.png) kritika0806:

i even cant recall that what exactly code i wrote in git bash due to which this happened




You should take a look at your bash history. That might offer some clues as to what happened.


`history | tail` should give you the last 10 commands you ran.

---
**Post ID:** 635774  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/lost-data-in-laptop-while-working-on-git-bash/175382/5  

many folders were created but none of them has my laptop data..

---
**Post ID:** 635775  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/lost-data-in-laptop-while-working-on-git-bash/175382/6  

command not found


it got erased…

---
**Post ID:** 635778  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/lost-data-in-laptop-while-working-on-git-bash/175382/7  

to the best of my abilities till now i am unable to backup it …


but this taught me great things.

---
**Post ID:** 635779  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/lost-data-in-laptop-while-working-on-git-bash/175382/8  

Try TestDisk.


TestDisk is a tool for recovering files which have been deleted.


`Install testdisk
Enter testisk into the command line, and the utility will start.
Select your partition to search in.
Select quick search or deeper search.
testdisk will output which files have been recovered and then you can decide to recover or not.`
A tutorial on testdisk at the following link, [How to Install TestDisk on Linux and Recover Deleted Files | DigitalOcean](https://www.journaldev.com/36700/how-to-install-testdisk-on-linux-and-recover-deleted-files)


Also available on Windows, don’t know the steps though.

