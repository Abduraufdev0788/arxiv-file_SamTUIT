<div align="center">

<img src="https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
<img src="https://img.shields.io/badge/DRF-3.16-red?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" />

# 📚 SamTUIT — Raqamli Axborot Portali

**Muhammad al-Xorazmiy nomidagi Toshkent Axborot Texnologiyalari Universiteti**  
**Samarqand filiali — Elektron Arxiv va Ma'lumot Boshqaruv Tizimi**

> Talabalar, o'qituvchilar, professorlar va rasmiy qarorlarni boshqarish uchun markazlashgan Django web-platformasi.

</div>

---

## 📋 Mundarija

- [Loyiha haqida](#-loyiha-haqida)
- [Texnologiyalar](#-texnologiyalar)
- [Loyiha arxitekturasi](#-loyiha-arxitekturasi)
- [Django ilovalari](#-django-ilovalari)
- [Ma'lumotlar bazasi modellari](#-malumotlar-bazasi-modellari)
- [Autentifikatsiya tizimi](#-autentifikatsiya-tizimi)
- [URL marshrutlari](#-url-marshrutlari)
- [O'rnatish va ishga tushirish](#-ornatish-va-ishga-tushirish)
- [Muhit o'zgaruvchilari](#-muhit-ozgaruvchilari)
- [REST API](#-rest-api)
- [Loyiha tuzilmasi](#-loyiha-tuzilmasi)
- [Hissa qo'shish](#-hissa-qoshish)

---

## 🎯 Loyiha haqida

**SamTUIT Elektron Arxivi** — bu TATU Samarqand filialining barcha akademik va ma'muriy ma'lumotlarini raqamlashtirish va markazlashtirish maqsadida yaratilgan zamonaviy web-tizim.

### ✨ Asosiy imkoniyatlar

| Xususiyat | Tavsif |
|-----------|--------|
| 🎓 **Talabalar bazasi** | Filialda ta'lim olayotgan va bitirgan barcha talabalar ma'lumotlari |
| 📖 **Bitiruv malakaviy ishlar** | BMI mavzulari, rahbarlar va baholash natijalari |
| 👨‍🏫 **Xodimlar boshqaruvi** | O'qituvchilar va professorlar, ularning shartnoma ma'lumotlari |
| 📜 **Qarorlar arxivi** | Prezident va universitet qarorlari, buyruqlar fayl bilan |
| 🔐 **JWT autentifikatsiya** | Cookie asosidagi xavfsiz kirish tizimi |
| 📄 **Hisobot generatsiyasi** | `.docx` formatida avtomatik arxitektura hisoboti |
| 📱 **Responsive dizayn** | Tailwind CSS yordamida barcha qurilmalar uchun moslashgan interfeys |

---

## 🛠 Texnologiyalar

### Backend
| Texnologiya | Versiya | Maqsad |
|------------|---------|--------|
| **Django** | 5.2 | Asosiy web freymvork |
| **Django REST Framework** | 3.16.1 | REST API yaratish |
| **djangorestframework-simplejwt** | 5.5.1 | JWT token autentifikatsiyasi |
| **psycopg2-binary** | 2.9.11 | PostgreSQL adapter |
| **python-decouple** | 3.8 | Konfiguratsiya boshqaruvi |
| **python-dotenv** | 1.2.1 | `.env` fayllari yuklash |

### Ma'lumotlar bazasi
| Texnologiya | Versiya | Maqsad |
|------------|---------|--------|
| **PostgreSQL** | 16+ | Asosiy relatsion ma'lumotlar bazasi |
| **SQLAlchemy** | 2.0.45 | ORM qo'shimcha vosita |

### Frontend
| Texnologiya | Maqsad |
|------------|--------|
| **Tailwind CSS** (CDN) | Zamonaviy UI uslublash |
| **Django Templates** | Server-side render |
| **Google Fonts (Inter)** | Professional tipografiya |
| **Vanilla JavaScript** | Dinamik interfeys elementlari |

---

## 🏗 Loyiha arxitekturasi

```
arxiv-file_SamTUIT/
│
├── 📁 core/                    # Django asosiy konfiguratsiyasi
│   ├── settings.py             # Loyiha sozlamalari
│   ├── urls.py                 # Asosiy URL yo'naltiruvchi
│   ├── wsgi.py                 # WSGI server interfeysi
│   └── asgi.py                 # ASGI server interfeysi
│
├── 📁 apps/                    # Django ilovalar to'plami
│   ├── login/                  # Autentifikatsiya va sessiya
│   ├── bmi/                    # Bitiruv malakaviy ishlar
│   ├── talabalar/              # Talabalar boshqaruvi
│   ├── oqituvchilar/           # O'qituvchilar boshqaruvi
│   ├── professorlar/           # Professorlar boshqaruvi
│   ├── qarorlar/               # Qarorlar arxivi
│   ├── Customuser/             # Foydalanuvchi profili
│   └── utils/                  # Yordamchi funksiyalar
│
├── 📁 templates/               # HTML shablonlar
│   ├── Customs/                # Umumiy shablonlar (asosiy sahifa)
│   ├── bmi/                    # BMI sahifalari
│   ├── ftot/                   # Talabalar sahifalari
│   ├── oqituvchilar/           # O'qituvchilar sahifalari
│   ├── professors/             # Professorlar sahifalari
│   ├── qarorlar/               # Qarorlar sahifalari
│   ├── home/                   # Bosh sahifa
│   └── login/                  # Kirish/Ro'yxatdan o'tish sahifalari
│
├── 📁 media/                   # Yuklangan fayllar saqlash joyi
│   ├── student_files/          # Talabalar fayllari
│   ├── buyruqlar/              # O'qituvchi buyruqlari
│   └── professor_buyruqlari/   # Professor buyruqlari
│
├── 📁 frontend/                # Frontend resurslar
├── 📄 manage.py                # Django boshqaruv komandasi
├── 📄 requirements.txt         # Python kutubxonalar ro'yxati
├── 📄 generate_docx.py         # Hisobot generatsiya skripti
├── 📄 .env                     # Muhit o'zgaruvchilari (maxfiy)
└── 📄 .env.sample              # Muhit namunasi
```

---

## 📦 Django ilovalari

Loyiha **8 ta mustaqil Django ilovasi**dan tashkil topgan, har biri o'z soha mantig'iga mas'ul:

### 1. 🔐 `apps.login` — Autentifikatsiya
- Foydalanuvchi ro'yxatdan o'tishi va kirishi
- JWT tokenlarini yaratish va tekshirish
- `JWTAuthMiddleware` — cookie orqali tokenlarni avtomatik aniqlash
- `JWTLoginRequiredMixin` va `AdminOnlyMixin` — ruxsat nazorati

### 2. 🎓 `apps.bmi` — Bitiruv Malakaviy Ishlar
- Bitiruv malakaviy ishlarini ro'yxatga olish
- Talaba ma'lumotlari: ismi, fakulteti, guruhi, mavzu nomi
- Umumiy ball va fayl biriktirish imkoniyati
- Qidirish (ism, guruh, mavzu, yil bo'yicha) va sahifalash

### 3. 🧑‍🎓 `apps.talabalar` — Talabalar Ma'lumotlari
- Barcha talabalar bazasini boshqarish (CRUD)
- To'liq ism, pasport, qabul yili, fakultet, guruh, status
- Holat: O'qimoqda / Bitirgan / To'xtatgan
- Kengaytirilgan filtr: ism, fakultet, qabul yili, guruh
- Sahifalash (100 ta yozuv/sahifa)

### 4. 👨‍🏫 `apps.oqituvchilar` — O'qituvchilar
- O'qituvchilar profili va shartnoma ma'lumotlari
- Kafedra: Axborot xavfsizligi, AT, Raqamli ta'lim, Dasturiy injiniring va boshqalar
- Lavozim: Assistent, Katta o'qituvchi, Dotsent, Professor
- Shartnoma raqami, boshlanish/tugash sanasi
- Buyruq fayli biriktirish

### 5. 🎓 `apps.professorlar` — Professorlar
- Professorlar profili boshqaruvi
- Fakultet va kafedra bog'liqligi
- Shartnoma va buyruq fayllari
- Faollik holati (is_active)

### 6. 📜 `apps.qarorlar` — Rasmiy Qarorlar Arxivi
- Prezident va universitet qarorlarini arxivlash
- Qaror raqami, sarlavhasi, sanasi va tavsifi
- PDF yoki boshqa format fayllar biriktirish

### 7. 👤 `apps.Customuser` — Foydalanuvchi Profili
- Foydalanuvchi sozlamalari va profil sahifasi
- Rol asosida ko'rinish boshqaruvi

### 8. 🛠 `apps.utils` — Yordamchi Modul
- Umumiy yordamchi funksiyalar
- Asosiy (bosh) sahifa yo'naltiruvchisi

---

## 🗄 Ma'lumotlar bazasi modellari

### `Registration` (login ilovasi)
```python
class Registration(models.Model):
    name     = CharField(max_length=200)
    surname  = CharField(max_length=200)
    email    = EmailField()
    password = CharField(max_length=256)   # Xeshlangan
    role     = CharField(choices=[("Admin", "Admin"), ("Custom", "Custom")])
```

### `Talabalar` (talabalar ilovasi)
```python
class Talabalar(models.Model):
    full_name   = CharField(max_length=300)
    pasport     = CharField(max_length=9)    # Unikal
    qabul_yili  = IntegerField()
    faculty     = CharField(choices=CHOISE_FACULTY)
    group       = CharField(max_length=128)
    status      = CharField(choices=CHOISE_STATUS)
    # Holat: O'qimoqda | Bitirgan | To'xtatgan
```

### `BmiTalaba` (bmi ilovasi)
```python
class BmiTalaba(models.Model):
    first_name  = CharField(max_length=128)
    last_name   = CharField(max_length=128)
    faculty     = CharField(choices=[KI, AT])
    group_name  = CharField(max_length=64)
    theme_name  = TextField()
    years       = CharField(max_length=32)
    total_ball  = FloatField()
    files       = FileField(upload_to='student_files/')
```

### `Teacher` (oqituvchilar ilovasi)
```python
class Teacher(models.Model):
    first_name          = CharField(max_length=128)
    last_name           = CharField(max_length=128)
    qabul_sana          = DateField()
    chiqish_sana        = DateField(null=True)
    shartnoma_raqami    = IntegerField(unique=True)
    shartnoma_bekor_sana = DateField(null=True)
    ishlagan_bolimi     = CharField(choices=KAFEDRA)
    ishlagan_lavozimi   = CharField(choices=LAVOZIM)
    pasport             = CharField(max_length=20, unique=True)
    buyruq              = FileField(upload_to='buyruqlar/')
    is_active           = BooleanField(default=True)
```

### `Professor` (professorlar ilovasi)
```python
class Professor(models.Model):
    first_name        = CharField(max_length=128)
    last_name         = CharField(max_length=128)
    qabul_sana        = DateField()
    ishlagan_fakultet = CharField(choices=FAKULTET)
    ishlagan_bolimi   = CharField(choices=KAFEDRA)
    shartnoma_raqami  = IntegerField(unique=True)
    pasport           = CharField(max_length=20, unique=True)
    buyruq            = FileField(upload_to='professor_buyruqlari/')
    is_active         = BooleanField(default=True)
```

### `PQaror` (qarorlar ilovasi)
```python
class PQaror(models.Model):
    qaror_num   = CharField(unique=True)
    title       = CharField()
    created_at  = DateTimeField()
    description = CharField()
    file        = FileField(upload_to='PQarorlar/')
```

---

## 🔐 Autentifikatsiya tizimi

Loyiha **ikki qatlamli** JWT autentifikatsiya tizimini qo'llaydi:

```
Foydalanuvchi kirishi
        │
        ▼
  [Login View] ──► JWT token yaratiladi
        │
        ▼
  Token Cookie'ga saqlanadi ("access_token")
        │
        ▼
  [JWTAuthMiddleware] ──► Har bir so'rovda cookie o'qiladi
        │
        ▼
  Token dekodlanadi ──► request.user_jwt o'rnatiladi
        │
        ▼
  [JWTLoginRequiredMixin] ──► Kirishni tekshiradi
  [AdminOnlyMixin]         ──► Admin ruxsatini tekshiradi
```

**JWT sozlamalari:**
```python
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME':  timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES':      ('Bearer',),
}
```

**Foydalanuvchi rollari:**

| Rol | Imkoniyatlar |
|-----|-------------|
| `Admin` | Barcha CRUD operatsiyalari, panel boshqaruvi |
| `Custom` | Faqat o'qish, shaxsiy sahifa |

---

## 🌐 URL marshrutlari

| URL pattern | Ilova | Tavsif |
|------------|-------|--------|
| `/` | `utils` | Bosh sahifa |
| `/royxatdan_otish/` | `login` | Kirish / Ro'yxatdan o'tish |
| `/qarorlar/` | `qarorlar` | Qarorlar ro'yxati va boshqaruvi |
| `/talabalar/` | `talabalar` | Talabalar ma'lumotlari |
| `/bmi/` | `bmi` | Bitiruv malakaviy ishlar |
| `/xodimlar/` | `oqituvchilar` | O'qituvchilar boshqaruvi |
| `/professorlar/` | `professorlar` | Professorlar boshqaruvi |
| `/users/` | `Customuser` | Foydalanuvchi profili |
| `/admin/` | Django Admin | Tizim administratori paneli |

---

## 🚀 O'rnatish va ishga tushirish

### Talablar
- Python 3.11 yoki undan yuqori
- PostgreSQL 14 yoki undan yuqori
- pip (Python paket boshqaruvchisi)

### 1-qadam: Repozitoriyani klonlash
```bash
git clone https://github.com/Abduraufdev0788/arxiv-file_SamTUIT.git
cd arxiv-file_SamTUIT
```

### 2-qadam: Virtual muhit yaratish
```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3-qadam: Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4-qadam: Muhit o'zgaruvchilarini sozlash
```bash
cp .env.sample .env
```
`.env` faylini oching va quyidagi qiymatllarni to'ldiring (pastdagi bo'limga qarang).

### 5-qadam: Ma'lumotlar bazasini yaratish
```bash
# PostgreSQL'da ma'lumotlar bazasini yarating:
createdb samtuit_db

# Migratsiyalarni qo'llash:
python manage.py makemigrations
python manage.py migrate
```

### 6-qadam: Superuser yaratish
```bash
python manage.py createsuperuser
```

### 7-qadam: Statik fayllarni yig'ish
```bash
python manage.py collectstatic
```

### 8-qadam: Serverni ishga tushirish
```bash
python manage.py runserver
```

🌐 Brauzerda oching: **http://127.0.0.1:8000**

---

## ⚙️ Muhit o'zgaruvchilari

`.env` faylini yaratib, quyidagi qiymatlarni to'ldiring:

```env
# Django xavfsizlik kaliti (majburiy)
SECRET_KEY=your-very-secret-key-here

# Debug rejimi (ishlab chiqishda True, produksiyada False)
DEBUG=True

# Ruxsat etilgan hostlar
ALLOWED_HOSTS=127.0.0.1,localhost

# ──── Ma'lumotlar bazasi ────
DB_HOST=localhost
DB_PORT=5432
DB_NAME=samtuit_db
DB_USER=postgres
DB_PASSWORD=your_password

# ──── Email xizmati ────
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# ──── Telegram bot (ixtiyoriy) ────
TELEGRAM_BOT_TOKEN=your-bot-token
TELEGRAM_CHAT_ID=your-chat-id
```

> ⚠️ **Muhim:** `.env` fayli hech qachon Git'ga qo'shilmasligi kerak. `.gitignore` da allaqachon qo'shilgan.

---

## 🔌 REST API

Loyiha **Django REST Framework** bilan qurilgan va JWT autentifikatsiyasini qo'llaydi.

### Autentifikatsiya header'i
```http
Authorization: Bearer <your_access_token>
```

### Asosiy endpointlar

| Method | Endpoint | Tavsif | Ruxsat |
|--------|----------|--------|--------|
| `POST` | `/royxatdan_otish/login/` | Kirish, token olish | Hammaga |
| `POST` | `/royxatdan_otish/register/` | Ro'yxatdan o'tish | Hammaga |
| `GET` | `/talabalar/` | Talabalar ro'yxati | Admin |
| `POST` | `/talabalar/add/` | Yangi talaba qo'shish | Admin |
| `POST` | `/talabalar/<id>/delete/` | Talabani o'chirish | Admin |
| `GET/POST` | `/bmi/` | BMI ro'yxati | Admin |
| `GET` | `/qarorlar/` | Qarorlar ro'yxati | Hammaga |
| `GET` | `/xodimlar/` | O'qituvchilar ro'yxati | Admin |
| `GET` | `/professorlar/` | Professorlar ro'yxati | Admin |

---

## 📄 Hisobot generatsiyasi

Loyiha avtomatik `.docx` formatida backend arxitektura hisobotini yaratish imkonini beradi:

```bash
python generate_docx.py
```

Bu buyruq `Backend_Architecture_Report.docx` faylini yaratadi, unda quyidagilar bo'ladi:
- Loyiha kirish qismi va tavsif
- Barcha Django ilovalariga umumiy ko'rinish
- Modellar jadvali (ilovalar va ularning maqsadi)
- Amalga oshirish holati jadvali

---

## 📊 Loyiha holati

| Modul | Holat | Izoh |
|-------|-------|------|
| Ma'lumotlar bazasi sxemasi | ✅ Tayyor | Barcha modellar yaratilgan |
| JWT autentifikatsiyasi | ✅ Tayyor | Cookie-based middleware |
| Talabalar moduli | ✅ Tayyor | To'liq CRUD + filtr |
| BMI moduli | ✅ Tayyor | Yaratish, o'zgartirish, o'chirish |
| O'qituvchilar moduli | ✅ Tayyor | Shartnoma va buyruq bilan |
| Professorlar moduli | ✅ Tayyor | Fakultet va kafedra bilan |
| Qarorlar arxivi | ✅ Tayyor | Fayl biriktirish bilan |
| REST API endpointlari | 🔄 Jarayonda | DRF bilan kengaytirilmoqda |
| Telegram bildirishnoma | 🔄 Jarayonda | Bot integratsiyasi |
| Frontend dizayn | ✅ Tayyor | Tailwind CSS, responsive |

---

## 🧰 Loyiha tuzilmasi (to'liq)

```
arxiv-file_SamTUIT/
├── apps/
│   ├── Customuser/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── bmi/
│   │   ├── models.py       # BmiTalaba modeli
│   │   ├── views.py        # CRUD + qidirish
│   │   ├── forms.py        # BmiTalabaForm
│   │   └── urls.py
│   ├── login/
│   │   ├── models.py       # Registration modeli
│   │   ├── middleware.py   # JWTAuthMiddleware
│   │   ├── mixins.py       # LoginRequired, AdminOnly
│   │   ├── jwt_utils.py    # Token encode/decode
│   │   └── urls.py
│   ├── oqituvchilar/
│   │   ├── models.py       # Teacher modeli
│   │   ├── views.py
│   │   └── urls.py
│   ├── professorlar/
│   │   ├── models.py       # Professor modeli
│   │   ├── views.py
│   │   └── urls.py
│   ├── qarorlar/
│   │   ├── models.py       # PQaror modeli
│   │   ├── views.py
│   │   └── urls.py
│   ├── talabalar/
│   │   ├── models.py       # Talabalar modeli
│   │   ├── views.py        # To'liq CRUD + filtr
│   │   └── urls.py
│   └── utils/
│       └── urls.py
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── templates/
│   ├── Customs/home/home.html   # Asosiy sahifa
│   ├── bmi/
│   ├── ftot/                    # Talabalar shablonlari
│   ├── oqituvchilar/
│   ├── professors/
│   ├── qarorlar/
│   └── login/
├── media/                       # Yuklangan fayllar
├── generate_docx.py             # Hisobot generatori
├── manage.py
├── requirements.txt
├── .env                         # Maxfiy konfiguratsiya
└── .env.sample                  # Konfiguratsiya namunasi
```

---

## 🤝 Hissa qo'shish

Loyihaga hissa qo'shmoqchi bo'lsangiz:

1. Repozitoriyani **fork** qiling
2. Yangi branch oching: `git checkout -b feature/yangi-funksiya`
3. O'zgartirishlar kiriting va commit qiling: `git commit -m "feat: yangi funksiya qo'shildi"`
4. Branch'ni push qiling: `git push origin feature/yangi-funksiya`
5. **Pull Request** oching

### Commit uslubi

```
feat: yangi funksiya qo'shildi
fix: xato tuzatildi
docs: hujjat yangilandi
style: format o'zgartirildi
refactor: kod qayta yozildi
test: test qo'shildi
```

---

## 📞 Aloqa

**SamTUIT — Muhammad al-Xorazmiy nomidagi TATU Samarqand filiali**

- 📍 Manzil: Samarqand shahri, Shoxrux ko'chasi, 37-uy
- 📞 Telefon: +998 (66) 232-29-29
- 📧 Email: info@samtuit.uz

---

<div align="center">

**© 2025 SamTUIT | Barcha huquqlar himoyalangan**

*Django 5.2 · PostgreSQL · JWT Auth · DRF · Tailwind CSS*

</div>