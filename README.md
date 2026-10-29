# 42 Python Projects

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![42](https://img.shields.io/badge/42-Kocaeli-000000?style=flat-square&logo=42&logoColor=white)

42 Kocaeli Python müfredatında tamamladığım modüller. Temel sözdiziminden
OOP'ye, hata yönetiminden dosya işlemlerine, sanal ortamlardan fonksiyonel
programlamaya kadar uzanıyor. Her modül kendi klasöründe, her egzersiz de
`exN/` alt klasöründe duruyor.

> Modüller önceden ayrı repolardaydı; commit geçmişleri korunarak bu repoda birleştirildi.

## Modüller

| Modül | Konu | Öne çıkanlar |
| --- | --- | --- |
| [Python_00](Python_00) | Python temelleri | Değişkenler, input/print, koşullar, döngüler, iteratif ve recursive fonksiyonlar |
| [Python_01](Python_01) | Nesne yönelimli programlama | Sınıflar, constructor, encapsulation, kalıtım, factory yapısı |
| [Python_02](Python_02) | Hata yönetimi | `try`/`except`, `raise`, farklı hata türleri, özel exception sınıfları, `finally` |
| [Python_03](Python_03) | Veri yapıları | `sys.argv`, list, tuple, set, dict, generator'lar, comprehension'lar |
| [Python_04](Python_04) | Dosya işlemleri | Dosya okuma/yazma, stdin/stdout/stderr akışları, context manager (`with`) |
| [Python_05](Python_05) | Soyut sınıflar ve polimorfizm | `abc` ile soyut sınıflar, veri işleme pipeline'ı |
| [Python_08](Python_08) | Ortam yönetimi | Sanal ortamlar, pip ve Poetry, `.env` ile yapılandırma (python-dotenv) |
| [Python_09](Python_09) | Veri doğrulama | Pydantic modelleri, `Enum`, `datetime`, alan doğrulamaları |
| [Python_10](Python_10) | Fonksiyonel programlama | Lambda, higher-order fonksiyonlar, scope ve closure, `functools`, decorator'lar |

## Çalıştırma

Egzersizlerin çoğu tek dosyalık script'lerdir:

```bash
python3 Python_00/ex0/ft_hello_garden.py
```

Harici paket kullanan modüller (`Python_08`, `Python_09`) için önce sanal ortam kur:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r Python_08/ex1/requirements.txt   # Python_08
pip install pydantic                            # Python_09
```

## Yapı

```
.
├── Python_00/
│   ├── ex0/
│   ├── ex1/
│   └── ...
├── Python_01/
├── ...
└── Python_10/
```
