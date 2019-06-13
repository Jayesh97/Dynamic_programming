a = [1,2,0,1,3,0,0,2]
last = len(a)-1
for i in range(last,-1,-1):
    if i+a[i]>=last:
        last = i
print(last==0)

"""
apt install curl
curl -o nginx_signing.key http://nginx.org/keys/nginx_signing.key
apt install gnupg
apt-key add nginx_signing.key
apt install vim


vim /etc/apt/sources.list
## Add official NGINX repository
deb http://nginx.org/packages/ubuntu/ xenial nginx
deb-src http://nginx.org/packages/ubuntu/ xenial nginx


sudo apt-get update
sudo apt-get install -y nginx
apt install systemd

sudo systemctl start nginx
sudo systemctl enable nginx

sudo /etc/init.d/nginx start
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx restart


docker run --name some-nginx -itd -p 8080:80 ubuntu:nginx
docker exec -it some-nginx /bin/bash

sudo /etc/init.d/nginx start
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx restart


docker commit b237d65fd197 newcentos:withapache


tar -xf file.tar.xz



docker login --username=yourhubusername --email=youremail@company.com
docker tag bb38976d03cf yourhubusername/verse_gapminder:firsttry
docker push yourhubusername/verse_gapminder

/etc/resolv.conf

docker cp foo.txt mycontainer:/foo.txt

apt-get install iputils
apt-get install iproute2
apt-get install curl
apt-get install dnsutils
apt-get install tcpdump


dig @192.168.122.1(to specify a specific dns server) google.com

https://www.rootusers.com/12-dig-command-examples-to-query-dns-in-linux/

"""
