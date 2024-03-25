for /f "tokens=* delims=" %%a in ('python --version 2^>^&1') do (
    msg * Python version: %%a
)