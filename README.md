# softwareEngineering
과제용

------------------------------------------------------
1. 맨처음에 ctrl + F5를 눌러서 python debug console이 실행되게 한다.
1. python debug console에 python -m venv venv 입력
2. venv위의 Scripts위치로 이동 cd .../venv/Scripts
3. activate.bat실행 --> activate.bat 입력(가상환경 진입)
4. requirements.txt가 있는 위치로 이동(myproject폴더)
4. 패키지 설치 pip install -r requirements.txt
5. 환경변수 입력
set FLASK_APP=pybo
set FLASK_ENV=development
6. 프로젝트 파일(config.py가 있는 위치로 cd)로 이동 cd .../myproject
7.flask run 입력
