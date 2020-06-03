from config import *


@bot.message_handler(commands=['start'])
def handle_start(message):
    time = str(datetime.now().strftime("%H_%M"))
    #shutil.copy(r'Позов.docx', r'Позов_{0}.docx'.format(str(message.chat.id)+"_"+str(time)))
    #shutil.copy(r'court_bill_blank.docx', r'Судовий_збір_{0}.docx'.format(str(message.chat.id)+"_"+str(time)))
    bot.send_chat_action(message.chat.id, action="typing")
    bot.send_message(message.chat.id, "Привіт " + ("@"+ str(message.from_user.username) if message.from_user.username != None
                                                       else str(message.from_user.first_name)) + "!\nЯ допоможу тобі створити позовну заяву про стягнення заборгованості до господарьского суду")
    bot.send_chat_action(message.chat.id, action="typing")
    msg = bot.send_message(message.chat.id, "Готовий вигравати справу? Напиши мені код ЄДРПОУ відповідача")
    #bot.register_next_step_handler(msg, edr, time)


@bot.message_handler(content_types=["text"])
def edr(message, time):
    if len(message.text) != 8:
        msg = bot.send_message(message.chat.id, "Здається щось не так. Перевір правильність та введи код ще раз")
        bot.register_next_step_handler(msg,edr)
    elif len(message.text) == 8:
        if message.text.isdigit() == False:
            msg = bot.send_message(message.chat.id, "Ми так не домовлялись :) \nВведи тільки цифри ЄДРПОУ")
            bot.register_next_step_handler(msg, edr)
        elif message.text.isdigit() == True:
            url = "https://opendatabot.com/api/v2/company/" + message.text + "?apiKey=legalhack20"
            r = requests.get(url).json()
            adress = r[0]["location"]
            name = r[0]["full_name"]
            person = r[0]["ceo_name"]
            date_bill = str(datetime.now().strftime("%d.%m.%Y"))
            if "м.Київ" in adress or "м. Київ" in adress:
                court = "Господарський суд м. Києва"
                court_adress = "01054, м. Київ, вул. Б. Хмельницького, 44-в"
                money_reciever = "ГУК у м.Києві/м.Київ/22030101"
                court_edr = "37993783"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA918999980313191206083026001"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд м. Києва"
            elif "Київська" in adress:
                court = "Господарський суд Київської області"
                court_adress = "МСП 01032, м. Київ-32, вул. Симона Петлюри , 16/108"
                money_reciever = "ГУК у Київ. обл./м.Київ/22030101"
                court_edr = "37955989"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA708999980313181206083010001"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Київської області"
            elif "Харків" in adress:
                court = "Господарський суд Харківської області"
                court_adress = "61022, м. Харків, майдан Свободи, 5, Держпром, 8-й під'їзд"
                money_reciever = "УК Шевченкі/мХар Шевченківс/22030101"
                court_edr = "37999654"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA868999980313111206083020003"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Харківської області"
            elif "Севастополь" in adress:
                court = "Господарський суд м. Києва"
                court_adress = "01054, м. Київ, вул. Б. Хмельницького, 44-в"
                money_reciever = "ГУК у м.Києві/м.Київ/22030101"
                court_edr = "37993783"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA918999980313191206083026001"
                bugdet_code = "22030101"
                payment_goal = '*;101;' + str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд м. Києва"
            elif "Вінницька" in adress or "Вінниця" in adress:
                court = "Господарський суд Вінницької області"
                court_adress = "21018, м. Вінниця, вулиця Пирогова, 29"
                money_reciever = "УК у м.Вінниці/отг м.Вінниця/22030101"
                court_edr = "38054707"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA748999980313111206083002856"
                bugdet_code = "22030101"
                payment_goal = '*;101;' + str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Вінницької області"
            elif "Крим" in adress:
                court = "Господарський суд Київської області"
                court_adress = "МСП 01032, м. Київ-32, вул. Симона Петлюри , 16/108"
                money_reciever = "ГУК у Київ. обл./м.Київ/22030101"
                court_edr = "37955989"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA708999980313181206083010001"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Київської області"
            elif "Волинська" in adress or "Луцьк" in adress:
                court = "Господарський суд Волинської області"
                court_adress = "43010, м. Луцьк, пр. Волі, 54А, тел.0332-200214"
                money_reciever = "УК у м.Луцьку/Луцька отг/22030101"
                court_edr = "38009628"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA238999980313131206083003550"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Волинської області"
            elif "Дніпро" in adress:
                court = "Господарський суд Дніпропетровської області"
                court_adress = "49600, м. Дніпро, вул. Володимира Винниченка, 1"
                money_reciever = "УК у Собор.р.м.Дніпра/Собор.р/22030101"
                court_edr = "37989269"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA238999980313151206083004005"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Дніпропетровської області"
            elif "Донецьк" in adress:
                court = "Господарський суд Донецької області"
                court_adress = "61022, м. Харків, пр. Науки, 5"
                money_reciever = "УК мХаркові/мХаркiв/22030101"
                court_edr = "37999649"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA628999980313141206083020002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Донецької області"
            elif "Житомир" in adress:
                court = "Господарський суд Житомирської області"
                court_adress = "10002, м. Житомир, майдан Путятинський, 3/65"
                money_reciever = "Житомирська міська отг22030101"
                court_edr = "38035726"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA768999980313111206083006797"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Житомирської області"
            elif "Закарпатська" in adress or "Ужгород" in adress:
                court = "Господарський суд Закарпатської області"
                court_adress = "10002, м. Житомир, майдан Путятинський, 3/65"
                money_reciever = "УК у м.Ужгороді/м.Ужгород/22030101"
                court_edr = "38015610"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA028999980313151206083007002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Закарпатської області"
            elif "Запоріжжя" in adress or "Запорізька" in adress:
                court = "Господарський суд Запорізької області"
                court_adress = "69001, м. Запоріжжя, вул. Гетьманська, 4"
                money_reciever = "УК у м.Запоріжжі/Вознесенівс./22030101"
                court_edr = "38025409"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA908999980313171206083008007"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Запорізької області"
            elif "Івано-Франківськ" in adress:
                court = "Господарський суд Івано-Франківської області"
                court_adress = "вул. Шевченка, 16, м. Івано-Франківськ, 76018"
                money_reciever = "УК у м.Ів.-Фр./ОТГ м.Ів.-Фр./ 22030101"
                court_edr = "37952250"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA688999980313141206083009612"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Івано-Франківської області"
            elif "Кропивницький" in adress or "Кіровоградська" in adress:
                court = "Господарський суд Кіровоградської області"
                court_adress = "25022, м. Кропивницький, вул. В'ячеслава Чорновола, 29/32"
                money_reciever = "УК у м.Кроп./м.Кропивницький/22030101"
                court_edr = "38037409"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA148999980313121206083011002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Кіровоградської області"
            elif "Луганськ" in adress:
                court = "Господарський суд Луганської області"
                court_adress = "61022, м. Харків, проспект Науки, б.5"
                money_reciever = "УК Київськ/мХар Київський/22030101"
                court_edr = "37999675"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA378999980313181206083020004"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Луганської області"
            elif "Львів" in adress:
                court = "Господарський суд Львівської області"
                court_adress = "79014, м. Львів, вул. Личаківська, 128"
                money_reciever = "УКуЛичак.р мЛьв./Личаківський/22030101"
                court_edr = "38007620"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA958999980313141206083013006"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Львівської області"
            elif "Миколаїв" in adress:
                court = "Господарський суд Миколаївської області"
                court_adress = "54001, м. Миколаїв, вул. Адміральська, 22"
                money_reciever = "УК у м.Миколаїв/м.Миколаїв/22030101"
                court_edr = "37992781"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA898999980313131206083014002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Миколаївської області"
            elif "Одеса" in adress or "Одеська" in adress:
                court = "Господарський суд Одеської області"
                court_adress = "проспект Шевченка, 29, Одеса, Одеська область, 65119"
                money_reciever = "УК у м.Одесі/Приморський р-н/22030101"
                court_edr = "38016923"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA078999980313121206083015008"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Одеської області"
            elif "Одеса" in adress or "Одеська" in adress:
                court = "Господарський суд Полтавської області"
                court_adress = "36000, м. Полтава, вул. Зигіна, 1"
                money_reciever = "УК у м.Полтаві/м.Полтава/22030101"
                court_edr = "38019510"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA508999980313171206083016002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Полтавської області"
            elif "м. Рівне" in adress or "м.Рівне" in adress or "Рівненська" in adress:
                court = "Господарський суд Рівненської області"
                court_adress = "33013, м. Рівне, вул. Набережна, 26-А"
                money_reciever = "УК у м.Рiвному/м.Рiвне/22030101"
                court_edr = "38012714"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA678999980313141206083017002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Рівненської області"
            elif "м. Суми" in adress or "м.Суми" in adress or "Сумська" in adress:
                court = "Господарський суд Сумської області"
                court_adress = "проспект ім. Т.Шевченка,18/1, м. Суми, 40011"
                money_reciever = "Сумська міська отг22030101"
                court_edr = "37970593"
                court_bank = "Казначейство України"
                court_bank_code = "899998"
                reciever_bill = "UA868999980313181206083018540"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Сумської області"
            elif "Тернопіль" in adress:
                court = "Господарський суд Тернопільської області"
                court_adress = "46001, м. Тернопіль, вул. Князя Острозького, 14-а"
                money_reciever = "УК у м.Терноп/отг м.Тернопiль/22030101"
                court_edr = "37977726"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA668999980313131206083019751"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Тернопільської області"
            elif "Херсонська" in adress or "м. Херсон" in adress or "м.Херсон" in adress:
                court = "Господарський суд Херсонської області"
                court_adress = "73003, м. Херсон, вул. Театральна (Горького), 18"
                money_reciever = "УК у м Херсоні /м Херсон/22030101"
                court_edr = "37959779"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA798999980313111206083021002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Херсонської області"
            elif "Хмельницький" in adress or "Хмельницької" in adress:
                court = "Господарський суд Хмельницької області"
                court_adress = "29005, м. Хмельницький, майдан Незалежності, 1"
                money_reciever = "УК у м. Хмельниц./м.Хмельниц./22030101"
                court_edr = "38045529"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA238999980313181206083022002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Хмельницької області"
            elif "Черкаси" in adress or "Черкаська" in adress:
                court = "Господарський суд Черкаської області"
                court_adress = "18005, м. Черкаси, бульвар Шевченка, 307"
                money_reciever = "УК у м.Черкасах/Черкаси/22030101"
                court_edr = "38031150"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA408999980313151206083023002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Черкаської області"
            elif "Черкаси" in adress or "Черкаська" in adress:
                court = "Господарський суд Чернівецької області"
                court_adress = "58000, м. Чернівці, вул. О.Кобилянської, 14"
                money_reciever = "Чернівецьке УК/м.Чернiвцi/22030101"
                court_edr = "37978173"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA578999980313121206083024002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Чернівецької області"
            elif "Чернівці" in adress or "Чернівецька" in adress:
                court = "Господарський суд Чернівецької області"
                court_adress = "58000, м. Чернівці, вул. О.Кобилянської, 14"
                money_reciever = "Чернівецьке УК/м.Чернiвцi/22030101"
                court_edr = "37978173"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA578999980313121206083024002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Чернівецької області"
            elif "Чернігів" in adress:
                court = "Господарський суд Чернігівської області"
                court_adress = "14000, м.Чернiгiв, проспект Миру, 20"
                money_reciever = "УК у м.Чернігові/м.Чернiгiв/22030101"
                court_edr = "38054398"
                court_bank = "Казначейство України (ЕАП)"
                court_bank_code = "899998"
                reciever_bill = "UA988999980313191206083025002"
                bugdet_code = "22030101"
                payment_goal = '*;101;'+str("ЄДРПОУ НАШ") + ";Судовий збір, за позовом " + str("Наша назва") + ", Господарський суд Чернігівської області"

            bot.send_message(message.chat.id, "Назва:" + name + "\nВідповідальна особа: " + person + "\nАдреса: " + adress + "\nТериторіальна підсудність: " + court + "\nКод ЭДРПОУ: " + message.text)
            msg = bot.send_message(message.chat.id, "Тепер введи дату виникнення зобов'язання у форматі ДД.ММ.РРРР")
            bot.register_next_step_handler(msg, date_calc, time)

