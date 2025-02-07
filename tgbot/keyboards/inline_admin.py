# - *- coding: utf- 8 - *-
import gettext
from pathlib import Path
from contextvars import ContextVar
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as ikb

from tgbot.services.api_sqlite import get_paymentx, get_settingsx, get_userx, update_settingsx, get_upaymentx, get_upaycount, create_upayments_row, get_places_in_cityx
from babel import Locale
from tgbot.data.config import get_admins, BOT_DESCRIPTION, I18N_DOMAIN, LOCALES_DIR

from tgbot.middlewares.i18n import I18nMiddleware
i18n = I18nMiddleware(I18N_DOMAIN, LOCALES_DIR)

print(i18n)
_ = i18n.gettext

# Поиск профиля
def select_place_finl(city_id):
    remover = 0
    get_places = get_places_in_cityx(city_id)
    keyboard = InlineKeyboardMarkup()

    for count, a in enumerate(range(remover, len(get_places))):
        print(get_places[a]['place_id'])
        if count < 10:
            keyboard.add(ikb(get_places[a]['name'],
                            callback_data=f"here_event_place:{get_places[a]['place_id']}"))

    return keyboard

# Поиск профиля
def profile_search_finl(user_id, lang):
    if lang == "en":
        chbbtn = "💰 Change Balance"
        tbbtn = "💰 Charge Balance"
        bbtn = "🎁 Purchaces"
        sbtn = "💌 Send Message To User"
        rebtn = "🔄 Refresh"
    if lang == "ru":
        chbbtn = "💰 Изменить баланс"
        tbbtn = "💰 Выдать баланс"
        bbtn = "🎁 Покупки"
        sbtn = "💌 Отправить сообщение пользователю"
        rebtn = "🔄 Обновить"

    return (
        InlineKeyboardMarkup()
        .add(
            ikb(
                chbbtn,
                callback_data=f"admin_user_balance_set:{user_id}",
            ),
            ikb(
                tbbtn,
                callback_data=f"admin_user_balance_add:{user_id}",
            ),
        )
        .add(
            ikb(
                bbtn,
                callback_data=f"admin_user_purchases:{user_id}",
            ),
            ikb(
                sbtn,
                callback_data=f"admin_user_message:{user_id}",
            ),
        )
        .add(
            ikb(
                rebtn,
                callback_data=f"admin_user_refresh:{user_id}",
            )
        )
    )


# Поиск профиля с запросом на продавца
def profile_search_reqs_finl(user_id, lang):
    if lang == "ru":
        submbtn = "Подтвердить"
        declbtn = "Отклонить"
        delbtn = "Удалить"
    if lang == "en":
        submbtn = "Submit"
        declbtn = "Decline"
        delbtn = "Delete"

    return InlineKeyboardMarkup().add(
        ikb(submbtn, callback_data=f"admin_user_request_approve:{user_id}"),
        ikb(declbtn, callback_data=f"admin_user_request_decline:{user_id}"),
        ikb(delbtn, callback_data=f"admin_user_request_delete:{user_id}"),
    )


