% 移动到ts文件所在目录下再运行 %
% 可按自己意愿修改为不同的视频格式转换 %
% 需要提前配置好ffmpeg系统变量 %
for %%a in (*.ts) do ffmpeg -i "%%~a" -codec copy -f mp4 "%%~na.mp4"
del /a /f /s /q "*.ts"