docker pull mycroftai/docker-mycroft
docker run -d \
-v config_dir_on_host:/root/.mycroft \
-v skills_dir_on_host:/opt/mycroft/skills \
-e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
-v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
-v ~/.config/pulse/cookie:/root/.config/pulse/cookie \
-p 8181:8181 \
--name mycroft mycroftai/docker-mycroft
docker exec -it mycroft /opt/mycroft/bin/mycroft-msm install https://github.com/cthadeu/msk-test