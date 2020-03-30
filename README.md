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