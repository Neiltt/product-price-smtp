import smtplib, ssl

def send_mail(name, price):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "49@gmail.com"
    receiver_email = "491.on@gmail.com"
    password = "eyyy sxxx gzzz rfff"
    message = f"""\
Subject: {name} 降價囉!

{name} 降價至 {price}""".encode('utf-8')

    # with 語句會在語句結束時自動關閉資源(SMTP 連線)。
    # EHLO 命令是用於向 SMTP 伺服器進行初始化和自我介紹的命令。STARTTLS 命令啟動加密連線
    # STARTTLS 命令是用於啟動加密連線的命令。
    # 在啟動加密連線後，需要再次向 SMTP 伺服器發送 EHLO 命令以確認連線已加密。
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

print("mail寄送囉!")
# 測試
# send_mail("PS5", 19000)
