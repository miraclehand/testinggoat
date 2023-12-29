cat nginx.template.conf \
    | sed "s/DOMAIN/yongeun-superlists-staging.duckdns.org/g" \
    | sudo tee /etc/nginx/sites-available/yongeun-superlists-staging.duckdns.org

sudo ln -s /etc/nginx/sites-available/yongeun-superlists-staging.duckdns.org /etc/nginx/sites-enabled/yongeun-superlists-staging.duckdns.org


cat gunicorn-systemd.template.service \
    | sed "s/DOMAIN/yongeun-superlists-staging.duckdns.org/g" \
    | sudo tee /etc/systemd/system/gunicorn-yongeun-superlists-staging.duckdns.org.service

sudo systemctl daemon-reload
sudo systemctl reload nginx
sudo systemctl enable gunicorn-yongeun-superlists-staging.duckdns.org
sudo systemctl start gunicorn-yongeun-superlists-staging.duckdns.org
