# ЛР9 — автотесты в CI/CD (GitHub Actions)

Автотесты из предыдущих лабораторных работ по дисциплине «Тестирование программного обеспечения»,
которые автоматически запускаются в GitHub Actions при каждом push в ветку `main`.

## Состав

- `calculator.py` — класс `Calculator` (ЛР6);
- `tests/test_calculator.py` — модульные тесты класса `Calculator` (ЛР6, 51 проверка);
- `tests/test_api.py` — тесты REST API JSONPlaceholder на `requests` (ЛР5, 4 теста);
- `.github/workflows/run-tests.yml` — настройка GitHub Actions.

## Локальный запуск

```
pip3 install -r requirements.txt
python3 -m pytest -v
```

Автор: Дрозд Ксения, группа 231-335