# Способы пополнения
def payment_choice_finl(user_id, lang):
    keyboard = InlineKeyboardMarkup()
    print("inline_admin")
    print(user_id)
    print(lang)
    count = get_upaycount(user_id)
    print(count['paycount'])
    if count['paycount'] == 0:
        cur = create_upayments_row(user_id)
    else:
        get_payments = get_upaymentx(user_id)

    print(get_payments)
    if lang == "en":
        byqwformbtn = "📋 By QIWI Form"
        byqwphonebtn = "📞 By QIWI Number"
        byqwnickbtn = "Ⓜ By Nickname"
        byyoobtn = "📋 By Yoo Form"
        byfreereqs = "📋 By Free Data"
        bycbbtn = "Coinbase"
    if lang == "ru":
        byqwformbtn = "📋 По QIWI форме"
        byqwphonebtn = "📞 По QIWI номеру"
        byqwnickbtn = "Ⓜ По Никнейму"
        byyoobtn = "📋 По Yoo форме"
        byfreereqs = "📋 Свободные реквизиты"
        bycbbtn = "Coinbase"

    status_form_kb = ikb("✅", callback_data=f"change_payment:Form:False:{user_id}")
    status_number_kb = ikb("✅", callback_data=f"change_payment:Number:False:{user_id}")
    status_nickname_kb = ikb("✅", callback_data=f"change_payment:Nickname:False:{user_id}")
    status_formy_kb = ikb("✅", callback_data=f"change_payment:ForYm:False:{user_id}")
    status_freecredi_kb = ikb("✅", callback_data=f"change_payment:FreeCredi:False:{user_id}")
    status_coinbase_kb = ikb("✅", callback_data=f"change_payment:CoinBase:False:{user_id}")

    if get_payments['way_form'] == "False":
        status_form_kb = ikb("❌", callback_data=f"change_payment:Form:True:{user_id}")
    if get_payments['way_number'] == "False":
        status_number_kb = ikb("❌", callback_data=f"change_payment:Number:True:{user_id}")
    if get_payments['way_nickname'] == "False":
        status_nickname_kb = ikb("❌", callback_data=f"change_payment:Nickname:True:{user_id}")
    if get_payments['way_formy'] == "False":
        status_formy_kb = ikb("❌", callback_data=f"change_payment:ForYm:True:{user_id}")
    if get_payments['way_freecredi'] == "False":
        status_freecredi_kb = ikb("❌", callback_data=f"change_payment:FreeCredi:True:{user_id}")
    if get_payments['way_coinbase'] == "False":
        status_coinbase_kb = ikb("❌", callback_data=f"change_payment:CoinBase:True:{user_id}")

    keyboard.add(ikb(byqwformbtn, url="https://vk.cc/bYjKGM"), status_form_kb)
    keyboard.add(ikb(byqwphonebtn, url="https://vk.cc/bYjKEy"), status_number_kb)
    keyboard.add(ikb(byqwnickbtn, url="https://vk.cc/c8s66X"), status_nickname_kb)
    keyboard.add(ikb(byyoobtn, url="https://vk.cc/bYjKGM"), status_formy_kb)
    keyboard.add(ikb(byfreereqs, url="https://vk.cc/bYjKGM"), status_freecredi_kb)
    keyboard.add(ikb(bycbbtn, url="https://vk.cc/bYjKGM"), status_coinbase_kb)

    return keyboard


# Кнопки с настройками
def settings_open_finl(lang):
    keyboard = InlineKeyboardMarkup()
    get_settings = get_settingsx()
    if lang == "ru":
        settingnotexists = "❌ Не установлено"
        settingexist = "✅ Установлено"
        typenotset = "❌ Тип не задан"
        typeset = "✅:"
        faq = "ℹ FAQ"
        support = "☎ Поддержка"
        tradetype = "☎ Тип площадки"

    if lang == "en":
        settingnotexists = "❌ Empty"
        settingexist = "✅ Exist"
        typenotset = "❌ Platform Type"
        typeset = "✅:"
        faq = "ℹ FAQ"
        support = "☎ Support"
        tradetype = "☎ Platform type"

    if get_settings['misc_support'].isdigit():
        get_user = get_userx(user_id=get_settings['misc_support'])

        if get_user is not None:
            support_kb = ikb(f"@{get_user['user_login']} ✅", callback_data="settings_edit_support")
        else:
            support_kb = ikb(settingnotexists, callback_data="settings_edit_support")
            update_settingsx(misc_support="None")
    else:
        support_kb = ikb(settingexist, callback_data="settings_edit_support")

    if get_settings['misc_faq'] == "None":
        faq_kb = ikb(settingnotexists, callback_data="settings_edit_faq")
    else:
        faq_kb = ikb(settingexist, callback_data="settings_edit_faq")

    if get_settings['type_trade'] is None:
        trade_type_kb = ikb(typenotset, callback_data="settings_edit_trade_type")
    else:
        trade_type_kb = ikb(typeset + str(get_settings['type_trade']), callback_data="settings_edit_type_trade")

    keyboard.add(
        ikb(faq, callback_data="..."), faq_kb
    ).add(
        ikb(support, callback_data="..."), support_kb
    ).add(
        ikb(tradetype, callback_data="..."), trade_type_kb
    )

    return keyboard


