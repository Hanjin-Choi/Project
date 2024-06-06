![Logo of the project](./img_for_readme/banner.png)

# SHIN-HAN Finance
This project is final project in Samsung Software Academy for Youth 1st semester.

Leader - Hanjin Choi  
member - Minjun Shin

## Tech stack
### Back-End
![python](https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white)
![django](https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=white)
![openai](https://img.shields.io/badge/openai-412991?style=flat-square&logo=openai&logoColor=white)
![openai](https://img.shields.io/badge/sqlite-003B57?style=flat-square&logo=sqlite&logoColor=white)

### Front-End
![Vue](https://img.shields.io/badge/Vue.3-4FC08D?style=flat-square&logo=Vue.js&logoColor=white)
![vite](https://img.shields.io/badge/vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![html5](https://img.shields.io/badge/html5-E34F26?style=flat-square&logo=html5&logoColor=white)
![css3](https://img.shields.io/badge/css3-1572B6?style=flat-square&logo=css3&logoColor=white)
![javascript](https://img.shields.io/badge/javascript-F7DF1E?style=flat-square&logo=javascript&logoColor=white)
![bootstrap](https://img.shields.io/badge/bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)

## Building

You need two terminals

### first terminal
```shell
cd final-pjt/final-pjt-back  # move to back-end folder

python -m venv venv
source venv/Scripts/activate  # make and active venv

pip install -r requirements.txt  # install libraries required

python manage.py migrate
python manage.py runserver  # run django server
```

### second terminal
```shell
cd final-pjt/final-pjt-front  # move to front-end folder

npm install
npm run dev  # run vue3
```

Then, you can access to main page on http://127.0.0.1:5173

### Initial Configuration

You have to make API Keys in `.env` for
- front
  1. Kakao map
- back
  1. Open AI
  2. Financial Supervisory Service (financial product in Korea)
  3. The Export-Import Bank of Korea (exchange rate data in Korea)

## Features
This project can perform

* Providing details about financial products
* Enabling you to participate in a product
* Calculating the amount of money using the exchange rate
* Locating banks near your current location
* Comunity Page
* Providing financial product recommendations based on your information
* Recommendation chatbot

## Configuration
#### Providing details about financial products
![products](./img_for_readme/products.PNG)

#### Enabling you to participate in a product
![detail](./img_for_readme/detail.PNG)

#### Calculating the amount of money using the exchange rate
![exchange](./img_for_readme/exchange.PNG)

#### Locating banks near your current location
![map](./img_for_readme/map.PNG)

#### Comunity Page
![posts](./img_for_readme/posts.PNG)

#### Providing financial product recommendations based on your information
![recommendations](./img_for_readme/recommendation.PNG)

#### Recommendation chatbot
![chatbot](./img_for_readme/chatbot.PNG)

## Links

API LINKS LIST

- [Kakao Map API](https://apis.map.kakao.com/)
- [Open AI API](https://openai.com/index/openai-api/)
- [Financial Supervisory Service API](https://finlife.fss.or.kr/finlife/main/contents.do?menuNo=700029)
- [The Export-Import Bank of Korea API](https://www.koreaexim.go.kr/ir/HPHKIR020M01?apino=2&viewtype=C&searchselect=&searchword=)
