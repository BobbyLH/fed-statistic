# fed-statistic
前端工具使用统计服务

## 安装依赖
```shell
sudo apt-get install pipenv

pipenv shell

pipenv install
```

## 初始化数据库
```shell
python setup.py passwd={your_mysql_password}
```

或者

```shell
python setup.py passwd={your_mysql_password} host={mysql_server_host} user={your_mysql_username}
```

## 运行项目开发环境
```shell
python -m flask run
```

打开 http://localhost:5000

## 部署(以 centos 7 为例)
### 修改 yum 源
```shell
cd /etc/yum.repos.d/

# 备份
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup

touch CentOS-Base.repo && vi CentOS-Base.repo

# 填写靠谱的yum源信息
```

### 安装 mysql
```shell
# step1 设置 yum 源
rpm -Uvh https://repo.mysql.com/mysql80-community-release-el7-3.noarch.rpm

# step2 安装
sed -i 's/enabled=1/enabled=0/' /etc/yum.repos.d/mysql-community.repo

# step3 启动mysql服务
service mysqld start

# step4 获取缺省密码
grep "A temporary password" /var/log/mysqld.log

# step5 安装安全的 mysql 服务，并输入刚才获取的密码，而后更改启动密码
mysql_secure_installation

# step6 重启
service mysqld restart

# step7 登陆
mysql -uroot -p

# step8 change the mysql password police
show variables like 'validate_password%';

set global validate_password.length=6;

set global validate_password.policy=low;
```

### 安装 git
```shell
yum install git
```

### 安装 python3.7+
```shell
yum install gcc openssl-devel bzip2-devel libffi-devel wget

yum install -y xz-devel

wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz

tar xzf Python-3.7.5.tgz && cd Python-3.7.5.tgz

./configure --enable-optimizations

make altinstall
```

### 安装 pipenv
```shell
pip3.7 install pipenv

vi ~/.bashrc

# 在末尾处加上
export PATH="$PATH:~/.local/bin"
eval "$(pipenv --completion)"
```

### 安装 gunicorn
```shell
pip3.7 install gunicorn
```

- clone 项目至服务器，而后初始化启动项目
```shell
git clone git@github.com:BobbyLH/fed-statistic.git

cd fed-statistic && pipenv install

python setup.py passwd='{your mysql root password}'

gunicorn -w 2 -b 0.0.0.0:5000 main:server --daemon
```

访问 `ip:5000` 即可看到展示的页面

### 杀掉 gunicorn 进程
```shell
pkill gunicorn
```