# Выключатели
def turn_open_finl(lang):
    keyboard = InlineKeyboardMarkup()
    get_settings = get_settingsx()
    if lang == "ru":
        son = "Включены ✅"
        soff = "Выключены ❌"
        twork = "⛔ Тех. работы"
        tadd = "💰 Пополнения"
        tpays = "🎁 Покупки"

    if lang == "en":
        son = "On ✅"
        soff = "Off ❌"
        twork = "⛔ Tech. Works"
        tadd = "💰 Payments"
        tpays = "🎁 Purchases"

    if get_settings['status_buy'] == "True":
        status_buy_kb = ikb(son, callback_data="turn_buy:False")
    elif get_settings['status_buy'] == "False":
        status_buy_kb = ikb(soff, callback_data="turn_buy:True")

    if get_settings['status_work'] == "True":
        status_twork_kb = ikb(son, callback_data="turn_twork:False")
    elif get_settings['status_work'] == "False":
        status_twork_kb = ikb(soff, callback_data="turn_twork:True")

    if get_settings['status_refill'] == "True":
        status_pay_kb = ikb(son, callback_data="turn_pay:False")
    else:
        status_pay_kb = ikb(soff, callback_data="turn_pay:True")

    keyboard.row(ikb(twork, callback_data="..."), status_twork_kb)
    keyboard.row(ikb(tadd, callback_data="..."), status_pay_kb)
    keyboard.row(ikb(tpays, callback_data="..."), status_buy_kb)

    return keyboard

######################################## МАГАЗИНЫ ########################################
# Изменение магазина
def shop_name_edit_open_finl(shop_id, user_id, remover, lang):
    if lang == "ru":
        ebtn = "🏷 Изм. название"
        dbtn = "❌ Удалить"
        bbtn = "⬅ Вернуться ↩"
    if lang == "en":
        ebtn = "🏷 Change Name"
        dbtn = "❌ Delete"
        bbtn = "⬅ Back Up ↩"

    return (
        InlineKeyboardMarkup()
            .add(
            ikb(
                ebtn,
                callback_data=f"shop_edit_name:{category_id}:{remover}",
            ),
            ikb(
                dbtn,
                callback_data=f"shop_edit_delete:{category_id}:{remover}",
            ),
        )
            .add(
            ikb(
                bbtn,
                callback_data=f"shop_edit_return:{remover}",
            )
        )
    )

# Изменение магазина
def shop_description_edit_open_finl(shop_id, user_id, remover, lang):
    if lang == "ru":
        ebtn = "🏷 Изм. описание"
        dbtn = "❌ Удалить"
        bbtn = "⬅ Вернуться ↩"
    if lang == "en":
        ebtn = "🏷 Change Name"
        dbtn = "❌ Delete"
        bbtn = "⬅ Back Up ↩"

    return (
        InlineKeyboardMarkup()
            .add(
            ikb(
                ebtn,
                callback_data=f"shop_edit_description:{category_id}:{remover}",
            ),
            ikb(
                dbtn,
                callback_data=f"shop_edit_delete:{category_id}:{remover}",
            ),
        )
            .add(
            ikb(
                bbtn,
                callback_data=f"shop_edit_return:{remover}",
            )
        )
    )
