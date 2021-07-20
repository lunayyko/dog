DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movie',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1', #데이터베이스의 IP주소, 이건 각자의 컴퓨터
        'PORT': '3306',
    }
}

SECRET_KEY = '0!o9z-#^tes338bg0(hm3(+qy*v@ri)+=5fy6q(1qy$tu*3=3'