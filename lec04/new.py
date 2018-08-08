from gmail import GMail, Message
from random import choice
import datetime
now = datetime.datetime.now()

gmail= GMail("bachsxi@gmail.com", "B@chs2609")
check_time = True

while check_time:
    if 9>= now.hour >= 7:
        html_content= """
            <p style="text-align: center;"><strong>CỘNG H&Ograve;A X&Atilde; HỘI CHỦ NGHĨA VIỆT NAM</strong></p>
        <p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
        <p style="text-align: center;">-------***-------</p>
        <p>&nbsp;</p>
        <p style="text-align: center;"><strong>Đơn xin nghỉ ph&eacute;p</strong></p>
        <p>K&iacute;nh gửi: gi&aacute;o vi&ecirc;n chủ nhiệm</p>
        <p style="padding-left: 30px;">Em t&ecirc;n l&agrave; Ho&agrave;ng Duy B&aacute;ch, em xin được nghỉ ph&eacute;p v&igrave; l&iacute; do {{excuse}}. Em xin cảm ơn.</p>
        <p>&nbsp;</p>
        """
        excuses=["đau bụng","gãy chân", "tai nạn xe"]
        rand_excuse = choice(excuses)
        html_send= html_content.replace("{{excuse}}",rand_excuse)
        msg= Message(
            "Đơn xin nghỉ phép",
            to="bachs2803@gmail.com",
            html=html_send
        )
        gmail.send(msg)
        break
    else:
        check_time= False    
    