def date_calc(message, time):
    line = message.text
    line_c = copy(line)
    for i in line_c:
        if i.isdigit() == True:
            line_c = re.sub(i, "d", line_c)
        else:
            pass
    if line_c == "dd.dd.dddd":
        date1 = datetime.strptime(str(line), '%d.%m.%Y')
        date2 = datetime.strptime(str(datetime.now().strftime("%d.%m.%Y")), '%d.%m.%Y')
        delta = date2 - date1
        if delta.days >= 30:
            per = 25
        else:
            per = 10
        bot.send_message(message.chat.id, "Різниця між сьогоднішнім днем та днем виникнення зобов'язання - "+ str(delta.days)+ " днів")
        msg = bot.send_message(message.chat.id, 'Тепер введи суму заборгованості використовуючи лише цифри')
        bot.register_next_step_handler(msg, money_calc, time, per)
    else:
        msg = bot.send_message(message.chat.id, "Неправильний формат дати. Введи дату початку зобов'язання у форматі ДД.ММ.РРРР\Наприклад: 01.01.2020")
        bot.register_next_step_handler(msg, date_calc, time)

def money_calc(message, time, per):
    if message.text.isdigit() == True:
        if int(per) == 25:
            debt = int(message.text)
            percent = debt/100*25
            total = debt+percent
        elif int(per) == 10:
            debt = int(message.text)
            percent = debt/100*10
            total = debt+percent
        bot.send_message(message.chat.id, "Сума заборгованості: " + str(debt) + "\nШтраф: " + str(percent) + "\nВсього: " + str(total))
    else:
        msg = bot.send_message(message.chat.id, "Неправильний формат суми заборгованості. Введи суму заборгованості використовуючи лише цифри\nНаприклад: 10000")
        bot.register_next_step_handler(msg,money_calc,time, per)

