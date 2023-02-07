import requests
import json


def get_data():
    headers = {
        'Accept': 'application/json',
        'Cookie': 'MVID_CITY_ID=CityCZ_35163; MVID_KLADR_ID=5000006300000; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_TIMEZONE_OFFSET=3; MVID_ENVCLOUD=prod1; tmr_detect=0%7C1675809572608; _ga=GA1.2.1464164422.1675808158; _gid=GA1.2.189837419.1675808160; afUserId=f6280e9b-cd28-493b-8d2a-f860742e2d56-p; tmr_lvid=859c0745d7360413b98853cfdb914b26; tmr_lvidTS=1675808161604; _sp_id.d61c=2a8ef859-85ba-4f8f-84b5-d1471ab820ba.1675808160.1.1675809567..1912ea7f-6b93-4b92-b99e-fab63cba955e..2e7ba52a-188e-424c-8495-37e1ca317089.1675808159681.49; _sp_ses.d61c=*; directCrm-session=%7B%22deviceGuid%22%3A%227718f4e5-8e00-401a-aff7-1923a5a218ff%22%7D; mindboxDeviceUUID=7718f4e5-8e00-401a-aff7-1923a5a218ff; _ga_BNX5WPP3YK=GS1.1.1675808158.1.1.1675809562.21.0.0; _ga_CFMZTSS5FM=GS1.1.1675808157.1.1.1675809562.0.0.0; _dc_gtm_UA-1873769-37=1; _dc_gtm_UA-1873769-1=1; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VqTTVYIRV3MUd2UDlFNDN/dCMgDyFjc0MWJHJ5e0Exa1xAeiNkSGZhTx8vPRM5LCEIDSc5GjhuH2RMYCVLXlZqJh8YfHMjVwgRXENHcGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0Jzei5DZSVgTVslSVtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=0wRBeA==; cfidsgib-w-mvideo=vy8bOXxM1ZF7icJTq8WXlQTTkk8jCK/G/EVK0gi8fsEqaf1reijGu6WA/zRe5/bdxePd17F5PeBimCm/5GRl+HKwJgwXAdKY/xPXXMxRTVlvotPwoYRcisY2yy7osCDTJREheQcQg+PeY5V/sP4poVjSYiuffoed8reK8V0=; fgsscgib-w-mvideo=19aS40890a539a4fb299065b54ee13ccb288f6e9; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VqTTVYIRV3MUd2UDlFNDN/dCMgDyFjc0MWJHJ5e0Exa1xAeiNkSGZhTx8vPRM5LCEIDSc5GjhuH2RMYCVLXlZqJh8YfHMjVwgRXENHcGUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0Jzei5DZSVgTVslSVtJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=0wRBeA==; cfidsgib-w-mvideo=vy8bOXxM1ZF7icJTq8WXlQTTkk8jCK/G/EVK0gi8fsEqaf1reijGu6WA/zRe5/bdxePd17F5PeBimCm/5GRl+HKwJgwXAdKY/xPXXMxRTVlvotPwoYRcisY2yy7osCDTJREheQcQg+PeY5V/sP4poVjSYiuffoed8reK8V0=; fgsscgib-w-mvideo=19aS40890a539a4fb299065b54ee13ccb288f6e9; cfidsgib-w-mvideo=AV0jpcSB+e+61jG1ZTojBe05S4AoROj3QV46twmpdNm9sC6AYdedrkyc3fy8l9e0kj56CduuUlmh4SUnXIBM6GkiAPBMNHch6Hs4CvPgr9fJy2UJBWH6XFrJP/lYU142SmITgOYNCjh3R8JTKumS4awmIXcwxJ+M/q2r7Bc=; gsscgib-w-mvideo=BATAvBd9x0efH+UP/MDM6BgBEx/q9jiTKBldMWc1j0syOqVzHnc/VxPSvJOSiXaoZ93v+IPdgz69bJuTS9j2uq/My5Y06T/NYKfbs43/xrHUmarpeoer4u6YX5ZgKgbRARsKSNetQshuswnAZZxLIYArVOIJ7N1Yl9qvR/eCaTUMyMBW4aFYNx9xjUrDQfBhVniAtQ4o+2CQNcSdDoagSVTaVxxiLbLuJOY2ydW2XfADOCu2HaW+QB4NYMn6AQ==; gsscgib-w-mvideo=BATAvBd9x0efH+UP/MDM6BgBEx/q9jiTKBldMWc1j0syOqVzHnc/VxPSvJOSiXaoZ93v+IPdgz69bJuTS9j2uq/My5Y06T/NYKfbs43/xrHUmarpeoer4u6YX5ZgKgbRARsKSNetQshuswnAZZxLIYArVOIJ7N1Yl9qvR/eCaTUMyMBW4aFYNx9xjUrDQfBhVniAtQ4o+2CQNcSdDoagSVTaVxxiLbLuJOY2ydW2XfADOCu2HaW+QB4NYMn6AQ==; AF_SYNC=1675808162541; CACHE_INDICATOR=true; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_VIEWED_PRODUCTS=; bIPs=1595647062; flacktory=no; BIGipServeratg-ps-prod_tcp80=2919554058.20480.0000; BIGipServeratg-ps-prod_tcp80_clone=2919554058.20480.0000; MVID_GTM_BROWSER_THEME=1; SMSError=; authError=; deviceType=desktop; flocktory-uuid=9a6fb5e4-67c2-4709-912b-dae819764e4b-3; adrcid=AD2S3ptm-xbMDrzkrcfnk-g; adrdel=1; advcake_session_id=c9bba56e-7b67-deae-dbe7-70937a44559b; advcake_track_id=f0adaab6-2117-48fe-babd-aa9255a889a8; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=043f356f-c568-4163-8cd5-daa9564ddca6; uxs_uid=017dcb80-a735-11ed-b37b-bd479d9c070b; JSESSIONID=qBxkjvNB4Q3hPKR890y8F8f2QYynFTzT3QgvGwqxnPlJlbQnstbn!-925576899; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; wurfl_device_id=generic_web_browser; _ym_d=1675808160; _ym_isad=2; _ym_uid=1675808160125512875; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_COOKIE=3500; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_IMG_RESIZE=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MCLICK_NEW=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MULTIOFFER=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_SERVICES=111; MVID_TYP_CHAT=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; __lhash_=8531d1e64cd331dd2a84f9ad99441227; MVID_CREDIT_AVAILABILITY=true; MVID_WEB_SBP=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; HINTS_FIO_COOKIE_NAME=2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GUEST_ID=20660180981; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=1; MVID_GEOLOCATION_NEEDED=false',
        'Connection': 'keep-alive',
        'Accept-Language': 'ru',
        'Host': 'www.mvideo.ru',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15',
        'Referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'x-set-application-id': 'cff5536a-5650-4a5a-a1b6-13ffb46d0b8b',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=6ca61a1f483f4cf9acd21be139ba0b0a,sentry-sample_rate=0.5',
        'sentry-trace': '6ca61a1f483f4cf9acd21be139ba0b0a-a902ea5fda6c7b56-0',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params,
                            headers=headers).json()
    # print(response)


    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)


    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', headers=headers, json=json_data).json()
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))


    products_ids_str = ",".join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)


    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        products_id = item.get('productId')

        if products_id in products_prices:
            prices = products_prices[products_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
