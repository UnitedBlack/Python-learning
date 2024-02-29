import requests

cookies = {
    '__ddg1_': 'ikQWIvnrAuGLtsYuFHMp',
    '_xsrf': 'bb1a2365a8e36708fe30e0c812b20fe1',
    'hhtoken': 'okoC7RpB2_!a7_Q12j3pEF2yRVY0',
    'hhuid': 'RdGxZJTZR6I5OWT!QnUwHw--',
    'crypted_hhuid': 'F2CC07FECC1E3CB0757AA1330159551D030509DED3D2B50FDAE2772F57D60874',
    'iap.uid': '79526e710cc842ad8c954f55f466f64c',
    'redirect_host': 'hh.ru',
    'region_clarified': 'hh.ru',
    'display': 'desktop',
    'GMT': '3',
    'regions': '1',
    'hhrole': 'applicant',
    'crypted_id': 'B12C57702CB0A1ED747E44D10A918C45A5471C6F722104504734B32F0D03E9F8',
    'hhul': '71460e98dd0baeab2de9a6e03781ff2fa487c0ad9ac7f8537e7962c9b15f20bb',
    'device_breakpoint': 'l',
    'total_searches': '1',
    '_hi': '103005699',
    'device_magritte_breakpoint': 'l',
    'cfidsgib-w-hh': 'FVlpCkpGO3YG41ciYcl+jOZfmfL2zi6zIfqzMCh0HBIx5ooq8ARnfZAlOsgjDfRWC11IqWeBmIMXLRwlcsZK6XeWEhgw+LD31A+HeyHR7yOZ+wFwEOQgmQwXibaR6+0w87uyb8JIvs9Dc0cZCxUTVD2q15hFlYqkYhA0w0Q=',
    'gsscgib-w-hh': 'KWwZzn8CafgzNqVKLrO7I6H9RCduCdomr7z9Kn/3ibsHGkCLHfKSXeL/QvSq2a7vCEsZJGsl6sXoGaioysOnbGjTkPCFqGHKn0O0BW8opJGM87zkfOpRBNcGBQ/jdoj/56J2IwNJnkyE/t8hjap4YosjkRzfG3yt2wcRC66G4RTb1A1zpsfBVSRAukNTIfXPL49MVg77QmsjI/qBMsmjC5D+JjLdzQiQkgcPWXC2X0QDM5UVr7zvO2Lh/oQxC3Izf0e5/Yc=',
    '__zzatgib-w-hh': 'MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LXy8xcWggZXoVVUcSCHslTBl9bVkNfzxeb0RwLitxZlFjOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEW1Z9KxoYe20lVRAMVy8NPjteLW8PKhMjZHYhP04hC00+KlwVNk0mbjN3RhsJHlksfEspNRNRey4bFn8nKAsPE2JwSG10K20hH2h4YiJ1Dn5+V0wUeyQqCA8QW3EzaWVpcC9gIBIlEU1HGEVkW0I2KBVLcU8cenZffSpBbiFlSGAjRVdTCS4Ve0M8YwxxFU11cjgzGxBhDyMOGFgJDA0yaFF7CT4VHThHKHIzd2UqO2gdX0xfKExHSWtlTlNCLGYbcRVNCA00PVpyIg9bOSVYCBI/CyYfGntxJFYLDV1DSm1vG382XRw5YxEOIRdGWF17TEA=lwY9Ag==',
    'fgsscgib-w-hh': 'Qcvv2bb169f89d6e8199071709ecbd663618bcf6',
    'cfidsgib-w-hh': 'Kj/axjcmTrttSLpFkdPpNaIVInDCbTnvDSUaZkK7TyjQhnrxwuqROdIdc3m0b1jLmjqhMplir8qndyESplEGdoXHxIVJeGq/tdC4h+HvJagaIQCBJQq0XU1XFFjGBBIP2zx8v9E5Kk90Xhe3zBgm2Q97n8XYwiZM6stIG+s=',
}