@bot.message_handler(content_types=["document"])
def handle_doc(message):
    if "sheet" in str(message.document.mime_type):
        bot.send_chat_action(message.chat.id, action="typing")
        bot.send_message(message.chat.id, "Почекай трохи. Зараз всіх засудимо!")
        bot.send_chat_action(message.chat.id, action="typing")
        start_time = datetime.now()
        os.mkdir(str(message.document.file_id))
        url = "https://api.telegram.org/file/bot1285037918:AAFThCZD8y9r-hGvmO0NkOGwrhA_EAsaUx0/" +str((bot.get_file(message.document.file_id)).file_path)
        urllib.request.urlretrieve(url, str(datetime.now().strftime("%d_%h_%Y_%H_%M"))+"_sheet.xlsx")
        #shutil.move(str(datetime.now().strftime("%d_%h_%Y_%H_%M"))+"_sheet.xlsx", str(message.document.file_id))
        wb = load_workbook(str(datetime.now().strftime("%d_%h_%Y_%H_%M"))+"_sheet.xlsx")
        ws = wb["Аркуш1"]
        range_edr = ws['a2':'a1000']
        for i in range_edr:
            if i[0].value != None:
                print(i[0].value)
                url = "https://opendatabot.com/api/v2/company/" + str(int(i[0].value)) + "?apiKey=legalhack20"
                r = requests.get(url).json()
                adress = str(ws["B"+str(range_edr.index(i)+2)].value)
                name = r[0]["full_name"]
                person = r[0]["ceo_name"]
                court = str(ws["C"+str(range_edr.index(i)+2)].value)
                court_adress = str(ws["D" + str(range_edr.index(i) + 2)].value)
                date1 = datetime.strptime(str(ws["F"+str(range_edr.index(i)+2)].value.strftime("%d.%m.%Y")), '%d.%m.%Y')
                date2 = datetime.strptime(str(datetime.now().strftime("%d.%m.%Y")), '%d.%m.%Y')
                delta = date2 - date1
                if delta.days >= 30:
                    per = 25
                else:
                    per = 10
                if int(per) == 25:
                    debt = int(str(int(ws["E"+str(range_edr.index(i)+2)].value)))
                    percent = debt / 100 * 25
                    total = debt + percent
                elif int(per) == 10:
                    debt = int(str(int(ws["E"+str(range_edr.index(i)+2)].value)))
                    percent = debt / 100 * 10
                    total = debt + percent


                print(i[0].value, court, adress, person, per, total)
                shutil.copy(r'Позов_зразок.docx', r'Позов_' + str(int(i[0].value)) + str(range_edr.index(i)) + '.docx')
                doc = DocxTemplate('Позов_' + str(int(i[0].value)) + str(range_edr.index(i))+ '.docx')
                context = {
                    'court': court,
                    "court_adress" : court_adress,
                    "name" : name,
                    "person" : person,
                    "edrpou" : str(int(i[0].value)),
                    'date1' : str(date1),
                    "debt" : debt,
                    "delta" : str(delta),
                    "percent" : str(percent),
                    "total" : str(total)
                }
                doc.render(context)
                doc.save('Позов_' + str(int(i[0].value)) + str(range_edr.index(i)) + '.docx')
                shutil.move('Позов_' + str(int(i[0].value)) + str(range_edr.index(i)) + '.docx',str(message.document.file_id))

        make_archive("Позови_"+str(message.chat.id)+str(datetime.now().strftime("_%H_%M")), format="zip", root_dir=str(message.document.file_id))
        time.sleep(0.5)
        doc = open('Позови_'+str(message.chat.id)+str(datetime.now().strftime("_%H_%M"))+ ".zip", 'rb')
        bot.send_document(message.chat.id,doc)
        print(datetime.now() - start_time)
        bot.send_message(message.chat.id, "Витрати часу: " +str(datetime.now() - start_time))

bot.polling(none_stop=True)

