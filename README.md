---
title: Rtsptrend
emoji: 🐢
colorFrom: purple
colorTo: yellow
sdk: docker
pinned: false
---


├── Dockerfile             # Главен Dockerfile за проекта
├── requirements.txt       # Общи зависимости
├── app.py                 # Основно приложение (FastAPI)
│
├── modules/
│   ├── __init__.py        # Прави директорията пакет
│   │
│   ├── rtsp_capture/      # Модул за RTSP захващане
│   │   ├── __init__.py
│   │   ├── config.py      # Конфигурация на модула
│   │   ├── capture.py     # Логика за захващане на кадри
│   │   └── api.py         # API ендпойнти свързани с модула
│   │
│   ├── image_analysis/    # Модул за AI анализ (в бъдеще)
│   │   ├── __init__.py
│   │   ├── config.py      
│   │   ├── analyzer.py    # AI анализ логика
│   │   └── api.py         
│   │
│   └── weather_data/      # Модул за метеорологични данни (в бъдеще)
│       ├── __init__.py
│       ├── config.py
│       ├── weather.py     # Логика за метеорологични данни
│       └── api.py
│
├── utils/
│   ├── __init__.py
│   ├── logger.py          # Общи логинг функции
│   └── helpers.py         # Помощни функции
│
├── static/                # Статични файлове (CSS, JS, изображения)
│
└── templates/             # Jinja2 шаблони
    ├── base.html          # Основен шаблон
    ├── index.html         # Начална страница
    └── components/        # Преизползваеми компоненти
        ├── header.html
        └── footer.html


