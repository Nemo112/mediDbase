#!/bin/bash
nm="/usr/share/applications/mediDbase.desktop";
touch  $nm;
chmod 755  $nm;

toi=$(cat <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=mediDbase
GenericName=mediDbase
TryExec=su-to-root
Exec=su-to-root -X -c /opt/mediDbase/main.py
Terminal=false
Icon=/opt/mediDbase/iconst.png
Type=Application
Categories=AudioVideo;Player;Recorder;
Comment=DBase for media drives
EOF
)
printf "%s\n" "$toi" > $nm;
