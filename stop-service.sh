cd ~/.config/systemd/user
systemctl --user stop app-crawler.timer
systemctl --user disable app-crawler.timer
systemctl --user stop app-crawler.service
cd ~/app_crawler
