##  欢迎来到 singboxWebOnDocker

我们注意到缺少一个可在 Docker 上部署的 Sing-Box 代理，并带有用于控制的 Web 面板。因此，singboxWebOnDocker 应运而生。

## 部署
要部署 singboxWebOnDocker，请按照以下步骤操作：

1. 克隆存储库：

    ```bash
    git clone https://github.com/RedSTARO/singboxWebOnDocker.git ; cd singboxWebOnDocker
    ```

2. 构建 Docker 镜像：

    ```bash
    sudo docker build -t singbox_web_on_docker .
    ```

3. 运行 Docker 容器：

    ```bash
    sudo docker run -p 5000:5000 -p 9090:9090 -p 2080:2080 singbox_web_on_docker
    ```

## 用法
1. 通过导航到 `http://localhost:5000` 访问 Web 面板。
2. 在端口 `5000` 上的提供的输入框中输入订阅链接。
3. 等待自动重定向到 `http://localhost:9090` 上的面板。如果在 10 秒内没有发生重定向，请检查日志以查看是否有任何问题。

4. 将客户端配置为将代理地址指向 `localhost:2080` 以进行mixed流量代理。

## 感谢
- [sing-box](https://github.com/SagerNet/sing-box)
- [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe)