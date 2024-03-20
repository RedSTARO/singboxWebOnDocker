# **Welcome to singboxWebOnDocker**

### Language / 语言
- [English](README.md) (Default)
- [中文](README-cn.md)


We have noticed the absence of a Sing-Box agent deployable on Docker with a web panel for control. Hence, singboxWebOnDocker has emerged.

## Deployment
To deploy singboxWebOnDocker, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/RedSTARO/singboxWebOnDocker.git ; cd singboxWebOnDocker
    ```

2. Build the Docker image:

    ```bash
    sudo docker build -t singbox_web_on_docker .
    ```

3. Run the Docker container:

    ```bash
    sudo docker run -p 5000:5000 -p 9090:9090 -p 2080:2080 singbox_web_on_docker
    ```

## Usage
1. Access the web panel by navigating to `http://localhost:5000`.
2. Enter the subscription link in the provided input box on port `5000`.
3. Wait for automatic redirection to the panel at `http://localhost:9090`. If no redirection occurs within 10 seconds, check the logs for any issues.

4. Configure your client to point the proxy address to `localhost:2080` for mixed traffic.

## Thanks
- [sing-box](https://github.com/SagerNet/sing-box)
- [sing-box-subscribe](https://github.com/Toperlock/sing-box-subscribe)