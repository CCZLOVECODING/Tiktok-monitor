import requests
import json
import os.path
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# 可视化相关
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
import time


import json
from datetime import datetime



if __name__ == '__main__':

    # 初始化数据存储
    timestamps = []
    follower_counts = []

    # 创建图形
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(10, 6))
    line, = ax.plot([], [], 'b-', marker='o', label='粉丝数')
    ax.set_xlabel('时间')
    ax.set_ylabel('粉丝数')
    ax.set_title('抖音粉丝数实时监控')
    ax.grid(True)
    ax.legend()


    heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'Cookie':'store-region-src=uid; live_use_vvc=%22false%22; UIFID_TEMP=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a446b675bf27194f1b48c4a653ef38c0129aca2dfe92e2751df7a31d24f8feb385bc3aa268139f09102299e772c04e06b7; fpk1=U2FsdGVkX19Yw9ZsLOj0lnV63dVEjt9OixNe8CP9CYwA6ULabrEDEywdYO3mgbLDabKV/8plgaNnN9IBAC9Deg==; fpk2=d94a27a56e6a143d4c900b9014d6ba5d; UIFID=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4f7a159e54bbc4a4ce7aeb7862e4d2abae763d2dfdcd8212782e6c6645788140b6efef37f58db076b107eca650da1828cbaf6d73810dcbb048498a2c77c79ca133990a06df4e44a51d131e7d002a9e5a010fadb0937a07dd95b4dd4a0d9ef3cda3faa7809ac2570431e16b13846c65597699191a09889334eca6ae570c7338958; hevc_supported=true; bd_ticket_guard_client_web_domain=2; is_staff_user=false; SelfTabRedDotControl=%5B%5D; store-region=cn-js; dy_swidth=1707; dy_sheight=960; is_dash_user=1; xgplayer_device_id=83048133735; xgplayer_user_id=712531914111; SEARCH_RESULT_LIST_TYPE=%22single%22; WebUgChannelId=%2230006%22; n_mh=hkKrzhBFAOy5qfLAkpFugtuITxsK27XqocRPBCcFy3A; uid_tt=09cf43f1beccfd2f937e5bd26314b492; uid_tt_ss=09cf43f1beccfd2f937e5bd26314b492; sid_tt=2ae4c61fb4fe55dff7349243f6c383bf; sessionid=2ae4c61fb4fe55dff7349243f6c383bf; sessionid_ss=2ae4c61fb4fe55dff7349243f6c383bf; enter_pc_once=1; my_rd=2; __security_mc_1_s_sdk_crypt_sdk=b97d6c42-42df-9d96; __security_mc_1_s_sdk_cert_key=900f87b4-4456-aaf1; s_v_web_id=verify_mcbvhbre_F0lrdc9Q_940p_4pEU_9iyL_0jzyKWiqM93S; passport_csrf_token=923e439c33a8d006a07563ffddde4520; passport_csrf_token_default=923e439c33a8d006a07563ffddde4520; passport_assist_user=CkHR-qKrRlByh6REgKgKU_8HTSo0EdvALMN6MXOZ-OCvTL1EVw8zNlf27qz9TXMD0t34ceSTI3oUASPRzQ_5-l4XUhpKCjwAAAAAAAAAAAAATygSUm19z7U2go5_H9egEYnVhB6bIVMmDR9YZJwpCBY-IUT6vMXGEL5g6EOG5rcU5jQQh4j1DRiJr9ZUIAEiAQM6t3LL; login_time=1750868833084; __security_mc_1_s_sdk_sign_data_key_web_protect=5a8580e1-4b67-bf53; _bd_ticket_crypt_cookie=999fc1995862297ac8e7745054a83cfb; session_tlb_tag=sttt%7C16%7CKuTGH7T-Vd_3NJJD9sODv__________33rb9T2zSGVlxOkHtzxYd7D3O6Xn7kCVAsfK9MQGSIuk%3D; h265ErrorNum=-1; sid_guard=2ae4c61fb4fe55dff7349243f6c383bf%7C1752923402%7C5184000%7CWed%2C+17-Sep-2025+11%3A10%3A02+GMT; sid_ucp_v1=1.0.0-KDU1MTg1ZDZmZGI5MjhkNDIzNzRhNmVjZWRjZTQxOTc0ZDliZDQ5NGIKIQj3pOCE442_BRCK-u3DBhjvMSAMMKyUjJ8GOAVA-wdIBBoCaGwiIDJhZTRjNjFmYjRmZTU1ZGZmNzM0OTI0M2Y2YzM4M2Jm; ssid_ucp_v1=1.0.0-KDU1MTg1ZDZmZGI5MjhkNDIzNzRhNmVjZWRjZTQxOTc0ZDliZDQ5NGIKIQj3pOCE442_BRCK-u3DBhjvMSAMMKyUjJ8GOAVA-wdIBBoCaGwiIDJhZTRjNjFmYjRmZTU1ZGZmNzM0OTI0M2Y2YzM4M2Jm; publish_badge_show_info=%220%2C0%2C0%2C1753277484619%22; __druidClientInfo=JTdCJTIyY2xpZW50V2lkdGglMjIlM0EwJTJDJTIyY2xpZW50SGVpZ2h0JTIyJTNBMCUyQyUyMndpZHRoJTIyJTNBMCUyQyUyMmhlaWdodCUyMiUzQTAlMkMlMjJkZXZpY2VQaXhlbFJhdGlvJTIyJTNBMS41JTJDJTIydXNlckFnZW50JTIyJTNBJTIyTW96aWxsYSUyRjUuMCUyMChXaW5kb3dzJTIwTlQlMjAxMC4wJTNCJTIwV2luNjQlM0IlMjB4NjQpJTIwQXBwbGVXZWJLaXQlMkY1MzcuMzYlMjAoS0hUTUwlMkMlMjBsaWtlJTIwR2Vja28pJTIwQ2hyb21lJTJGMTM4LjAuMC4wJTIwU2FmYXJpJTJGNTM3LjM2JTIwRWRnJTJGMTM4LjAuMC4wJTIyJTdE; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __live_version__=%221.1.3.6365%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A1%7D; live_can_add_dy_2_desktop=%221%22; csrf_session_id=62c5c06a88162fa610be50170b050143; strategyABtestKey=%221753840347.882%22; download_guide=%223%2F20250730%2F0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; playRecommendGuideTagCount=13; totalRecommendGuideTagCount=13; WallpaperGuide=%7B%22showTime%22%3A1747312752553%2C%22closeTime%22%3A0%2C%22showCount%22%3A6%2C%22cursor1%22%3A10%2C%22cursor2%22%3A285%2C%22hoverTime%22%3A1745664290928%7D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAr4tdtLnCN6YFIi1BLiVC-UsKVfy5XxLSrNGM1QEnQbow4LgvtDaaNqEirMPOwmvS%2F1753891200000%2F0%2F0%2F1753848143357%22; __ac_nonce=0688998540004317d1fbd; __ac_signature=_02B4Z6wo00f01QG4CHgAAIDD4nf47xKg1fUBmAzAACjq90; biz_trace_id=a7c1e9d5; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f2735353635353c32313d36303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=5Ycyg0ApjShY0toqm2_r2_q-bUDwhxmTPpa9pey15nMrTgYjpwumcZfQVvdI8-6v_nMTJ0yWxa8nKq0oOWIdpigRKAPaYRF21Zo6LWp_xESt0J5_ThYjpF9q8vhA3LIxytqHx_A9UtmmoAX0YCZGhsIoOWWGK8kPmqZF1h2kod-D5P4Iljh7cI9ShPT8-Pf58Fh7CjCrQGnRGfpmn3Q_ObIaL_XNFXVZYWyyBMYyhZ-uSHswWxcEImoNd-syxpIUdUjOQjoB8RHTkkMRKEF5sFU0bZj2Qe_awqvTD9gjEBOol5ZgGC8w5ieshJy2DmMuQwX6mjfE97OFcXWfYXywOJNzeLNdPaszwWphSu2AHYh_hLK5_4jIvzHksFiGsZoahYqUA0ul-9TAeqdoFxyEoB17iQmC5XHj89OU0TyskgLSuTRhdad9goZsmPyQYFfeHMMITv5jgu7VirJ_vp-xp-hnrWprnGDblDNkwnh3638mbnms_X0avC1y8WcZGct-PsxlqMtpO9_XF4GTHfyAe8G3jzP8Qzle4ikNoA0aEdU%3D; gulu_source_res=eyJwX2luIjoiNzU0M2ZjOGQ1M2I0ODllM2QzNDA1NDBmYmViY2VhOTQ5YjdkNmE0NmQyY2RiODQzN2RiNDY4OTdiNDkzN2RlZiJ9; passport_auth_mix_state=mziydgem2j2i3v5lpxfwanfwaa1zhp1bb7cmme25zyerki50; passport_fe_beating_status=true; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAr4tdtLnCN6YFIi1BLiVC-UsKVfy5XxLSrNGM1QEnQbow4LgvtDaaNqEirMPOwmvS%2F1753891200000%2F1753844333639%2F1753847912328%2F0%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSjloR24yeC9WNE5acml5eHI2T05UYmpNVHF0eTBDR3RkUkd0YkRaUHQ3cmRoU0ZCV1NrdytKTXdFc1FJRXV4cXpvZm1ZbEpjSHp0QlkxNVpQUUlORFk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; ttwid=1%7CEXB34thGmagumqg7Z1ZoveFWGfOm0OlVZm9YSsgzUUk%7C1753847917%7Ce16aeb11a81198b4ee4f4849b622abaa6d82e21ee141216c18df139eca34f445; IsDouyinActive=true; home_can_add_dy_2_desktop=%220%22; odin_tt=ad378b49b4b226fb8fe06d9a117d27d95d8894d9841745b0dc1c640e27f02485ea248354d8bb84831ca23e6081cc659f89cb819e4ebfa74915b81dbdb7ee6f35',
    'Referer':'https://www.douyin.com/user/MS4wLjABAAAACdtHOv8XS_X_PTuqJ3WReO4ka7pBWg7fmzG4wjiIZVkUKFOVtbhizl9GkpdOJ-O1?from_tab_name=main'
    }
    url ='https://www.douyin.com/aweme/v1/web/user/profile/other/?device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&source=channel_pc_web&sec_user_id=MS4wLjABAAAACdtHOv8XS_X_PTuqJ3WReO4ka7pBWg7fmzG4wjiIZVkUKFOVtbhizl9GkpdOJ-O1&personal_center_strategy=1&profile_other_record_enable=1&land_to=1&update_version_code=170400&pc_client_type=1&pc_libra_divert=Windows&support_h265=1&support_dash=1&cpu_core_num=20&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=960&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=138.0.0.0&browser_online=true&engine_name=Blink&engine_version=138.0.0.0&os_name=Windows&os_version=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7350947635651593780&uifid=edf0d417f427c69b9e8dcf334ec311738f5d7ef487ab7a4043d6c18231e232a4f7a159e54bbc4a4ce7aeb7862e4d2abae763d2dfdcd8212782e6c6645788140b6efef37f58db076b107eca650da1828cbaf6d73810dcbb048498a2c77c79ca133990a06df4e44a51d131e7d002a9e5a010fadb0937a07dd95b4dd4a0d9ef3cda3faa7809ac2570431e16b13846c65597699191a09889334eca6ae570c7338958&verifyFp=verify_mcbvhbre_F0lrdc9Q_940p_4pEU_9iyL_0jzyKWiqM93S&fp=verify_mcbvhbre_F0lrdc9Q_940p_4pEU_9iyL_0jzyKWiqM93S&msToken=5ZSM6kGeVzVOz2Kcu1aThCKwtV-50mXk0uIzeyYan-LUJ7xR-DXW1CleMo6VaD4kB7Veo6XOFNjDzuSFttOPKrQDqZOm4Oz_tiTmc9i1RXXymZ0gb8xk_XK5-thzHqzFZuiMT_Nc5it111JYrM9oYzXzUaZuIjWgo5ohRTq45r5ogyjKm9Y%3D&a_bogus=dyUfDwXyxd%2FVKdKSmKJn9eZUdZ2MrP8yPMT%2FbYOPexFIOZeGJ8PIwOGUjxqB4Z9fmSpzioIHPDM%2FYxdcssUTZCnkFmkDuPkSKTdVVW0LM173Y-vg7qfhekbEok4O8uGOQA51iQE1AzloZI5vNrCZAlP97CeNBCR0TqrSdaRU7xgB6GiYV92SeaZL&x-secsdk-web-expire=1753848264369&x-secsdk-web-signature=6c2fd17c625aa0fe9754a4d6ade1c18b'


    funnum_list = []
    time_list = []
    plt.ion()  # 开启交互模式
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title('旺仔小乔粉丝变化')
    while True:
        r = requests.get(url=url, headers=heads)
        r_list = json.loads(r.text)
        user = r_list['user']
        funnum = user['follower_count']
        print(funnum)
        funnum_list.append(funnum)
        # time_list.append(time.strftime('%H:%M:%S'))
        ax.clear()
        ax.plot(funnum_list, marker='o', markerfacecolor='none', label=f'粉丝数：{funnum:,}')  # 空心点，legend显示普通数字
        ax.set_xlabel('time/S')
        
        ax.set_ylabel('the number of fans')
        ax.set_title('Real-time changes in the number of fans')


        # 只更新legend，不影响y轴
        leg = ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=1, frameon=True)
        for text in leg.get_texts():
            text.set_fontsize(30);#字体更大



        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.pause(2) 