headers = {
    'authority': 'hh.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__ddg1_=ikQWIvnrAuGLtsYuFHMp; _xsrf=bb1a2365a8e36708fe30e0c812b20fe1; hhtoken=okoC7RpB2_!a7_Q12j3pEF2yRVY0; hhuid=RdGxZJTZR6I5OWT!QnUwHw--; crypted_hhuid=F2CC07FECC1E3CB0757AA1330159551D030509DED3D2B50FDAE2772F57D60874; iap.uid=79526e710cc842ad8c954f55f466f64c; redirect_host=hh.ru; region_clarified=hh.ru; display=desktop; GMT=3; regions=1; hhrole=applicant; crypted_id=B12C57702CB0A1ED747E44D10A918C45A5471C6F722104504734B32F0D03E9F8; hhul=71460e98dd0baeab2de9a6e03781ff2fa487c0ad9ac7f8537e7962c9b15f20bb; device_breakpoint=l; total_searches=1; _hi=103005699; device_magritte_breakpoint=l; cfidsgib-w-hh=FVlpCkpGO3YG41ciYcl+jOZfmfL2zi6zIfqzMCh0HBIx5ooq8ARnfZAlOsgjDfRWC11IqWeBmIMXLRwlcsZK6XeWEhgw+LD31A+HeyHR7yOZ+wFwEOQgmQwXibaR6+0w87uyb8JIvs9Dc0cZCxUTVD2q15hFlYqkYhA0w0Q=; gsscgib-w-hh=KWwZzn8CafgzNqVKLrO7I6H9RCduCdomr7z9Kn/3ibsHGkCLHfKSXeL/QvSq2a7vCEsZJGsl6sXoGaioysOnbGjTkPCFqGHKn0O0BW8opJGM87zkfOpRBNcGBQ/jdoj/56J2IwNJnkyE/t8hjap4YosjkRzfG3yt2wcRC66G4RTb1A1zpsfBVSRAukNTIfXPL49MVg77QmsjI/qBMsmjC5D+JjLdzQiQkgcPWXC2X0QDM5UVr7zvO2Lh/oQxC3Izf0e5/Yc=; __zzatgib-w-hh=MDA0dC0jViV+FmELHw4/aQsbSl1pCENQGC9LXy8xcWggZXoVVUcSCHslTBl9bVkNfzxeb0RwLitxZlFjOVURCxIXRF5cVWl1FRpLSiVueCplJS0xViR8SylEW1Z9KxoYe20lVRAMVy8NPjteLW8PKhMjZHYhP04hC00+KlwVNk0mbjN3RhsJHlksfEspNRNRey4bFn8nKAsPE2JwSG10K20hH2h4YiJ1Dn5+V0wUeyQqCA8QW3EzaWVpcC9gIBIlEU1HGEVkW0I2KBVLcU8cenZffSpBbiFlSGAjRVdTCS4Ve0M8YwxxFU11cjgzGxBhDyMOGFgJDA0yaFF7CT4VHThHKHIzd2UqO2gdX0xfKExHSWtlTlNCLGYbcRVNCA00PVpyIg9bOSVYCBI/CyYfGntxJFYLDV1DSm1vG382XRw5YxEOIRdGWF17TEA=lwY9Ag==; fgsscgib-w-hh=Qcvv2bb169f89d6e8199071709ecbd663618bcf6; cfidsgib-w-hh=Kj/axjcmTrttSLpFkdPpNaIVInDCbTnvDSUaZkK7TyjQhnrxwuqROdIdc3m0b1jLmjqhMplir8qndyESplEGdoXHxIVJeGq/tdC4h+HvJagaIQCBJQq0XU1XFFjGBBIP2zx8v9E5Kk90Xhe3zBgm2Q97n8XYwiZM6stIG+s=',
    'referer': 'https://hh.ru/search/vacancy?text=%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%BE%D0%B2%D1%8B%D0%B9+%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA+python&salary=&ored_clusters=true&area=1',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
}

params = {
    'from': '',
    'query': '',
}