######################################## ТОВАРЫ ########################################
# Изменение категории
def category_edit_open_finl(category_id, remover, lang):
    if lang == "ru":
        ebtn = "🏷 Изм. название"
        dbtn = "❌ Удалить"
        bbtn = "⬅ Вернуться ↩"
    if lang == "en":
        ebtn = "🏷 Change Name"
        dbtn = "❌ Delete"
        bbtn = "⬅ Back Up ↩"

    return (
        InlineKeyboardMarkup()
        .add(
            ikb(
                ebtn,
                callback_data=f"category_edit_name:{category_id}:{remover}",
            ),
            ikb(
                dbtn,
                callback_data=f"category_edit_delete:{category_id}:{remover}",
            ),
        )
        .add(
            ikb(
                bbtn,
                callback_data=f"category_edit_return:{remover}",
            )
        )
    )

# Кнопки с удалением категории
def category_edit_delete_finl(category_id, remover, lang):
    if lang == "ru":
        dbtn = "❌ Да, удалить"
        cbtn = "✅ Нет, отменить"

    if lang == "en":
        dbtn = "❌ Yes, Delete Please"
        cbtn = "✅ No, Cancel Please"

    return InlineKeyboardMarkup().add(
        ikb(
            dbtn,
            callback_data=f"category_delete:{category_id}:yes:{remover}",
        ),
        ikb(
            cbtn,
            callback_data=f"category_delete:{category_id}:not:{remover}",
        ),
    )

# Кнопки с удалением категории
def shop_edit_delete_finl2(shop_id, remover, lang):
    if lang == "ru":
        yesbtn = "❌ Да, удалить"
        nobtn =  "✅ Нет, отменить"
    if lang == "en":
        yesbtn = "❌ Да, удалить"
        nobtn =  "✅ Нет, отменить"

    return InlineKeyboardMarkup().add(
        ikb(
            yesbtn,
            callback_data=f"shop_delete:{shop_id}:yes:{remover}",
        ),
        ikb(
            nobtn,
            callback_data=f"shop_delete:{shop_id}:not:{remover}",
        ),
    )

# Кнопки при открытии позиции для изменения
def position_edit_open_finl(position_id, category_id, remover, lang):
    print(lang)
    if lang == "ru":
        chnbtn = "🏷 Изм. название"
        chpbtn = "💰 Изм. цену"
        chdbtn = "📜 Изм. описание"
        chphbtn = "📸 Изм. фото"
        chrbtn = "📜 Изменить остаток"
        chlbtn = "📸 <---<ВП>-->"
        chcbtn = "🏙 Изм. город"
        chsbtn = "🏙 Изм. магазин"
        chclbtn = "🗑 Очистить"
        agbtn = "🎁 Добавить товары"
        prsbtn = "📥 Товары"
        delbtn = "❌ Удалить"
        backbtn = "⬅ Вернуться ↩"
    if lang == "en":
        chnbtn = "🏷 Edit Name"
        chpbtn = "💰 Edit Price"
        chdbtn = "📜 Edit Description"
        chphbtn = "📸 Edit Photo"
        chrbtn = "📜 Edit Rest"
        chlbtn = "📸 <---<ВП>-->"
        chcbtn = "🏙 Edit City"
        chsbtn = "🏙 Edit Shop"
        chclbtn = "🗑 Clear"
        agbtn = "🎁 Add Goods"
        prsbtn = "📥 Goods"
        delbtn = "❌ Delete"
        backbtn = "⬅ Back ↩"

    return (
        InlineKeyboardMarkup()
        .add(
            ikb(
                chnbtn,
                callback_data=f"position_edit_name:{position_id}:{category_id}:{remover}",
            ),
            ikb(
                chpbtn,
                callback_data=f"position_edit_price:{position_id}:{category_id}:{remover}",
            ),
        )
        .add(
            ikb(
                chdbtn,
                callback_data=f"position_edit_description:{position_id}:{category_id}:{remover}",
            ),
            ikb(
                chphbtn,
                callback_data=f"position_edit_photo:{position_id}:{category_id}:{remover}",
            ),
            # добавил 12.08.22    -----------------------------------------------------------
        )
        .add(
            ikb(
                chrbtn,
                callback_data=f"position_edit_rest:{position_id}:{category_id}:{remover}",
            ),
            ikb(
                chlbtn,
                callback_data=f"position_edit_photo:{position_id}:{category_id}:{remover}",
            ),
            # добавил 1.02.23    -----------------------------------------------------------
        )
        .add(
            ikb(
                chcbtn,
                callback_data=f"position_edit_city:{position_id}:{category_id}:{remover}",
            ),
            ikb(
                chsbtn,
                callback_data=f"position_edit_shop:{position_id}:{category_id}:{remover}",
            ),
            # -------------------------------------------------------------------------
        )
        .add(
            ikb(
                chclbtn,
                callback_data=f"position_edit_clear:{position_id}:{category_id}:{remover}",
            ),
            ikb(
                agbtn,
                callback_data=f"products_add_position:{position_id}:{category_id}",
            ),
        )
        .add(
            ikb(
                prsbtn,
                callback_data=f"position_edit_items:{position_id}:{category_id}:{remover}",
            ),
            ikb(
                delbtn,
                callback_data=f"position_edit_delete:{position_id}:{category_id}:{remover}",
            ),
        )
        .add(
            ikb(
                backbtn,
                callback_data=f"position_edit_return:{category_id}:{remover}",
            ),
        )
    )


