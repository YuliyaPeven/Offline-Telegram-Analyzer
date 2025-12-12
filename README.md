# Offline Telegram Analyzer

**Offline Telegram Analyzer** — это локальный инструмент для анализа Telegram-каналов.  
Проект позволяет скачивать последние посты канала, строить статистику, графики и PDF-отчеты, полностью бесплатно, без платных API.

---

## Функционал

- Скачивание последних N постов из любого публичного Telegram-канала.
- Расчет основных метрик:
  - Среднее количество просмотров
  - Средняя длина поста
  - Активные дни недели
- Визуализация:
  - График просмотров по дате
- Генерация PDF-отчета с метриками и графиками

---

## Стек технологий

- **Python 3.10+**
- [Telethon](https://docs.telethon.dev/) — для работы с Telegram
- [Pandas](https://pandas.pydata.org/) — обработка данных
- [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/) — визуализация
- [ReportLab](https://www.reportlab.com/) — генерация PDF

---

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/telegram-analyzer.git
cd telegram-analyzer

Запуск

Используйте CLI для анализа канала:

python main.py --channel t.me/examplechannel --limit 50


--channel — ссылка или username канала

--limit — количество постов для анализа (по умолчанию 50)

После выполнения команды:

views.png — график просмотров

report.pdf — PDF-отчет с метриками

Структура проекта
telegram-analyzer/
│
├── README.md
├── requirements.txt
├── main.py
├── analyzer/
│   ├── __init__.py
│   ├── telegram_scraper.py
│   ├── metrics.py
│   ├── visualization.py
│   └── report.py
├── data/
│   └── sample_data.json
└── tests/
    ├── __init__.py
    ├── test_metrics.py
    └── test_scraper.py

Примеры использования
Получение статистики канала:
python main.py --channel t.me/examplechannel --limit 50
Просмотр графика просмотров:
Получение PDF-отчета:
