# 📝 Diary
멋쟁이사자차럼 미니 프로젝트
<br>
<br>

## 🦁 프로젝트 소개
- 나만의 사진 일기장 사이트 만들기
<br>

## ✔ 기능구현 체크리스트
- [x] django를 이용하여 일기장 Create, Read, Delete 구현하기
- [x] Paginator를 이용하여 홈 화면에 일기 3개씩 보이기
- [x] 구글 social 로그인 구현하기
<br>

## ❤ DEMO
1. 홈 화면
<img src="https://user-images.githubusercontent.com/69155170/125750447-e1619686-fccc-4f17-a915-1e3d3e40d823.gif" width="500px;">
2. 구글 로그인
<img src="https://user-images.githubusercontent.com/69155170/125750047-6af78710-d3b7-4556-a424-ebb5a15ead73.gif" width="500px;">
3. 새 일기 작성
<img src="https://user-images.githubusercontent.com/69155170/125750040-1fdd90f5-6538-479e-8473-3f8c46ce0197.gif" width="500px;">
4. 일기 검색 및 디테일 페이지
<img src="https://user-images.githubusercontent.com/69155170/125750351-0568727b-0f8e-4496-a14f-b68c7bd8a9a7.gif" width="500px;">
<br>

## ✏ Tech Stack
- Django
- Python3
- HTML, CSS
<br>

## 💻 프로젝트 실행방법
1. 프로젝트 clone
- git clone https://github.com/kiteB/Diary.git
2. 가상 환경 생성 및 실행
- `python -m venv <가상환경 이름>`
- `(Windows) . <가상환경 이름>/Scripts/activate`
3. 필요한 라이브러리 설치
- `pip install -r requirements.txt`
4. 모델 등록
- `python manage.py makemigrations`
- `python manage.py migrate`
5. 관리자 생성하기
- `python manage.py createsuperuser`
6. 서버 실행
- `python manage.py runserver`
7. 웹 브라우저에서 url 실행
- 'http://127.0.0.1:8000/admin/' 접속 -> 관리자로 로그인
- 'http://127.0.0.1:8000/'접속 -> 홈 화면