# Кнопки при открытии позиции для изменения
def artist_edit_open_finl(artist_id, user_id, remover):
    return (
        InlineKeyboardMarkup()
        .add(
            ikb(
                _("🏷 Изм. название", locale=lang),
                callback_data=f"artist_edit_name:{artist_id}:{user_id}:{remover}",
            ),
            ikb(
                _("🏙 Изм. город", locale=lang),
                callback_data=f"artist_edit_city:{artist_id}:{user_id}:{remover}",
            ),
        )
        .add(
            ikb(
                _("📜 Изм. описание", locale=lang),
                callback_data=f"artist_edit_description:{artist_id}:{user_id}:{remover}",
            ),
            ikb(
                _("📸 Изм. фото", locale=lang),
                callback_data=f"artist_edit_photo:{artist_id}:{user_id}:{remover}",
            ),
            # -------------------------------------------------------------------------
        )
        .add(
            ikb(
                _("🗑 Очистить", locale=lang),
                callback_data=f"artist_edit_clear:{artist_id}:{user_id}:{remover}",
            ),
            ikb(
                _("❌ Удалить", locale=lang),
                callback_data=f"artist_edit_delete:{artist_id}:{user_id}:{remover}",
            ),
        )
        .add(
            ikb(
                _("⬅ Вернуться ↩", locale=lang),
                callback_data=f"artist_edit_return:{user_id}:{remover}",
            ),
        )
    )

# Подтверждение удаления позиции
def artist_edit_delete_finl():
    return InlineKeyboardMarkup().add(
        ikb(
            _("❌ Да, удалить", locale=lang),
            callback_data=f"artist_delete:yes:{position_id}:{category_id}:{remover}",
        ),
        ikb(
            _("✅ Нет, отменить", locale=lang),
            callback_data=f"artist_delete:not:{position_id}:{category_id}:{remover}",
        ),
    )


# Подтверждение удаления позиции
def position_edit_delete_finl(position_id, category_id, remover, lang):
    if lang == "ru":
        dbtn = "❌ Да, удалить"
        cbtn = "✅ Нет, отменить"
    if lang == "en":
        dbtn = "❌ Yes, Delete"
        cbtn = "✅ No, Cancel"

    return InlineKeyboardMarkup().add(
        ikb(
            dbtn,
            callback_data=f"position_delete:yes:{position_id}:{category_id}:{remover}",
        ),
        ikb(
            cbtn,
            callback_data=f"position_delete:not:{position_id}:{category_id}:{remover}",
        ),
    )


