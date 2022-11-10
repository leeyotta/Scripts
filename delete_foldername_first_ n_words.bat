@echo off&setlocal enabledelayedexpansion
set /p str=please input deletenum:
for /d %%i in (*) do (
   set "a=%%i"
   echo %str%|findstr "-" >nul 2>nul&&set "b=!a:~0,%str%!"||set "b=!a:~%str%!   
   ren "%%i" "!b!"
)
pause