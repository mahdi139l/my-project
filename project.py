# # #sms bomber

# # # import time
# # # from collections import defaultdict
# # # from twilio.rest import Client


# # # account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# # # auth_token = "your_auth_token"
# # # sender = input("enter your number?")
# # # client = Client(account_sid, auth_token)
# # # last_sent_at = defaultdict(lambda: 0)
# # # WINDOW_SECONDS = 60

# # # def send_sms_safe(to_number: str, body: str):
# # #     now = time.time()
# # #     if now - last_sent_at[to_number] < WINDOW_SECONDS:
# # #         raise RuntimeError("درخواست زیاد: لطفاً بعداً تلاش کنید.")
# # #     msg = client.messages.create(to=to_number, from_=sender, body=body)
# # #     last_sent_at[to_number] = now
# # #     return msg.sid

 



# # # این فقط یک مثال از چیزی‌ست که نباید نوشته یا اجرا بشه!
# # # while True:
# # #     client.messages.create(
# # #         to="+989044105128",
# # #         from_="+989938929001",
# # #         body="سلام :)"
# # #     )














# # #snake and ladders 
# # #مار و پله 
# # # بارگیری کتابخانه Pygame
# # import pygame 
# # import random

# # # تعریف رنگ‌ها
# # BLACK = (0, 0, 0)
# # WHITE = (255, 255, 255)
# # GREEN = (0, 255, 0)
# # RED = (255, 0, 0)

# # # اندازه صفحه نمایش را تعیین می‌کنیم
# # SCREEN_WIDTH = 640
# # SCREEN_HEIGHT = 480

# # # اندازه شبکه بازی
# # GRID_SIZE = 10

# # # سرعت حرکت مار
# # SNAKE_SPEED = 1

# # # اندازه مار
# # SNAKE_SIZE = GRID_SIZE

# # # اندازه پله
# # LADDER_SIZE = GRID_SIZE

# # # تعداد پله‌ها
# # NUM_LADDERS = 6

# # # موقعیت اولیه مار
# # snake_position = [0, 0]

# # # موقعیت پله‌ها
# # ladder_positions = []
# # for i in range(NUM_LADDERS):
# #     ladder_positions.append([random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1) * GRID_SIZE,
# #                              random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 2) * GRID_SIZE])

# # # شروع Pygame
# # pygame.init()

# # # تعیین اندازه صفحه نمایش
# # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # # تعیین عنوان پنجره بازی
# # pygame.display.set_caption("بازی مارپله")

# # # تعیین ساعت بازی
# # clock = pygame.time.Clock()

# # # ساخت فونت
# # font = pygame.font.SysFont('Arial', 16)

# # # امتیاز اولیه
# # score = 0

# # # ساخت مار
# # snake = pygame.Surface((SNAKE_SIZE, SNAKE_SIZE))
# # snake.fill(GREEN)

# # # ساخت پله‌ها
# # ladders = []
# # for i in range(NUM_LADDERS):
# #     ladder = pygame.Surface((LADDER_SIZE, LADDER_SIZE))
# #     ladder.fill(RED)
# #     ladders.append(ladder)

# # # جهت اولیه حرکت مار
# # direction = [1, 0]

# # # حلقه بازی
# # while True:
# #     # پردازش رویدادها
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #             quit()

# #     # حرکت مار
# #     snake_position[0] += direction[0] * SNAKE_SPEED * GRID_SIZE
# #     snake_position[1] += direction[1] * SNAKE_SPEED * GRID_SIZE

# #     # چک کردن برای برخورد مار با پله
# #     for i in range(NUM_LADDERS):
# #         if (snake_position[0], snake_position[1]) == tuple(ladder_positions[i]):
# #             snake_position[1] -= GRID_SIZE
# #             score += 10



# #     # رسم مار و پله‌ها
# #     screen.fill(WHITE)
# #     screen.blit(snake, snake_position)
# #     for i in range(NUM_LADDERS):
# #         screen.blit(ladders[i], ladder_positions[i])

# #     # نمایش امتیاز
# #     text = font.render("امتیاز: {}".format(score), True, BLACK)
# #     screen.blit(text, [10, 10])

# #     # نمایش صفحه بازی
# #     pygame.display.flip()

# #     # محدود کردن مار در محدوده صفحه بازی
# #     if snake_position[0] < 0:
# #         snake_position[0] = 0
# #     elif snake_position[0] >= SCREEN_WIDTH:
# #         snake_position[0] = SCREEN_WIDTH - SNAKE_SIZE
# #     if snake_position[1] < 0:
# #         snake_position[1] = 0
# #     elif snake_position[1] >= SCREEN_HEIGHT:
# #         snake_position[1] = SCREEN_HEIGHT - SNAKE_SIZE

# #     # انتخاب جهت جدید برای مار به صورت تصادفی
# #     direction = random.choice([[1, 0], [-1, 0], [0, 1], [0, -1]])

# #     # محاسبه موقعیت جدید پله‌ها به صورت تصادفی
# #     for i in range(NUM_LADDERS):
# #         ladder_positions[i][0] += random.choice([-1, 1]) * GRID_SIZE
# #         ladder_positions[i][1] += GRID_SIZE

# #     # تنظیم سرعت بازی
# #     # clock.tick(10






# # import tkinter as tk
# # import time

# # def update_time():
# #     current_time = time.strftime("%H:%M:%S")
# #     clock_label.config(text=current_time)
# #     clock_label.after(1000, update_time)

# # # ساخت پنجره
# # window = tk.Tk()
# # window.title("ساعت")

# # # ساخت برچسب
# # clock_label = tk.Label(window, font=("Helvetica", 48))
# # clock_label.pack(padx=20, pady=20)

# # # شروع به‌روزرسانی ساعت
# # update_time()

# # # نمایش پنجره
# # window.mainloop()





# import requests
# import time

# number =+989938929001
# message="salam"

# for _ in range(100):  # ارسال 100 پیام
#     requests.post("آدرس_API_پیامکی", data={"to": number, "text": message})
#     time.sleep(1)  # تاخیر برای دور زدن محدودیت





import requests
import time

# شماره گیرنده
number = "+989938929001"

# متن پیام
message = "salam"

# آدرس API (اینجا باید آدرس درست API سرویس پیام‌رسان خودت رو وارد کنی)
api_url = "https://example.com/send"  

# ارسال 100 پیام
for _ in range(100):
    response = requests.post(api_url, data={"to": number, "text": message})
    print(response.status_code, response.text)  # نمایش نتیجه درخواست
    time.sleep(1)  # یک ثانیه مکث بین هر پیام