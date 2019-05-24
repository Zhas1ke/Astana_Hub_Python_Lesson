def get_field(lst, name):
	if name in lst:
		return 1
	else:
		return 0

def parse_options(options):
	options = [i.strip() for i in options.split(',')]
	
	disks = get_field(options, 'литые диски')
	toning = get_field(options, 'тонировка')
	luke = get_field(options, 'люк')
	panoramic_roof = get_field(options, 'панорамная крыша')
	kangaroo = get_field(options, 'кенгурятник')
	spoiler = get_field(options, 'спойлер')
	body_kit = get_field(options, 'обвес')
	winch = get_field(options, 'лебёдка')
	windscreens = get_field(options, 'ветровики')
	railings = get_field(options, 'рейлинги')
	trunk = get_field(options, 'багажник')
	hitch = get_field(options, 'фаркоп')

	xenon = get_field(options, 'ксенон')
	bixenone = get_field(options, 'биксенон')
	crystal_optics = get_field(options, 'хрустальная оптика')
	lenticular_optics = get_field(options, 'линзованная оптика')
	daytime_lights = get_field(options, 'дневные ходовые огни')
	fog_lights = get_field(options, 'противотуманки')
	lights_washer = get_field(options, 'омыватель фар')
	lights_corrector = get_field(options, 'корректор фар')
	heated_mirrors = get_field(options, 'обогрев зеркал')

	velours = get_field(options, 'велюр')
	leather = get_field(options, 'кожа')
	wood = get_field(options, 'дерево')
	alcantara = get_field(options, 'алькантара')
	combinated = get_field(options, 'комбинированный')
	curtains = get_field(options, 'шторки')

	audio_system = get_field(options, 'аудиосистема')
	built_in_phone = get_field(options, 'встроенный телефон')
	bluetooth = get_field(options, 'bluetooth')
	cd = get_field(options, 'CD')
	cd_changer = get_field(options, 'CD-чейнджер')
	mp3 = get_field(options, 'MP3')
	usb = get_field(options, 'USB')
	dvd = get_field(options, 'DVD')
	dvd_changer = get_field(options, 'DVD-чейнджер')
	subwoofer = get_field(options, 'сабвуфер')

	power_steering = get_field(options, 'ГУР')
	abs = get_field(options, 'ABS')
	srs = get_field(options, 'SRS')
	winter_mode = get_field(options, 'зимний режим')
	sport_mode = get_field(options, 'спортивный режим')
	turbo = get_field(options, 'турбонаддув')
	turbo_timer = get_field(options, 'турботаймер')
	alarm_system = get_field(options, 'сигнализация')
	autostart = get_field(options, 'автозапуск')
	immobilizer = get_field(options, 'иммобилайзер')
	keyless_access = get_field(options, 'бесключевой доступ')
	full_electropackage = get_field(options, 'полный электропакет')
	centro_lock = get_field(options, 'центрозамок')
	air_condition = get_field(options, 'кондиционер')
	climate_control = get_field(options, 'климат-контроль')
	cruise_control = get_field(options, 'круиз-контроль')
	on_board_computer = get_field(options, 'бортовой компьютер')
	gps = get_field(options, 'навигационная система')
	multi_wheel = get_field(options, 'мультируль')
	heated_wheel = get_field(options, 'подогрев руля')
	heated_sits = get_field(options, 'подогрев сидений')
	heated_rear_sits = get_field(options, 'подогрев задних сидений')
	seat_ventilation = get_field(options, 'вентиляция сидений')
	seat_memory = get_field(options, 'память сидений')
	wheel_memory = get_field(options, 'память руля')
	parktrnics = get_field(options, 'парктроники')
	rear_view_camera = get_field(options, 'камера заднего вида')
	light_sensor = get_field(options, 'датчик света')
	rain_sensor = get_field(options, 'датчик дождя')
	tire_pressure_sensor = get_field(options, 'датчик давления в шинах')
	air_suspension = get_field(options, 'пневмоподвеска')
	changeable_clearance = get_field(options, 'изменяемый клиренс')

	freshly_fitted = get_field(options, 'свежепригнан')
	freshly_supplied = get_field(options, 'свежедоставлен')
	tax_paid = get_field(options, 'налог уплачен')
	ti_performed = get_field(options, 'техосмотр пройден')
	investment_not_required = get_field(options, 'вложений не требует')


	a_dict = {
		'disks' : disks,
		'toning' : toning,
		'luke' : luke,
		'panoramic_roof' : panoramic_roof,
		'kangaroo' : kangaroo,
		'spoiler' : spoiler,
		'body_kit' : body_kit,
		'winch' : winch,
		'windscreens' : windscreens,
		'railings' : railings,
		'trunk' : trunk,
		'hitch' : hitch,

		'xenon' : xenon,
		'bixenone' : bixenone,
		'crystal_optics' : crystal_optics,
		'lenticular_optics' : lenticular_optics,
		'daytime_lights' : daytime_lights,
		'fog_lights' : fog_lights,
		'lights_washer' : lights_washer,
		'lights_corrector' : lights_corrector,
		'heated_mirrors' : heated_mirrors,

		'velours' : velours,
		'leather' : leather,
		'wood' : wood,
		'alcantara' : alcantara,
		'combinated' : combinated,
		'curtains' : curtains,

		'audio_system' : audio_system,
		'built_in_phone' : built_in_phone,
		'bluetooth' : bluetooth,
		'cd' : cd,
		'cd_changer' : cd_changer,
		'mp3' : mp3,
		'usb' : usb,
		'dvd' : dvd,
		'dvd_changer' : dvd_changer,
		'subwoofer' : subwoofer,

		'power_steering' : power_steering,
		'abs' : abs,
		'srs' : srs,
		'winter_mode' : winter_mode,
		'sport_mode' : sport_mode,
		'turbo' : turbo,
		'turbo_timer' : turbo_timer,
		'alarm_system' : alarm_system,
		'autostart' : autostart,
		'immobilizer' : immobilizer,
		'keyless_access' : keyless_access,
		'full_electropackage' : full_electropackage,
		'centro_lock' : centro_lock,
		'air_condition' : air_condition,
		'climate_control' : climate_control,
		'cruise_control' : cruise_control,
		'on_board_computer' : on_board_computer,
		'gps' : gps,
		'multi_wheel' : multi_wheel,
		'heated_wheel' : heated_wheel,
		'heated_sits' : heated_sits,
		'heated_rear_sits' : heated_rear_sits,
		'seat_ventilation' : seat_ventilation,
		'seat_memory' : seat_memory,
		'wheel_memory' : wheel_memory,
		'parktrnics' : parktrnics,
		'rear_view_camera' : rear_view_camera,
		'light_sensor' : light_sensor,
		'rain_sensor' : rain_sensor,
		'tire_pressure_sensor' : tire_pressure_sensor,
		'air_suspension' : air_suspension,
		'changeable_clearance' : changeable_clearance,

		'freshly_fitted' : freshly_fitted,
		'freshly_supplied' : freshly_supplied,
		'tax_paid' : tax_paid,
		'ti_performed' : ti_performed,
		'investment_not_required' : investment_not_required
	}
	return a_dict

