/usr/bin/tmux new-session -d -s detect
/usr/bin/tmux set-option -t detect set-remain-on-exit on
/usr/bin/tmux new-windows -d -n 'GPSdetect' -t detect:1 'sudo python /home/pi/kyeocycle/gpskeydetect.py'
