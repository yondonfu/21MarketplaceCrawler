cd ~/.config/systemd/user
systemctl --user enable app-crawler.timer
systemctl --user start app-crawler.timer
systemctl --user start app-crawler.service
systemctl --user daemon-reload
cd ~/app_crawler
