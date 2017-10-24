# Programming Tools Project

In this project, we'll be making a realtime system monitoring tool, which can spy on a system anonymously and send to the tracker, the system's data and actions over the internet. This project will be primarily implemented in **C/C++** and **Python3**. We'll use tools like **make**  and **PyBuilder** for build automation.



## Brief Overview of the structure

The tool will consist of two major components - 
* A **server API**, which will grab the actions and data from all the multiple PC's which we are monitoring and display the data appropriately.
* A **trojan horse** which will be injected into the victim's PC for monitoring purposes.

The linux server will host scripts in PHP. The backend model will deploy a MYSQL database which will hold the logs from the victim PC's. The trojan horse will run several python and C scripts on the victim's machine and transfer the sensitive data to our servers.

For demonstration purposes, we'll be using a sub-domain on Harshit's [Private Server](https://arachnis.org), the end-point to which is [https://apps.arachnis.org/pt-project/](https://apps.arachnis.org/pt-project/). However, for testing, we will be simulating this in XAMPP's local server, which has the same configuration as any other linux server.



## Development Guidelines

If you are well-versed with Git VCS (Version Control System), the repository is divided into several branches. So, we'll be making separate branches for our work, and will merge it with our **master** branch, only when the code and build is stable. *Noone will directly push to the master branch*, as all the changes will be reviewed by each of us before implementation.


### How to start ? (For Divya and Gaurav)

1. Fork this repository to your account.

2. Once forked, open cmd/terminal/git bash on your computer and type `git clone https://github.com/YOUR_GITHUB_HANDLE/PT-Project.git` and press enter. This will clone the repo from your github account to your computer. Note that, this will be your copy of the complete code.

3. Now, on `YOUR_GITHUB_HANDLE/PT-Project`, create a new branch with your desired name. This will be done on Github and not on your computer.

4. After a branch is created on Github, you need to import that new branch on your computer. Open cmd/terminal/git bash and navigate to the project's folder. In there, type `git fetch` and press enter. In the output, you'll see a new branch.

5. Now, if you write `git status`, it'll show you on which branch you are on, currently. To switch branches, write `git checkout BRANCH_NAME` and press enter. Now, you'll be on your desired branch.


> **Once you are on your desired branch, make necessary changes or code there.**

6. To implement that code in our main code, your first push the changes to your Github account. To do this, write `git add .`, `git commit -m "ANY_MESSAGE"` and finally `git push origin BRANCH_NAME`.

7. After this, open the branch on Github and create a pull request considering the **base fork** as *harshitbudhraja/master* and **head fork** as *YOUR_GITHUB_HANDLE/BRANCH_NAME*.
