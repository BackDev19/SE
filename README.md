# softwareEngineering
과제용

------------------------------------------------------
1. 맨처음에 아무 .py파일에 ctrl + F5를 눌러서 python debug console이 실행되게 한다.

2. python debug console에 내가 가상머신을 만들고자 하는 경로로 이동 후에(ex. cd c:\경로), python -m venv venv 입력

3. venv위의 Scripts위치로 이동 cd .../venv/Scripts

4. activate.bat실행 --> activate.bat 입력(가상환경 진입)

5. requirements.txt가 있는 위치로 이동(myproject폴더) --> cd .../myproject

6. 패키지 설치 pip install -r requirements.txt

7. 환경변수 입력

    set FLASK_APP=pybo

    set FLASK_ENV=development

8. 프로젝트 파일(config.py가 있는 위치로 cd)로 이동 cd .../myproject

9. flask run 입력

** sqlite 설치할 것 **