def get_all_options(page):
	features = page.select('dl.clearfix.dl-horizontal.description-params dt.value-title') 
	values = page.select('dl.clearfix.dl-horizontal.description-params dd.value.clearfix')

	features_strip = []
	values_strip = []

	for feature in features:
		feature_strip = feature.get_text().strip()
		if (feature_strip != ''):
			features_strip.append(feature_strip)

	for value in values:
		value_strip = value.get_text().strip()
		if (value_strip != ''):
			values_strip.append(value_strip)

	pairs = {}
	for i in range(0, len(features_strip)):
		pairs[features_strip[i]] = values_strip[i]

	city = pairs['Город']
	body = pairs['Кузов']
	s = pairs['Объем двигателя, л']
	engine_type = s[s.find("(") + 1 : s.find(")")]
	volume = float(s[:s.find("(")])

	transmission = pairs['Коробка передач']
	helm = pairs['Руль']
	try:
		color = pairs['Цвет'].split()[0]
		metallic = len(pairs['Цвет'].split()) - 1
	except:
		color = ''
		metallic = 0
	try:
		drive = pairs['Привод']
	except:
		drive = ''
	custom = pairs['Растаможен']
	try:
		mileage = int(''.join(re.findall('\d+', pairs['Пробег'])))
	except:
		mileage = None

	index = page.select('div.a-title__container')[0].get_text().split().index('года')
	year = int(page.select('div.a-title__container')[0].get_text().split()[index - 1])
	age = date.today().year - year
	
	price_string = page.select('span.a-price__text')[0].get_text().strip()[:-1]
	price = int(''.join(re.findall('\d+', price_string)))
	
	try:
		options = page.select('div.a-params')[0].get_text().strip()
	except:
		options = ''

	try:
		photos = len(page.select('ul.photo-list')[0])
	except:
		photos = 0

	try:
		description = page.select('div.description-text')[0].get_text().strip()
		description = ' '.join(description.split())
	except:
		description = ''

	main_options = {
		'ads_id': ads_id,
		'link': link,
		'city': city,
		'manufacturer': manufacturer,
		'model': model,
		'body': body,
		'year': year,
		'age': age,
		'price': price,
		'volume': volume,
		'engine_type': engine_type,
		'transmission': transmission,
		'mileage': mileage,
		'helm': helm,
		'color': color,
		'metallic': metallic,
		'photos': photos,
		'drive': drive,
		'description': description
	}
	
	# print (main_options)
	# input()

	# views = page.select('div.col-sm-4.nb-views')[0].get_text().strip()
	# print (views)
	# comments = page.select('div.comments-header')[0].get_text().strip()
	# print (comments)
	# input()
	additional_options = parse_options(options)

	all_options = main_options.copy()
	all_options.update(additional_options)
	print (all_options)
	return all_options