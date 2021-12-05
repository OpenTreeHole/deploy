# Open Tree Hole 部署指南

## 前置需求

你需要域名、SSL 证书和服务器，建议将项目部署在独立的云服务器或 VPS 上，方便运维管理

## docker 部署

使用 docker compose ，项目可以轻松地安装部署

1. 下载 [docker-compose.yaml](https://github.com/OpenTreeHole/deploy/blob/master/docker-compose.yaml)
   
   ```shell
   wget https://github.com/OpenTreeHole/deploy/blob/master/docker-compose.yaml
   ```

2. 在 `docker-compose.yaml` 同目录下创建 `.env` 文件，并将 docker-compose 所需的环境变量逐行填列。完整的配置项列表及说明请参见
   [配置文档](https://github.com/OpenTreeHole/deploy/wiki/配置文档)
   
   ```shell
   nano .env
   ```
   
3. docker compose 部署
   
   请确保机器的 80 和 443 端口没有被占用
   
   ```shell
   docker-compose up -d
   ```

4. 放置机密文件

   项目机密文件（比如 SSL 证书等）储存于 secrets 卷中，一般来说，它位于 /var/lib/docker/volumes/treehole_secrets/_data
   完整的机密文件列表及说明请参见
   [机密文件](https://github.com/OpenTreeHole/deploy/wiki/配置文档#机密文件)
   
若成功，项目可以通过域名访问

## 注意

项目初始化时会自动创建管理员账户，邮箱为 admin@opentreehole.org，密码为 admin，须尽快登录至管理后台修改管理员信息
