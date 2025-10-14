# 🎵 YouTube Audio Telegram Bot

Этот бот загружает **только аудио с YouTube** и отправляет его пользователю в **Telegram**.  
Код написан на **Python** с использованием библиотек `yt_dlp` и `python-telegram-bot`.

---

## 💻 Полный код бота

```python
import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔹 Токен бота, полученный от @BotFather
BOT_TOKEN = "ВАШ_ТОКЕН_БОТА"

# 🔹 Временная папка для хранения аудиофайлов
TEMP_FOLDER = "temp_audio"
os.makedirs(TEMP_FOLDER, exist_ok=True)

# 🔹 Функция обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Привет! Отправь ссылку на видео с YouTube, и я отправлю тебе аудио напрямую."
    )

# 🔹 Основная функция обработки сообщений с ссылками
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    msg = await update.message.reply_text("⏳ Загрузка аудио...")

    # Настройки загрузки yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Выбор лучшего качества аудио
        'outtmpl': os.path.join(TEMP_FOLDER, '%(title)s.%(ext)s'),  # Путь для сохранения
        'retries': 10,  # Количество попыток при ошибках
        'continuedl': True,  # Продолжить загрузку при обрыве
        'concurrent_fragment_downloads': 4,  # Загрузка нескольких частей одновременно
        'fragment_retries': 5  # Повтор загрузки отдельных частей при ошибке
    }

    try:
        # Загрузка аудио
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            audio_file = ydl.prepare_filename(info)
            title = info.get("title", "Аудиофайл")

        # Отправка файла пользователю
        await msg.edit_text("✅ Отправка аудиофайла...")
        with open(audio_file, 'rb') as f:
            await update.message.reply_document(document=f, caption=title)

        # Удаление временного файла после отправки
        os.remove(audio_file)
        await msg.edit_text("✅ Аудио отправлено и временный файл удалён.")
    except Exception as e:
        await msg.edit_text(f"❌ Ошибка при загрузке: {e}")

# 🔹 Настройка и запуск бота
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🚀 Бот запущен...")
app.run_polling()


```
# Объяснения
## 1.Импорт библиотек
```python
 import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
```

- `os` — работа с файлами и папками на компьютере.  
- `yt_dlp` — скачивает аудио и видео с YouTube.  
- `telegram` и `telegram.ext` — создают и управляют Telegram-ботом.  
- `Update` — объект, содержащий данные о полученном сообщении.  
- `ApplicationBuilder`, `CommandHandler`, `MessageHandler`, `ContextTypes`, `filters` — инструменты для настройки логики бота: обработка команд и сообщений, фильтры.
---
## 2. Токен бота
```python
BOT_TOKEN = "ВАШ_ТОКЕН_БОТА"
```
- `BOT_TOKEN` —  сюда вляется токен, полученный от BotFather
---
## 3. Временная папка
```python
TEMP_FOLDER = "temp_audio"
os.makedirs(TEMP_FOLDER, exist_ok=True)

```
- `TEMP_FOLDER` — папка для временного хранения аудиофайлов перед отправкой пользователю.
- os.makedirs(..., exist_ok=True) создаёт папку, если её ещё нет, чтобы избежать ошибок.
---
## 4. Функция /start

```python
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Привет! Отправь ссылку на видео с YouTube, и я отправлю тебе аудио напрямую."
    )


```
-  Эта функция обрабатывает команду /start...Когда пользователь отправляет /start, бот приветствует его
- Используется await, так как функция асинхронная
    )
---
## 5. Функция обработки сообщений
```python
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    msg = await update.message.reply_text("⏳ Загрузка аудио...")

```
- Получает ссылку на YouTube из текста сообщения.
- Отправляет пользователю сообщение о начале загрузки аудио.


---
## 6. Настройки загрузки
```python
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(TEMP_FOLDER, '%(title)s.%(ext)s'),
    'retries': 10,
    'continuedl': True,
    'concurrent_fragment_downloads': 4,
    'fragment_retries': 5
}

```
- Настройки yt_dlp: качество аудио, путь сохранения, количество попыток при ошибках и загрузка фрагментами.
---
## 7. Загрузка аудио
```python
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=True)
    audio_file = ydl.prepare_filename(info)
    title = info.get("title", "Аудиофайл")


```
-  Используется yt_dlp для скачивания информации и аудио
- prepare_filename создаёт путь к файлу.
- title —..заголовок видео, который будет отображаться в подписи к файлу..
---
## 8. Отправка пользователю
```python
await msg.edit_text("✅ Отправка аудиофайла...")
with open(audio_file, 'rb') as f:
    await update.message.reply_document(document=f, caption=title)

```
- Обновляет сообщение о начале отправки.
- Отправляет файл пользователю как документ с подписью.
---
## 9. Удаление временного файла
```python
os.remove(audio_file)
await msg.edit_text("✅ Аудио отправлено и временный файл удалён.")
```
- Удаляет файл после отправки, чтобы не занимал место.
- Сообщает пользователю о завершении.
---
## 10. Обработка ошибок
```python
except Exception as e:
    await msg.edit_text(f"❌ Ошибка при загрузке: {e}")

```
- Сообщает пользователю о любой ошибке во время загрузки или отправки.
---
## 11. Настройка и запуск бота
```python
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print("🚀 Бот запущен...")
app.run_polling()
```
- Создаёт объект бота и добавляет обработчики команд и сообщений.
- Запускает бота в режиме постоянного ожидания сообщений (polling).
- Выводит сообщение в консоль о запуске бота.
