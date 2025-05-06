from matplotlib.artist import setp
import requests
import json
import os.path
import smtplib
from getpass import getpass
from email.message import EmailMessage
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
if __name__ == '__main__':

    EMAIL_ADDRESS=""
    EMAIL_PASSWORD=""
    
    #洋
    heads = {
        'User-Agent': '',
        'Cookie':'ttwid=1%7CEXB34thGmagumqg7Z1ZoveFWGfOm0OlVZm9YSsgzUUk%7C1711525881%7C757f828df61595c276a484428b5db43aaf6fc5104792ac14a5052a22286934d5; passport_csrf_token=2ec83255d6e4357b5f3778e83b58e365; passport_csrf_token_default=2ec83255d6e4357b5f3778e83b58e365; bd_ticket_guard_client_web_domain=2; SEARCH_RESULT_LIST_TYPE=%22single%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.7%7D; __ac_nonce=0662600b600309a7a7c5b; __ac_signature=_02B4Z6wo00f01SaY35gAAIDB0PHWvuUeScUmuNsAAC-Dd3; dy_swidth=1707; dy_sheight=960; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; csrf_session_id=fcfe4da3ee0db87e1ea48c4257274419; strategyABtestKey=%221713766584.145%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; passport_assist_user=CkELADOjGPfwTtsiGwBCjANpyNMct3ai2x2szHCJjNkSPKusT6k3RtYYJQZhcAOzOIqRKYKZASXHEdijx_3h_ZoL-hpKCjxRQnMiiTbkVis9ZQFl-nT-h3dsoS4wna29aE7O6mRtkOObF3nobqwmUAXNJjWXo-SUYYBQwEHmmyHhSE8QuKnPDRiJr9ZUIAEiAQMoex_0; n_mh=hkKrzhBFAOy5qfLAkpFugtuITxsK27XqocRPBCcFy3A; sso_uid_tt=8be2fedf4f08dc1b1916b4e4dcdf5973; sso_uid_tt_ss=8be2fedf4f08dc1b1916b4e4dcdf5973; toutiao_sso_user=5f4dd1ff61d3004d5e98e6a219389734; toutiao_sso_user_ss=5f4dd1ff61d3004d5e98e6a219389734; sid_ucp_sso_v1=1.0.0-KDE5MzYwM2U3NTg0ZDMzMmY4OWM0ZGNmMTE2ZTQzOTZlMDhjYmY4ODYKHwj3pOCE442_BRCVg5ixBhjvMSAMMKyUjJ8GOAZA9AcaAmxxIiA1ZjRkZDFmZjYxZDMwMDRkNWU5OGU2YTIxOTM4OTczNA; ssid_ucp_sso_v1=1.0.0-KDE5MzYwM2U3NTg0ZDMzMmY4OWM0ZGNmMTE2ZTQzOTZlMDhjYmY4ODYKHwj3pOCE442_BRCVg5ixBhjvMSAMMKyUjJ8GOAZA9AcaAmxxIiA1ZjRkZDFmZjYxZDMwMDRkNWU5OGU2YTIxOTM4OTczNA; passport_auth_status=1274478b0961655ea3c34f17b7a66cd1%2C; passport_auth_status_ss=1274478b0961655ea3c34f17b7a66cd1%2C; uid_tt=b5999278db59319450bfa2da0d3b08a5; uid_tt_ss=b5999278db59319450bfa2da0d3b08a5; sid_tt=46ab4c0eddfc6e2b05d9bab782106658; sessionid=46ab4c0eddfc6e2b05d9bab782106658; sessionid_ss=46ab4c0eddfc6e2b05d9bab782106658; publish_badge_show_info=%220%2C0%2C0%2C1713766808977%22; LOGIN_STATUS=1; store-region=cn-js; store-region-src=uid; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=00ddadd2fb8fa96a6ebcadc4ff984462; __security_server_data_status=1; sid_guard=46ab4c0eddfc6e2b05d9bab782106658%7C1713766810%7C5183998%7CFri%2C+21-Jun-2024+06%3A20%3A08+GMT; sid_ucp_v1=1.0.0-KGFkMmE3NmZmMDU0NWI2YTQwZmUyYzNkOGQ2ODRlNmIwMWM1ZTUxYWMKGwj3pOCE442_BRCag5ixBhjvMSAMOAZA9AdIBBoCbGYiIDQ2YWI0YzBlZGRmYzZlMmIwNWQ5YmFiNzgyMTA2NjU4; ssid_ucp_v1=1.0.0-KGFkMmE3NmZmMDU0NWI2YTQwZmUyYzNkOGQ2ODRlNmIwMWM1ZTUxYWMKGwj3pOCE442_BRCag5ixBhjvMSAMOAZA9AdIBBoCbGYiIDQ2YWI0YzBlZGRmYzZlMmIwNWQ5YmFiNzgyMTA2NjU4; download_guide=%223%2F20240422%2F0%22; my_rd=2; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSjloR24yeC9WNE5acml5eHI2T05UYmpNVHF0eTBDR3RkUkd0YkRaUHQ3cmRoU0ZCV1NrdytKTXdFc1FJRXV4cXpvZm1ZbEpjSHp0QlkxNVpQUUlORFk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; odin_tt=7cbc30e891d1c36f86b5f21044e1ba19e7ace990fa5c38b3c8f66c2e799e839a3ea60a1a7245052a6a90a6e86c85ce32; pwa2=%220%7C0%7C3%7C0%22; WallpaperGuide=%7B%22showTime%22%3A1713766689963%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A19%2C%22cursor2%22%3A0%7D; passport_fe_beating_status=false; msToken=9IkhDbvJSCnDPLdXiFv4V0JX_wdNBv3SrVXg60QCKlwE19zBHsZUihy8n_Jv6lhLNDtN4MmGCLnObjI3Nu05vca-UNDHtNVdxcuCX7eynKERgZ8bFWMvdw-7Ag==; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAr4tdtLnCN6YFIi1BLiVC-UsKVfy5XxLSrNGM1QEnQbow4LgvtDaaNqEirMPOwmvS%2F1713801600000%2F0%2F0%2F1713767609891%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAr4tdtLnCN6YFIi1BLiVC-UsKVfy5XxLSrNGM1QEnQbow4LgvtDaaNqEirMPOwmvS%2F1713801600000%2F0%2F1713767009891%2F0%22',
        'Referer':'https://www.douyin.com/user/MS4wLjABAAAAFwNcBWQlMQOjc6eoki0MruL4ZAPwYGg9An839CuoBg3TX8Z3ary1uc2sBtuUkbg5'
    }
    url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAFwNcBWQlMQOjc6eoki0MruL4ZAPwYGg9An839CuoBg3TX8Z3ary1uc2sBtuUkbg5&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1707&screen_height=960&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7350947635651593780&msToken=Z5MY2S2C8dwiQsGbToTYChoP3buuLxj_2DJxRQMzNN23EuRCNxG3M2Jx5zUKGZLhpDhy0JOh_KnSdPuWb6UcUhEkpunwIDfCzXARTOQeFtni6zYzbq1v8Lc8o1s%3D&a_bogus=D6mM%2F506didPfVWD5RdLfY3q6Ip3YkmQ0trEMD2fYdVVKg39HMO59exoLnsvWkYjLG%2FlIb6jy4heYNMMxQIbA3vIH8WKlICh-g00t-P2so0j5Z0rCDukrUmF-vwltBBp-JV3xcXmy7CGzuRplnAJ5k1cthMeaVR%3D'
    
    # heads = {
    # 'User-Agent': '',
    # 'Cookie':'ttwid=1%7CEXB34thGmagumqg7Z1ZoveFWGfOm0OlVZm9YSsgzUUk%7C1711525881%7C757f828df61595c276a484428b5db43aaf6fc5104792ac14a5052a22286934d5; passport_csrf_token=2ec83255d6e4357b5f3778e83b58e365; passport_csrf_token_default=2ec83255d6e4357b5f3778e83b58e365; bd_ticket_guard_client_web_domain=2; SEARCH_RESULT_LIST_TYPE=%22single%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.7%7D; __ac_nonce=0662600b600309a7a7c5b; __ac_signature=_02B4Z6wo00f01SaY35gAAIDB0PHWvuUeScUmuNsAAC-Dd3; dy_swidth=1707; dy_sheight=960; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; csrf_session_id=fcfe4da3ee0db87e1ea48c4257274419; strategyABtestKey=%221713766584.145%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; passport_assist_user=CkELADOjGPfwTtsiGwBCjANpyNMct3ai2x2szHCJjNkSPKusT6k3RtYYJQZhcAOzOIqRKYKZASXHEdijx_3h_ZoL-hpKCjxRQnMiiTbkVis9ZQFl-nT-h3dsoS4wna29aE7O6mRtkOObF3nobqwmUAXNJjWXo-SUYYBQwEHmmyHhSE8QuKnPDRiJr9ZUIAEiAQMoex_0; n_mh=hkKrzhBFAOy5qfLAkpFugtuITxsK27XqocRPBCcFy3A; sso_uid_tt=8be2fedf4f08dc1b1916b4e4dcdf5973; sso_uid_tt_ss=8be2fedf4f08dc1b1916b4e4dcdf5973; toutiao_sso_user=5f4dd1ff61d3004d5e98e6a219389734; toutiao_sso_user_ss=5f4dd1ff61d3004d5e98e6a219389734; sid_ucp_sso_v1=1.0.0-KDE5MzYwM2U3NTg0ZDMzMmY4OWM0ZGNmMTE2ZTQzOTZlMDhjYmY4ODYKHwj3pOCE442_BRCVg5ixBhjvMSAMMKyUjJ8GOAZA9AcaAmxxIiA1ZjRkZDFmZjYxZDMwMDRkNWU5OGU2YTIxOTM4OTczNA; ssid_ucp_sso_v1=1.0.0-KDE5MzYwM2U3NTg0ZDMzMmY4OWM0ZGNmMTE2ZTQzOTZlMDhjYmY4ODYKHwj3pOCE442_BRCVg5ixBhjvMSAMMKyUjJ8GOAZA9AcaAmxxIiA1ZjRkZDFmZjYxZDMwMDRkNWU5OGU2YTIxOTM4OTczNA; passport_auth_status=1274478b0961655ea3c34f17b7a66cd1%2C; passport_auth_status_ss=1274478b0961655ea3c34f17b7a66cd1%2C; uid_tt=b5999278db59319450bfa2da0d3b08a5; uid_tt_ss=b5999278db59319450bfa2da0d3b08a5; sid_tt=46ab4c0eddfc6e2b05d9bab782106658; sessionid=46ab4c0eddfc6e2b05d9bab782106658; sessionid_ss=46ab4c0eddfc6e2b05d9bab782106658; publish_badge_show_info=%220%2C0%2C0%2C1713766808977%22; LOGIN_STATUS=1; store-region=cn-js; store-region-src=uid; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=00ddadd2fb8fa96a6ebcadc4ff984462; __security_server_data_status=1; sid_guard=46ab4c0eddfc6e2b05d9bab782106658%7C1713766810%7C5183998%7CFri%2C+21-Jun-2024+06%3A20%3A08+GMT; sid_ucp_v1=1.0.0-KGFkMmE3NmZmMDU0NWI2YTQwZmUyYzNkOGQ2ODRlNmIwMWM1ZTUxYWMKGwj3pOCE442_BRCag5ixBhjvMSAMOAZA9AdIBBoCbGYiIDQ2YWI0YzBlZGRmYzZlMmIwNWQ5YmFiNzgyMTA2NjU4; ssid_ucp_v1=1.0.0-KGFkMmE3NmZmMDU0NWI2YTQwZmUyYzNkOGQ2ODRlNmIwMWM1ZTUxYWMKGwj3pOCE442_BRCag5ixBhjvMSAMOAZA9AdIBBoCbGYiIDQ2YWI0YzBlZGRmYzZlMmIwNWQ5YmFiNzgyMTA2NjU4; download_guide=%223%2F20240422%2F0%22; my_rd=2; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSjloR24yeC9WNE5acml5eHI2T05UYmpNVHF0eTBDR3RkUkd0YkRaUHQ3cmRoU0ZCV1NrdytKTXdFc1FJRXV4cXpvZm1ZbEpjSHp0QlkxNVpQUUlORFk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; odin_tt=7cbc30e891d1c36f86b5f21044e1ba19e7ace990fa5c38b3c8f66c2e799e839a3ea60a1a7245052a6a90a6e86c85ce32; pwa2=%220%7C0%7C3%7C0%22; WallpaperGuide=%7B%22showTime%22%3A1713766689963%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A19%2C%22cursor2%22%3A0%7D; passport_fe_beating_status=false; msToken=9IkhDbvJSCnDPLdXiFv4V0JX_wdNBv3SrVXg60QCKlwE19zBHsZUihy8n_Jv6lhLNDtN4MmGCLnObjI3Nu05vca-UNDHtNVdxcuCX7eynKERgZ8bFWMvdw-7Ag==; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAr4tdtLnCN6YFIi1BLiVC-UsKVfy5XxLSrNGM1QEnQbow4LgvtDaaNqEirMPOwmvS%2F1713801600000%2F0%2F0%2F1713767609891%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAr4tdtLnCN6YFIi1BLiVC-UsKVfy5XxLSrNGM1QEnQbow4LgvtDaaNqEirMPOwmvS%2F1713801600000%2F0%2F1713767009891%2F0%22',
    # 'Referer':'https://www.douyin.com/user/MS4wLjABAAAA5XIQ6_Ai_rqAn7FzADLdqIWMdQSR3ioErGAQ0vGpUPM'
    # }
    # url = 'https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAA5XIQ6_Ai_rqAn7FzADLdqIWMdQSR3ioErGAQ0vGpUPM&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1707&screen_height=960&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7350947635651593780&msToken=8BA4_x-aRpRL1RPhb9V5g1xhlspk-1vkNDMtYlK-LwLgNs7-orHA7TXQ_jQqskbDbIyilTYzPOtW4WTzjmK2uFZR7zoSDa_A8i1znVVWUDVaSQk2HIhMCbfzVz4%3D&a_bogus=dfWhMRhvdEDBkDWh5RcLfY3q6Rp3YkBa0trEMD2fUdVVyL39HMTY9exoqU0v2K6jLG%2FlIb6jy4hcOpeMxQIbA3vIH8WKlICh-g00t-P2so0j5Z0rCDukrUmF-vwltBBp-JV3xcXmy7CGzuRplnAJ5k1cthMeavS%3D'

    awemeid='71'#作品id
    flag1=0
    while 1:
        r = requests.get(url=url,headers=heads)
        r_list = json.loads(r.text)
        aweme=r_list['aweme_list']
        m=0
        i=aweme[0]
        flag=0
        if i['aweme_id']!=awemeid:
            title=i['desc']
            print('该用户已更新')

            #邮件初始化
            subject="你关心的博主已更新"
            body="以下为作品---"+title+"---详细内容"
            msg=MIMEMultipart()
            msg['subject']=subject
            msg['from']=EMAIL_ADDRESS
            msg['to']=EMAIL_ADDRESS
            msg.attach(MIMEText(body,'plain'))
            print("邮件初始化成功")

            awemeid=i['aweme_id']#更新作品id
            createfile=title
            #图文作品
            if i['images']:                              
                n=1
                while 1:
                    if os.path.exists(createfile):
                        createfile=createfile+str(n)
                        n=n+1
                    else:
                        break
                os.mkdir(createfile)
                for j in i['images']:
                    img=j['url_list'][0]
                    imgdown=requests.get(img,headers=heads)
                    filename=createfile+'\\'+str(m)+'.jpg'
                    
                    with open(filename,'wb') as f:
                        f.write(imgdown.content)
                        print(filename,'  保存成功')
                        
                    with open(filename,'rb') as e:
                        filename1=str(m)+'.jpg'
                        part=MIMEImage(e.read())
                        part.add_header('Content-Disposition','attachment',filename=filename1)
                        msg.attach(part)                                                   
                    m=m+1
                print(title,'照片保存成功')
                print("照片附件准备完毕")
                flag=1
            #音视频作品
            if i['video']:
                if flag==1:                                                     
                    video=i['video']['play_addr']['url_list'][0]
                    videodown=requests.get(video,headers=heads)
                    filename=createfile+'\\'+str(m)+'.mp3'
                    with open(filename,'wb') as f:
                        f.write(videodown.content)
                        print(filename,' 保存成功')
                    print(title, '音频保存成功')
                    with open(filename,'rb') as e:
                        filename1=str(m)+'.mp3'
                        mp3part = MIMEApplication(open(filename, 'rb').read())
                        mp3part.add_header('Content-Disposition', 'attachment', filename=filename1)
                        msg.attach(mp3part)
                        print("音频附件准备完毕")
                    m=m+1 
                else:
                    n=1
                    while 1:
                        if os.path.exists(createfile):
                            createfile=createfile+str(n)
                            n=n+1
                        else:
                            break
                    os.mkdir(createfile)
                    awemeid = i['aweme_id']
                    title = i['desc']
                    video=i['video']['play_addr']['url_list'][0]
                    videodown=requests.get(video,headers=heads)
                    filename=createfile+'\\'+str(m)+'.mp4'
                    with open(filename,'wb') as f:
                        f.write(videodown.content)
                        print(filename,' 保存成功')
                    with open(filename,'rb') as e:
                        filedata=e.read

                    with open(filename,'rb') as e:
                        filename1=str(m)+'.mp4'
                        part=MIMEApplication(open(filename,'rb').read())
                        part.add_header('Content-Disposition','attachment',filename=filename1)
                        msg.attach(part)
                        print("视频附件准备完毕")
                    m=m+1
                    print(title, '视频保存成功')
            with smtplib.SMTP_SSL("smtp.163.com",465) as smtp:
                smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
                smtp.send_message(msg)
        else:
            print('最新作品为  --',i['desc'],'-- 暂未更新')
            flag1=0

