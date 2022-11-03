# 阶段二[Git的学习]

### 1.Git的下载：

在学习之初，直接点击查看了廖雪峰老师的官方学习网站，在Git安装 windowns安装中直接点击下载安装程序安装， 按照步骤默认点击之后，选择GIt bash。之后在使用过程中，又重新安装了一次。

### 2.GIt的使用

#### 2.1.Git名字与邮箱的配置：

1. 在$前缀后输入 git config --global user.name  "name"和git config --global user.email"email@example.com"

2. 在检查配置时，先使用了 cat/git config却并没有正确查看到配置，之后使用git config--list才成功查看出配置。

3. 同时还使用git --version查看了所安装的Git的版本

   ![image-20221103112609690]([learngit/image-20221103112609690.png at main · GitEW45/learngit (github.com)](https://github.com/GitEW45/learngit/blob/main/image-20221103112609690.png)

   ![image-20221103112707552]([learngit/image-20221103112707552.png at main · GitEW45/learngit (github.com)](https://github.com/GitEW45/learngit/blob/main/image-20221103112707552.png)

![image-20221103112440133]([learngit/image-20221103112440133.png at main · GitEW45/learngit (github.com)](https://github.com/GitEW45/learngit/blob/main/image-20221103112440133.png)

#### 2.2.创建版本库

1. 按照步骤，创建了一个新目录

![image-20221103115411840]([learngit/image-20221103115411840.png at main · GitEW45/learngit (github.com)](https://github.com/GitEW45/learngit/blob/main/image-20221103115411840.png)

 2.通过git init命令将该目录变成了Git可以管理的仓库，得到:Initialized empty Git repository in D:/新建文件夹/Git/learngit/.git/

因为并没有在Learngit目录发现.git目录，所以在输入ls  -ah命令后看见：./  ../  .git/

3.先在typora中编写了文件remdam.md，内容是

```
Git is a version control system.
Git is free software.
```

之后将remdam.md文件移动到learngit的目录中，再依次用git add和git commit命令将文件提交到Git本地仓库。

![image-20221103123343895]([GitEW45/learngit (github.com)](https://github.com/GitEW45/learngit/blob/main/image-20221103123343895.png)

### 3.SSH密钥：

1.最开始并没有找到.ssh目录，于是用命令ssh-keygen -t rsa -C"email@example.com"创建了SSH密钥，在用户主目录中顺利找到了.ssh目录。

2.登录Github网站，点击头像框并打开“setting”，点击SHH and GPG keys，点击New SSH key，将公钥（id_rsa.pub内的内容）复制到key，最后Add key，成功添加Key。

### 4.Git本地文件推送到Github

1.按照教程，首先重新建立了一个仓库learngit，在第一次成功关联Git本地仓库和Github远程仓库就是关联的这一仓库，后来被用来推送需要使用的截图。

2.接下来，使用git remote add origin git@github.com:GitEW45/learngit.git关联远程仓库，但都没有成功。之后发现了错误，需要在版本库中打开git bash here,之前都是直接点击打开git bash。

![git bash]([l](https://github.com/GitEW45/learngit/blob/main/屏幕截图 2022-11-03 183508.png)https://github.com/GitEW45/learngit/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202022-11-03%20183508.png

![git bash here](https://github.com/GitEW45/learngit/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202022-11-03%20183601.png

3.由于刚开始与远程仓库Learngit.git关联成功，与Tasks.git仓库关联时关联失败，用git remote  -v查看关联的远程仓库，用git remote rm origin命令删除了关联的Learngit仓库，使用git remote add origin和git push -u origin  master将Git本地文件推送到GIthub远程仓库，在第一次使用git push 时应在第一次回车后等待，输入yes后再回车，不然无法正常关联。这里被推送的文件是已经使用命令提交到Git本地仓库的文件。Hello.md文件就未没有提交到Git本地仓库而没有被推送到远程仓库。

4.git push -u origin **master**中的**master**可以用**main**替换。

5.使用git clone可以对远程仓库进行克隆到Git本地仓库，文件在修改后用git push origin main推送到远程仓库，实现对远程仓库的对应文件进行修改。![5](https://github.com/GitEW45/learngit/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202022-11-03%20190958.png

6.通过对以上内容的摸索学习，成功将Hello.md成功从Git本地文件推送到Tasks.git远程仓库。