# Подтверждение очистики позиции
def position_edit_clear_finl(position_id, category_id, remover, lang):
    if lang == "ru":
        clbtn = "❌ Да, очистить"
        ccbtn = "✅ Нет, отменить"
    if lang == "en":
        clbtn = "❌ Yes, Clear"
        ccbtn = "✅ No, Cancel"

    return InlineKeyboardMarkup().add(
        ikb(
            clbtn,
            callback_data=f"position_clear:yes:{position_id}:{category_id}:{remover}",
        ),
        ikb(
            ccbtn,
            callback_data=f"position_clear:not:{position_id}:{category_id}:{remover}",
        ),
    )

# Кнопки при открытии позиции для изменения
def shop_edit_open_finl(shop_id, remover, user_id, lang):
    if lang == "ru":
        chnbtn = "Изменить название"
        chpbtn = "💰 Изм. цену"
        chdbtn = "📜 Изм. описание"
        chfbtn = "📸 Изм. фото"
        chcbtn = "🏙 Изм. город"
        delntn = "❌ Удалить"
        bbbtn = "Вернуться"
    if lang == "en":
        chnbtn = "Change name"
        chpbtn = "💰 Change price"
        chdbtn = "📜 Change description"
        chfbtn = "📸 Change photo"
        chcbtn = "🏙 Change city"
        delntn = "❌ Delete"
        bbbtn = "Back"

    return (
        InlineKeyboardMarkup()
        .add(
            ikb(
                chnbtn,
                callback_data=f"shop_edit_name:{shop_id}:{user_id}:{remover}",
            ),
            ikb(
                chpbtn,
                callback_data=f"shop_edit_price:{shop_id}:{user_id}:{remover}",
            ),
        )
        .add(
            ikb(
                chdbtn,
                callback_data=f"shop_edit_description:{shop_id}:{user_id}:{remover}",
            ),
            ikb(
                chfbtn,
                callback_data=f"shop_edit_photo:{shop_id}:{user_id}:{remover}",
            ),
            # добавил 12.08.22    -----------------------------------------------------------
        )
        .add(
            ikb(
                chcbtn,
                callback_data=f"shop_edit_city:{shop_id}:{user_id}:{remover}",
            ),
            ikb(
                "Для симметрии",
                callback_data=f"shop____edit_photo:{shop_id}:{user_id}:{remover}",
            ),
            # -------------------------------------------------------------------------
        )
        .add(
            ikb(
                "X🗑 Очистить",
                callback_data=f"shop_edit_clear:{shop_id}:{user_id}:{remover}",
            ),
            ikb(
                "X🎁 Добавить товары",
                callback_data=f"shop_add_position:{shop_id}:{user_id}",
            ),
        )
        .add(
            # ikb(_("📥 Товары", locale=lang), callback_data=f"shop_edit_items:{shop_id}:{user_id}:{remover}"),
            ikb(
                delntn,
                callback_data=f"shop_edit_delete:{shop_id}:{user_id}:{remover}",
            ),
        )
        .add(
            ikb(
                bbbtn,
                callback_data=f"shop_edit_return:{user_id}:{remover}",
            ),
        )
    )

# Подтверждение покупки товара
def shop_edit_delete_finl(shop_id, user_id, lang):
    if lang == "ru":
        yesbtn = "✅ Да, удалить"
        nobtn = "❌ Отменить удаление"
    if lang == "en":
        yesbtn = "✅ Yes, delete"
        nobtn = "❌ Cancel Delete"

    return InlineKeyboardMarkup().add(
        ikb(yesbtn, callback_data=f"shop_delete:yes:{shop_id}:{user_id}"),
        ikb(nobtn, callback_data=f"shop_delete:not:{shop_id}:{user_id}"),
    )
