#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def all_messages():
    """
    keep all messages in ar

    Returns:
        all messages in JSON
    """
    return \
        {
            "scan_started": "بدأ محرك Nettacker ...",
            "options": "python nettacker.py [خيارات]",
            "help_menu": "عرض قائمة مساعدة Nettacker",
            "license": "يرجى قراءة الترخيص والاتفاقيات https://github.com/OWASP/Nettacker",
            "engine": "محرك",
            "engine_input": "خيارات إدخال المحرك",
            "select_language": "اختر لغة {0}",
            "range": "مسح جميع عناوين IP في النطاق",
            "subdomains": "البحث عن النطاقات الفرعية ومسحها ضوئيًا",
            "thread_number_connections": "أرقام مؤشر الترابط للاتصالات إلى مضيف",
            "thread_number_hosts": "أرقام مؤشر الترابط لمضيفي المسح الضوئي",
            "save_logs": "احفظ كل السجلات في الملف (results.txt ، results.html ، results.json)",
            "target": "استهداف",
            "target_input": "خيارات الإدخال الهدف",
            "target_list": "قائمة الهدف (الأهداف) ، منفصلة مع \"،\"",
            "read_target": "قراءة الهدف (الأهداف) من الملف",
            "scan_method_options": "خيارات طريقة المسح",
            "choose_scan_method": "اختر طريقة المسح الضوئي {0}",
            "exclude_scan_method": "اختر طريقة الفحص لاستبعاد {0}",
            "username_list": "اسم المستخدم (أسماء) ، منفصلة مع \"،\"",
            "username_from_file": "قراءة اسم المستخدم (ق) من الملف",
            "password_seperator": "كلمة (كلمات) المرور ، منفصلة مع \"،\"",
            "read_passwords": "قراءة كلمة (كلمات) من الملف",
            "port_seperator": "قائمة port (s) ، منفصلة مع \"،\"",
            "time_to_sleep": "وقت للنوم بين كل طلب",
            "error_target": "لا يمكن تحديد الهدف (الأهداف)",
            "error_target_file": "لا يمكن تحديد الهدف (الأهداف) ، غير قادر على فتح الملف: {0}",
            "thread_number_warning": "فمن الأفضل استخدام عدد الخيط أقل من 100 ، راجع للشغل نحن نواصل ...",
            "set_timeout": "تعيين المهلة إلى {0} ثانية ، إنها كبيرة جدًا ، أليس كذلك؟ بالمناسبة نحن نواصل ...",
            "scan_module_not_found": "وحدة المسح هذه [{0}] غير موجودة!",
            "error_exclude_all": "لا يمكنك استبعاد جميع طرق الفحص",
            "exclude_module_error": "الوحدة {0} التي حددتها لاستبعادها غير موجودة!",
            "method_inputs": "أدخل مدخلات الطرق ، على سبيل المثال: ftp_brute_users = test و "
                             "admin & ftp_brute_passwds = read_from_file: /tmp/pass.txt&ftp_brute_port=21",
            "error_reading_file": "لا يمكن قراءة الملف {0}",
            "error_username": "لا يمكن تحديد اسم المستخدم (أسماء المستخدمين) ، غير قادر على فتح الملف: {0}",
            "found": "تم العثور على {0}! ({1}: {2})",
            "error_password_file": "لا يمكن تحديد كلمة (كلمات) المرور ، غير قادر على فتح الملف: {0}",
            "file_write_error": "الملف \"{0}\" غير قابل للكتابة!",
            "scan_method_select": "يرجى اختيار طريقة المسح الخاصة بك!",
            "remove_temp": "إزالة الملفات المؤقتة!",
            "sorting_results": "نتائج الفرز!",
            "done": "فعله!",
            "start_attack": "البدء في الهجوم {0} ، {1} من {2}",
            "module_not_available": "هذه الوحدة \"{0}\" غير متوفرة",
            "error_platform": "للأسف ، يمكن تشغيل هذا الإصدار من البرنامج على Linux / osx / windows.",
            "python_version_error": "إصدار بيثون الخاص بك غير معتمد!",
            "skip_duplicate_target": "تخطي الهدف المكرر (قد يكون لبعض النطاقات الفرعية "
                                     "/ النطاقات نفس عناوين IP ونطاقات)",
            "unknown_target": "نوع غير معروف من الهدف [{0}]",
            "checking_range": "التحقق من {0} النطاق ...",
            "checking": "جارٍ التحقق {0} ...",
            "HOST": "مضيف",
            "USERNAME": "اسم المستخدم",
            "PASSWORD": "كلمه السر",
            "PORT": "ميناء",
            "TYPE": "اكتب",
            "DESCRIPTION": "وصف",
            "verbose_level": "مستوى وضع verbose (0-5) (افتراضي 0)",
            "software_version": "عرض نسخة البرنامج",
            "check_updates": "فحص التحديثات",
            "outgoing_proxy": "الاتصالات الصادرة "
                              "الوكيل (الجوارب). example socks5: 127.0.0.1:9050، socks: //127.0.0.1: 9050"
                              " socks5: //127.0.0.1: 9050 or socks4: socks4: //127.0.0.1: 9050، authentication: "
                              "socks: // username: password @ 127.0.0.1 ، socks4: // اسم المستخدم:"
                              " password@127.0.0.1 ، socks5: // اسم المستخدم: password@127.0.0.1",
            "valid_socks_address": "يرجى إدخال عنوان ومنفذ جوارب ساري المفعول. مثال socks5: 127.0.0.1:9050 ، الجوارب:"
                                   " //127.0.0.1: 9050 ، socks5: //127.0.0.1: 9050 أو socks4: socks4: //127.0.0.1:"
                                   " 9050 ، المصادقة: socks: // username: password @ 127.0.0.1 "
                                   "، socks4: // اسم المستخدم: password@127.0.0.1 ،"
                                   " socks5: // اسم المستخدم: password@127.0.0.1",
            "connection_retries": "إعادة المحاولة عند انتهاء مهلة الاتصال (افتراضي 3)",
            "ftp_connection_timeout": "اتصال ftp {0}: مهلة {1} ، تخطي {2}: {3}",
            "login_successful": "مسجلا بنجاح!",
            "login_list_error": "مسجّل في بنجاح ، رفض الإذن لقائمة COMMAND!",
            "ftp_connection_failed": "اتصال ftp {0}: {1}"
                                     " فشل ، تخطي خطوة كاملة [process {2} من {3}]! الذهاب إلى الخطوة التالية",
            "input_target_error": "يجب أن يكون هدف الإدخال لوحدة {0} DOMAIN أو HTTP أو SINGLE_IPv4 ، مع تخطي {1}",
            "user_pass_found": "user: {0} pass: {1} host: {2} port: {3} found!",
            "file_listing_error": "(لا يوجد تصريح بإدخال الملفات)",
            "trying_message": "محاولة {0} من {1} في العملية {2} من {3} {4}: {5} ({6})",
            "smtp_connection_timeout": "اتصال smtp {0}: {1} مهلة ، تخطي {2}: {3}",
            "smtp_connection_failed": "اتصال SMTP بـ {0}: {1} فشل ، تخطي الخطوة"
                                      " بأكملها [process {2} of {3}]! الذهاب إلى الخطوة التالية",
            "ssh_connection_timeout": "اتصال ssh {0}: مهلة {1} ، تخطي {2}: {3}",
            "ssh_connection_failed": "اتصال ssh {0}: فشل {1} ، بتخطي"
                                     " الخطوة بأكملها [process {2} of {3}]! الذهاب إلى الخطوة التالية",
            "port/type": "{0} / {1}",
            "port_found": "المضيف: {0} المنفذ: {1} ({2}) تم العثور عليه!",
            "target_submitted": "الهدف {0} مقدم!",
            "current_version": "أنت تشغل إصدار OWASP Nettacker {0} {1} {2} {6} مع اسم الكود {3} {4} {5}",
            "feature_unavailable": "هذه الميزة غير متوفرة بعد! يرجى تشغيل "
                                   "\"بوابة استنساخ https://github.com/OWASP/Nettacker.git أ"
                                   "و نقطة تثبيت -U OWASP-Nettacker للحصول على الإصدار الأخير.",
            "available_graph": "بناء رسم بياني لجميع الأنشطة"
                               " والمعلومات ، يجب عليك استخدام مخرجات HTML. الرسوم البيانية المتاحة: {0}",
            "graph_output": "لاستخدام ميزة الرسم البياني يجب أن ينتهي اسم "
                            "ملف الإخراج الخاص بك بـ \".html\" أو \".htm\"!",
            "build_graph": "بناء الرسم البياني ...",
            "finish_build_graph": "الانتهاء من بناء الرسم البياني!",
            "pentest_graphs": "اختراق الرسومات البيانية",
            "graph_message": "هذا الرسم البياني التي تم إنشاؤها بواسطة OWASP Nettacker. يحتوي الرسم "
                             "البياني على جميع أنشطة الوحدات وخريطة الشبكة والمعلومات الحساسة "
                             "، يُرجى عدم مشاركة هذا الملف مع أي شخص إذا لم يكن موثوقًا.",
            "nettacker_report": "تقرير OWASP Nettacker",
            "nettacker_version_details": "تفاصيل البرنامج: إصدار OWASP Nettacker {0} [{1}] في {2}",
            "no_open_ports": "لا توجد منافذ مفتوحة!",
            "no_user_passwords": "لم يتم العثور على مستخدم / كلمة مرور!",
            "loaded_modules": "{0} تم تحميل الوحدات ...",
            "graph_module_404": "لم يتم العثور على وحدة الرسم البياني هذه: {0}",
            "graph_module_unavailable": "وحدة الرسم البياني هذه \"{0}\" غير متاحة",
            "ping_before_scan": "بينغ قبل مسح المضيف",
            "skipping_target": "تخطي الهدف بالكامل {0} وطريقة المسح "
                               "الضوئي {1} بسبب - إجراء الفحص قبل إجراء الفحص وفقط لم يستجب!",
            "not_last_version": "أنت لا تستخدم الإصدار الأخير من OWASP Nettacker ، يرجى تحديث.",
            "cannot_update": "لا يمكن التحقق من وجود تحديث ، يرجى التحقق من اتصال الإنترنت الخاص بك.",
            "last_version": "أنت تستخدم الإصدار الأخير من NWTWER OWASP ...",
            "directoy_listing": "تم العثور على قائمة الدليل في {0}",
            "insert_port_message": "الرجاء إدخال المنفذ عبر رمز التبديل -g أو --methods-args بدلاً من عنوان url",
            "http_connection_timeout": "اتصال http {0} timeout!",
            "wizard_mode": "بدء وضع المعالج",
            "directory_file_404": "لم يتم العثور على دليل أو ملف لـ {0} في المنفذ {1}",
            "open_error": "غير قادر على فتح {0}",
            "dir_scan_get": "يجب أن تكون قيمة dir_scan_http_method هي GET أو HEAD ، مع ضبط الإعداد الافتراضي على GET.",
            "list_methods": "قائمة جميع أساليب args",
            "module_args_error": "لا يمكن الحصول على {0} وحدة نمطية",
            "trying_process": "محاولة {0} من {1} في العملية {2} من {3} على {4} ({5})",
            "domain_found": "النطاق الموجود: {0}",
            "TIME": "زمن",
            "CATEGORY": "الفئة",
            "module_pattern_404": "لا يمكن العثور على أي وحدة نمطية بنمط {0}!",
            "enter_default": "يرجى إدخال {0} | الافتراضي [{1}]>",
            "enter_choices_default": "يرجى إدخال {0} | اختيارات [{1}] | الافتراضي [{2}]>",
            "all_targets": "الأهداف",
            "all_thread_numbers": "رقم الموضوع",
            "out_file": "اسم الملف الناتج",
            "all_scan_methods": "طرق الفحص",
            "all_scan_methods_exclude": "طرق المسح لاستبعادها",
            "all_usernames": "أسماء المستخدمين",
            "all_passwords": "كلمات المرور",
            "timeout_seconds": "ثواني المهلة",
            "all_ports": "أرقام المنافذ",
            "all_verbose_level": "المستوى المطول",
            "all_socks_proxy": "وكيل الجوارب",
            "retries_number": "رقم المحاولات",
            "graph": "رسم بياني",
            "subdomain_found": "تم العثور على نطاق فرعي: {0}",
            "select_profile": "حدد الملف الشخصي {0}",
            "profile_404": "الملف الشخصي \"{0}\" غير موجود!",
            "waiting": "بانتظار {0}",
            "vulnerable": "عرضة {0}",
            "target_vulnerable": "target {0}: {1} عرضة {2}!",
            "no_vulnerability_found": "لا يوجد الضعف! ({0})",
            "Method": "طريقة",
            "API": "API",
            "API_options": "خيارات واجهة برمجة التطبيقات",
            "start_API": "بدء خدمة API",
            "API_host": "عنوان مضيف واجهة برمجة التطبيقات",
            "API_port": "رقم منفذ واجهة برمجة التطبيقات",
            "API_debug": "وضع تصحيح API",
            "API_access_key": "مفتاح الوصول إلى واجهة برمجة التطبيقات",
            "white_list_API": "فقط اسمح لمضيفي القائمة البيضاء بالاتصال بواجهة برمجة التطبيقات",
            "define_whie_list": "تعريف مضيفي القائمة البيضاء ، مع فصل "
                                "، (أمثلة: 127.0.0.1 ، 192.168.0.1/24 ، 10.0.0.1-10.0.0.255)",
            "gen_API_access_log": "توليد سجل وصول API",
            "API_access_log_file": "سجل اسم الوصول إلى API",
            "API_port_int": "يجب أن يكون منفذ واجهة برمجة التطبيقات عددًا صحيحًا!",
            "unknown_ip_input": "نوع الإدخال غير المعروف ، الأنواع المقبولة هي SINGLE_IPv4 و RANGE_IPv4 و CIDR_IPv4",
            "API_key": "* مفتاح واجهة برمجة التطبيقات: {0}",
            "ports_int": "يجب أن تكون الموانئ صحيحة! (على سبيل المثال 80 | 80،1080 || 80،1080-1300،9000،12000-15000)",
            "through_API": "من خلال OWASP Nettacker API",
            "API_invalid": "مفتاح API غير صحيح",
            "unauthorized_IP": "IP الخاص بك غير مصرح به",
            "not_found": "غير معثور عليه!",
            "no_subdomain_found": "subdomain_scan: لم يتم تأسيس مجال فرعي!",
            "viewdns_domain_404": "viewdns_reverse_ip_lookup_scan: لم يتم العثور على نطاق!",
            "browser_session_valid": "جلسة متصفحك صالحة",
            "browser_session_killed": "جلسة المتصفح الخاص بك قتل",
            "updating_database": "تحديث قاعدة البيانات ...",
            "database_connect_fail": "لا يمكن الاتصال بقاعدة البيانات!",
            "inserting_report_db": "إدخال التقرير إلى قاعدة البيانات",
            "inserting_logs_db": "إدخال سجلات إلى قاعدة البيانات",
            "removing_logs_db": "إزالة السجلات القديمة من ديسيبل",
            "len_subdomain_found": "{0} تم العثور على نطاق فرعي (نطاقات)!",
            "len_domain_found": "{0} تم العثور على المجال (المجالات)!",
            "phpmyadmin_dir_404": "لم يتم العثور على أي phpmyadmin دير!",
            "DOS_send": "إرسال حزم DoS إلى {0}",
            "host_up": "{0} متروك! الوقت المستغرق لإعادة قراءة ping هو {1}",
            "host_down": "لا يمكن تنفيذ الأمر ping {0}!",
            "root_required": "هذا يحتاج إلى أن يعمل كجذر",
            "admin_scan_get": "يجب أن تكون قيمة admin_scan_http_method"
                              " هي GET أو HEAD ، مع ضبط الإعداد الافتراضي على GET.",
            "telnet_connection_timeout": "اتصال telnet {0}: {1} مهلة ، تخطي {2}: {3}",
            "telnet_connection_failed": "اتصال telnet إلى {0}: {1} فشل ، تخطي خطوة كاملة "
                                        "[process {2} من {3}]! الذهاب إلى الخطوة التالية",
            "http_auth_success": "نجاح المصادقة الأساسية لـ http - "
                                 "المضيف: {2}: {3} ، المستخدم: {0} ، اجتياز: {1} موجود!",
            "http_auth_failed": "فشل المصادقة الأساسية لـ http في {0}: {3} باستخدام {1}: {2}",
            "http_form_auth_success": "نجاح مصادقة نموذج http - المضيف: {2}: {3} ، المستخدم: {0} ، اجتياز: {1} موجود!",
            "http_form_auth_failed": "فشلت مصادقة نموذج http في {0}: {3} باستخدام {1}: {2}",
            "http_ntlm_success": "نجاح مصادقة http ntlm - المضيف: {2}: {3} ، المستخدم: {0} ، اجتياز: {1} موجود!",
            "http_ntlm_failed": "فشلت مصادقة http ntlm في {0}: {3} باستخدام {1}: {2}",
            "no_response": "لا يمكن الحصول على استجابة من الهدف",
            "category_framework": "الفئة: {0} ، وأطر العمل: {1} تم العثور عليها!",
            "nothing_found": "لم يتم العثور على شيء في {0} في {1}!",
            "no_auth": "لم يتم العثور على أي مصادقة في {0}: {1}"
        }
