# ๐ Diary
๋ฉ์์ด์ฌ์์ฐจ๋ผ ๋ฏธ๋ ํ๋ก์ ํธ
<br>
<br>

## ๐ฆ ํ๋ก์ ํธ ์๊ฐ
- ๋๋ง์ ์ฌ์ง ์ผ๊ธฐ์ฅ ์ฌ์ดํธ ๋ง๋ค๊ธฐ
<br>

## โ ๊ธฐ๋ฅ๊ตฌํ ์ฒดํฌ๋ฆฌ์คํธ
- [x] django๋ฅผ ์ด์ฉํ์ฌ ์ผ๊ธฐ์ฅ Create, Read, Delete ๊ตฌํํ๊ธฐ
- [x] Paginator๋ฅผ ์ด์ฉํ์ฌ ํ ํ๋ฉด์ ์ผ๊ธฐ 3๊ฐ์ฉ ๋ณด์ด๊ธฐ
- [x] ๊ตฌ๊ธ social ๋ก๊ทธ์ธ ๊ตฌํํ๊ธฐ
<br>

## โค DEMO
1. ํ ํ๋ฉด
<img src="https://user-images.githubusercontent.com/69155170/125750447-e1619686-fccc-4f17-a915-1e3d3e40d823.gif" width="500px;">
2. ๊ตฌ๊ธ ๋ก๊ทธ์ธ
<img src="https://user-images.githubusercontent.com/69155170/125750047-6af78710-d3b7-4556-a424-ebb5a15ead73.gif" width="500px;">
3. ์ ์ผ๊ธฐ ์์ฑ
<img src="https://user-images.githubusercontent.com/69155170/125750040-1fdd90f5-6538-479e-8473-3f8c46ce0197.gif" width="500px;">
4. ์ผ๊ธฐ ๊ฒ์ ๋ฐ ๋ํ์ผ ํ์ด์ง
<img src="https://user-images.githubusercontent.com/69155170/125750351-0568727b-0f8e-4496-a14f-b68c7bd8a9a7.gif" width="500px;">
<br>

## โ Tech Stack
- Django
- Python3
- HTML, CSS
<br>

## ๐ป ํ๋ก์ ํธ ์คํ๋ฐฉ๋ฒ
1. ํ๋ก์ ํธ clone
- git clone https://github.com/kiteB/Diary.git
2. ๊ฐ์ ํ๊ฒฝ ์์ฑ ๋ฐ ์คํ
- `python -m venv <๊ฐ์ํ๊ฒฝ ์ด๋ฆ>`
- `(Windows) . <๊ฐ์ํ๊ฒฝ ์ด๋ฆ>/Scripts/activate`
3. ํ์ํ ๋ผ์ด๋ธ๋ฌ๋ฆฌ ์ค์น
- `pip install -r requirements.txt`
4. ๋ชจ๋ธ ๋ฑ๋ก
- `python manage.py makemigrations`
- `python manage.py migrate`
5. ๊ด๋ฆฌ์ ์์ฑํ๊ธฐ
- `python manage.py createsuperuser`
6. ์๋ฒ ์คํ
- `python manage.py runserver`
7. ์น ๋ธ๋ผ์ฐ์ ์์ url ์คํ
- 'http://127.0.0.1:8000/admin/' ์ ์ -> ๊ด๋ฆฌ์๋ก ๋ก๊ทธ์ธ
- 'http://127.0.0.1:8000/'์ ์ -> ํ ํ๋ฉด

