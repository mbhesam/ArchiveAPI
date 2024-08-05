FROM docker.arvancloud.ir/nginx:latest
COPY nginx.conf /etc/nginx/nginx.conf
COPY archiveAPI.nginx.conf /etc/nginx/sites-available/archiveAPI.nginx.conf
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/archiveAPI.nginx.conf /etc/nginx/sites-enabled/
CMD ["nginx", "-g", "daemon off;"]
