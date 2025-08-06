# --- paradigm_name.py ---
# paradigm_name.py

class ProgrammingParadigm:
    """
    İnsan Dilinde ve Doğal Dilde Programlama Paradigmasını temsil eder.
    """

    def __init__(self):
        self._name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self._language = "Python"
        self._description = (
            "Bu paradigma, insanların doğal dilini temel alarak yazılım geliştirmeyi "
            "kolaylaştırmayı hedefler. Anlaşılabilirlik, erişilebilirlik ve sezgisellik ön plandadır."
        )

    def get_name(self):
        return self._name

    def get_language(self):
        return self._language

    def get_description(self):
        return self._description

    def __str__(self):
        return f"{self._name} [{self._language}]"

# Test amaçlı doğrudan çalıştırıldığında:
if __name__ == "__main__":
    paradigm = ProgrammingParadigm()
    print("Paradigma Adı :", paradigm.get_name())
    print("Programlama Dili :", paradigm.get_language())
    print("Tanım :", paradigm.get_description())

# --- natural_language_paradigm.py ---
# natural_language_paradigm.py

class NaturalLanguageProgrammingParadigm:
    """
    İnsan Dilinde ve Doğal Dilde Programlama Paradigması:
    İnsanların konuşma dillerini ve doğal iletişim biçimlerini kullanarak,
    kodlama yapmayı ve bilgisayarlarla insanlar gibi iletişim kurmayı sağlayan
    yenilikçi bir programlama yaklaşımıdır.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.language = "Python"
        self.core_idea = (
            "İnsanların konuştuğu doğal dillerle, insanlar gibi konuşarak "
            "ve iletişim kurarak kodlama yapılmasını sağlayan bir paradigmadır."
        )
        self.vision = (
            "Kod yazmayı teknik bir işlem olmaktan çıkarıp, herkesin konuşabildiği dilde "
            "düşünerek ve ifade ederek gerçekleştirebileceği bir hale getirmeyi amaçlar."
        )
        self.communication_style = "İnsan gibi, doğal cümlelerle, anlam odaklı iletişim"

    def introduce(self):
        intro = (
            f"Paradigma Adı: {self.name}\n"
            f"Kullanılan Temel Dil: {self.language}\n\n"
            f"Temel Fikir:\n{self.core_idea}\n\n"
            f"Vizyon:\n{self.vision}\n\n"
            f"İletişim Tarzı:\n{self.communication_style}"
        )
        return intro

# Bu modül doğrudan çalıştırıldığında tanıtım yapılır
if __name__ == "__main__":
    paradigm = NaturalLanguageProgrammingParadigm()
    print(paradigm.introduce())

# --- universal_paradigm.py ---
# universal_paradigm.py

class UniversalProgrammingParadigm:
    """
    İnsan Dilinde ve Doğal Dilde Programlama Paradigması:
    Evrensel olarak kullanılabilen, doğal dilleri temel alarak herkesin
    program yazabilmesini hedefleyen yeni nesil bir yazılım geliştirme yaklaşımıdır.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.language = "Python"
        self.is_universal = True
        self.reason_for_universality = (
            "Bu paradigma, insanların konuştuğu tüm doğal dilleri kapsayabilir; "
            "bu da onu evrensel hale getirir. Teknik bilgiye ihtiyaç duymadan, "
            "dünyadaki herkesin kendi diliyle kod yazabilmesini sağlar."
        )

    def describe_universality(self):
        if self.is_universal:
            return (
                f"'{self.name}' adlı programlama paradigması evrensel bir paradigmadır.\n\n"
                f"Neden Evrensel?\n{self.reason_for_universality}"
            )
        else:
            return f"'{self.name}' henüz evrensel değildir."

# Bu modül doğrudan çalıştırıldığında bilgi verir
if __name__ == "__main__":
    paradigm = UniversalProgrammingParadigm()
    print(paradigm.describe_universality())

# --- multilingual_support.py ---
# multilingual_support.py

class MultilingualProgrammingParadigm:
    """
    İnsan Dilinde ve Doğal Dilde Programlama Paradigması:
    Kullanıcıların kendi ana dillerini ya da konuşulan başka dilleri kullanarak
    programlama ve kodlama yapabilmelerini mümkün kılar.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.supported_languages = [
            "Türkçe",
            "İngilizce",
            "İspanyolca",
            "Fransızca",
            "Arapça",
            "Çince",
            "Rusça",
            "Japonca",
            "Almanca",
            "Hintçe",
            "Abazaca",
            "Abhazca",
            "Açece",
            "Açice",
            "Adigece",
            "Afarca",
            "Afrikaanca",
            "Ahtnaca",
            "Eynuca",
            "Aivilik İnuitçesi",
            "Akanca",
            "Akatekçe",
            "Alabamaca",
            "Algonkince",
            "Altayca",
            "Alur Dili",
            "Amharca",
            "Anişininice",
            "Apsalokece",
            "Aragonca",
            "Aramice",
            "Aranca",
            "Arapahoca",
            "Arayanice",
            "Arbereşçe",
            "Arikaraca",
            "Arnavutça",
            "Arviligjuaq İnuitçesi",
            "Assamca",
            "Asturyasça",
            "Aşağı Tananaca",
            "Atikamekçe",
            "Atsinaca",
            "Auvergnat Dili",
            "Avakatekçe",
            "Avarca",
            "Awadhi Dili",
            "Aymaraca",
            "Aynuca",
            "Azerice",
            "Balice",
            "Bambara Dili",
            "Baoulé Dili",
            "Baskça",
            "Başkurtça",
            "Batak Karo Dili",
            "Batak Simalungun Dili",
            "Batak Toba Dili",
            "Bataklık Kricesi",
            "Batı Apaçicesi",
            "Batı Kanada İnuitçesi",
            "Bengalce",
            "Berberice",
            "Bretonca",
            "Beyaz Rusça",
            "Boşnakça",
            "Bulgarca",
            "Burgonyaca",
            "Burmaca",
            "Buryatça",
            "Cavaca",
            "Champenois",
            "Çalçitekçe",
            "Çeçence",
            "Çekçe",
            "Çerokice",
            "Çevaca",
            "Chamorro dili",
            "Chuukece",
            "Çilkotince",
            "Çingenece",
            "Çortice",
            "Çuhça",
            "Çukçice",
            "Çupikçe",
            "Çulımca",
            "Çuvaşça",
            "Dakotaca",
            "Dakelce",
            "Danca",
            "Danezaca",
            "Dargince",
            "Darice",
            "Dauphinois",
            "Değinakça",
            "Denağinaca",
            "Denesulinece",
            "Denetaca",
            "Dinka Dili",
            "Dogri Dİli",
            "Doğu Kanada İnuitçesi",
            "Donşianca",
            "Dzongka",
            "Endonezce",
            "Ermenice",
            "Eski İngilizce",
            "Eski Nors Dili",
            "Esperanto",
            "Estonca",
            "Evenki Dili",
            "Eyakça",
            "Farsça",
            "Faroece",
            "Felemenkçe",
            "Filipince",
            "Frizce",
            "Fince",
            "Gagavuzca",
            "Galce",
            "Galiçyaca",
            "Gaskonca",
            "Gilanice",
            "Goranice",
            "Grönlandca",
            "Guaranice",
            "Guçince",
            "Güney Pikence",
            "Güney Tuçoncası",
            "Gürcüce",
            "Hakaltekçe",
            "Hakasça",
            "Hakka",
            "Halaçça",
            "Halkomelemce",
            "Hanca",
            "Hantıca",
            "Hausa",
            "Haydaca",
            "Hereroca",
            "Hırvatça",
            "Hidatsaca",
            "Hikarilaca",
            "Hintçe",
            "Hokankça",
            "Holikaçukça",
            "Hupaca",
            "İbranice",
            "İrlandaca",
            "İnguşça",
            "İnnuca",
            "İnuinnaq İnuitçesi",
            "İnyupikçe",
            "İskoçça",
            "İsveççe",
            "İşilce",
            "İtalyanca",
            "İtzaca",
            "İzlandaca",
            "Kabardeyce",
            "Kakçikelce",
            "Kalabriyaca",
            "Kalmıkça",
            "Kangiryuarmiut İnuitçesi",
            "Kanhobalca",
            "Kannadaca",
            "Kantonca",
            "Kanuri Dili",
            "Karaayakça",
            "Karakalpakça",
            "Karankavaca",
            "Kaskaca",
            "Kaşgayca",
            "Katalanca",
            "Kazakça",
            "Keçuvaca",
            "Kekçice",
            "Kernevekçe",
            "Khmerce",
            "Kırgızca",
            "Kırımca",
            "Kırımçakça",
            "Kiçece",
            "Kivalliq İnuitçesi",
            "Komoksça",
            "Komorca",
            "Kongoca",
            "Korece",
            "Korsikaca",
            "Koryakça",
            "Koyukonca",
            "Krice",
            "Kuzey Tuçoncası",
            "Kürtçe",
            "Kwalhioqua–Tlatskanai dili",
            "Ladino",
            "Lakça",
            "Lakotaca",
            "Latince",
            "Laponca",
            "Lazca",
            "Lehçe",
            "Letonca",
            "Leonca",
            "Lezgice",
            "Limburgca",
            "Limousin dili",
            "Lipanca",
            "Litvanca",
            "Lombardça",
            "Lorrain Dili",
            "Lorraine Frankçası",
            "Lüksemburgca",
            "Macarca",
            "Malayca",
            "Maltaca",
            "Maldivce",
            "Makedonca",
            "Mamca",
            "Manca",
            "Mançuca",
            "Mandanca",
            "Mandarin",
            "Mansice",
            "Maorice",
            "Mapudungun",
            "Marathice",
            "Mari Dİli",
            "Mayaca",
            "Megrelce",
            "Meskalero-Çirikavaca",
            "Meskvakice",
            "Mikasukice",
            "Miranda Dili",
            "Moğolca",
            "Moldovca",
            "Mopanca",
            "Nadoten-Vetsuvetence",
            "Nakodaca",
            "Nakotaca",
            "Napolice",
            "Naskapice",
            "Natsilik İnuitçesi",
            "Nattilik İnuitçesi",
            "Naukan Yupikçesi",
            "Navahoca",
            "Nikolaca",
            "Nissart dili",
            "Nlakapamukça",
            "Normanca",
            "Norveççe",
            "Nuhalkça",
            "Nunatsiavut İnuitçesi",
            "Nunavik İnuitçesi",
            "Nunivak Çupikçesi",
            "Oksitanca",
            "Orman Kricesi",
            "Osetçe",
            "Ova Apaçicesi",
            "Ova Kricesi",
            "Özbekçe",
            "Pali Dili",
            "Papiamento",
            "Pavnice",
            "Peçenekçe",
            "Pencapça",
            "Peştuca",
            "Pikartça",
            "Piraha Dili",
            "Pokomamca",
            "Pontus Rumcası",
            "Portekizce",
            "Potavatomice",
            "Provensal",
            "Qikiqtaaluk İnuitçesi",
            "Romanşça",
            "Ruandaca",
            "Rumence",
            "Saho Dili",
            "Sahtuca",
            "Sakapultekçe",
            "Salarca",
            "Sanskritçe",
            "Sarı Yugurca",
            "Sekanice",
            "Sırpça",
            "Sibirya Yupikçesi",
            "Sicilyaca",
            "Siglit İnuitçesi",
            "Sipakapaca",
            "Sirenik Yupikçesi",
            "Siyuca",
            "Slovakça",
            "Slovence",
            "Sorbca",
            "Soranice",
            "Supikçe",
            "Svahili Dili",
            "Svanca",
            "Süryanice",
            "Sivandi",
            "Şavnice",
            "Şayence",
            "Şorca",
            "Tacikçe",
            "Tahitice",
            "Tagalogca",
            "Tagişçe",
            "Tahltanca",
            "Tamilce",
            "Tanakrosça",
            "Tatarca",
            "Tatça",
            "Tayca",
            "Tayvanca",
            "Tektitekçe",
            "Teluguca",
            "Tetum Dili",
            "Tibetçe",
            "Tigrinya Dili",
            "Tiv Dili",
            "Tlınçonca",
            "Tlingitçe",
            "Tok Pisin Dili",
            "Tongaca",
            "Tsetsautça",
            "Tshiluba",
            "Tsutinaca",
            "Tsvana Dili",
            "Tupi Dili",
            "Tuvaca",
            "Türkmence",
            "Twi Dili",
            "Tzutuhilce",
            "Udmurtça",
            "Ukraynaca",
            "Ulahça",
            "Urduca",
            "Uspantekçe",
            "Utkuhiksalik İnuitçesi",
            "Uygurca",
            "Valensiyaca",
            "Vapoca",
            "Venedikçe",
            "Vietnamca",
            "Yakutça",
            "Yidiş",
            "Yukarı Kuskokvimce",
            "Yukarı Tananaca",
            "Yukatek Mayacası",
            "Yukice",
            "Yunanca",
            "Yupikçe",
            "Zazaca",
            "Zhuangca",
            "Zuluca",
            "Zunice",
            "Ndombe Dili",
            "Dyula Dili",
            "Ewece",
            "Fijice",
            "Fon Dili",
            "Fula Dili",
            "Furlanca",
            "Gaa Dili",
            "Guaranice",
            "Güceratça",
            "Habeşçe",
            "Haiti Kreolü",
            "Hakha Chin Dili",
            "Hawai Dili",
            "Hiligaynon Dili",
            "Hmong Dili",
            "Xhosa Dili",
            "Hunsrik Dili",
            "İlocano Dili",
            "İban Dilleri",
            "İgbo Dili",
            "Jingpo Dili",
            "Kamboçyaca",
            "Khasi Dili",
            "Kiga Dili",
            "Kituba Dili",
            "Kokborok Dili",
            "Komice",
            "Kongoca",
            "Konkani Dili",
            "Krio Dili",
            "Laoca",
            "Latgalce",
            "Ligurca",
            "Lingala Dili",
            "Luganda Dili",
            "Luo Dili",
            "Madurese Dili",
            "Maithili Dili",
            "Makassar Dili",
            "Malayalamca",
            "Malgaşça",
            "Manksça",
            "Marshall Adaları Dili",
            "Marwadi Dili",
            "Meitei Dili",
            "Minangkabau Dili",
            "Mizo Dili",
            "Morisyen",
            "Nahuatl",
            "Ndau Lehçesi",
            "Güney Ndebele Dili",
            "Nepalce",
            "N’Ko Dili",
            "Nuer Dili",
            "Oriya Dili",
            "Oksitanca",
            "Oromo Dili",
            "Ova Marice",
            "Pangasinan Dili",
            "Rundice",
            "Sabuanca",
            "Samoaca",
            "Sango Dili",
            "Santalice",
            "Kuzey Sotho Dili",
            "Güney Sotho Dili",
            "Seylanca",
            "Şeyseller Kreolü",
            "Shan Dili",
            "Şona Dili",
            "Silezyaca",
            "Somalice",
            "Sunda Dili",
            "Susu Dili",
            "Swati Dili",
            "Tsongaca",
            "Tsvana Dili",
            "Tuluca",
            "Tumbuka Dili",
            "Varayca",
            "Karayca",
            "Venda Dili",
            "Volofça",
            "Yorubaca",
            "Yucatek Mayaca",
            "Zapotek Dili",
            
        ]
        self.description = (
            "Bu paradigma, kullanıcıların hem kendi ana dillerinde hem de "
            "başka doğal dillerde programlama yapmalarını mümkün kılar. "
            "Kodlama süreci, teknik değil; dilsel ve sezgisel bir iletişim temeline dayanır."
        )

    def list_supported_languages(self):
        return ", ".join(self.supported_languages)

    def explain_multilingual_support(self):
        return (
            f"'{self.name}' paradigması çok dilli destek sunar.\n\n"
            f"Açıklama:\n{self.description}\n\n"
            f"Desteklenen Diller:\n{self.list_supported_languages()}"
        )

# Bu modül çalıştırıldığında bilgi verir
if __name__ == "__main__":
    paradigm = MultilingualProgrammingParadigm()
    print(paradigm.explain_multilingual_support())

# --- global_language_support.py ---
# global_language_support.py

class GlobalLanguageSupportParadigm:
    """
    İnsan Dilinde ve Doğal Dilde Programlama Paradigması:
    Tüm dünya dillerini ve yazı karakterlerini destekleyen evrensel bir kodlama anlayışı sunar.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.supports_all_languages = True
        self.supports_all_scripts = True
        self.languages_description = (
            "Bu paradigma, dünya çapında konuşulan tüm doğal dilleri destekler. "
            "Türkçe, İngilizce, Arapça, Çince, Japonca, Rusça, Fransızca, İspanyolca, "
            "Hintçe, Korece ve daha fazlası dahil olmak üzere hiçbir dil dışlanmaz."
        )
        self.scripts_description = (
            "Latin, Arap, Kiril, Han (Çin), Kana (Japon), Devanagari, Hangul, "
            "Yunanca, İbranice, Tay, Gürcü, Ermeni ve diğer tüm yazı sistemleriyle "
            "tam uyumludur."
        )

    def describe_global_support(self):
        if self.supports_all_languages and self.supports_all_scripts:
            return (
                f"'{self.name}' adlı programlama paradigması, dünya çapında konuşulan TÜM dilleri "
                f"ve yazı karakterlerini DESTEKLEMEKTEDİR.\n\n"
                f"Dil Desteği:\n{self.languages_description}\n\n"
                f"Yazı Karakteri / Alfabe Desteği:\n{self.scripts_description}"
            )
        else:
            return (
                f"'{self.name}' sınırlı dil veya karakter desteğine sahiptir. Evrensel değildir."
            )

# Modül doğrudan çalıştırıldığında
if __name__ == "__main__":
    paradigm = GlobalLanguageSupportParadigm()
    print(paradigm.describe_global_support())

# --- supported_characters.py ---
# supported_characters.py

class SupportedCharacterSets:
    """
    İnsan Dilinde ve Doğal Dilde Programlama Paradigması:
    Harf, sayı, özel ve Türkçe karakterleri destekler.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.letter_characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        self.digit_characters = list("0123456789")
        self.special_characters = list("!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~")
        self.turkish_characters = list("çÇğĞıİöÖşŞüÜ")

    def describe_supported_characters(self):
        return (
            f"'{self.name}' adlı programlama paradigmasında desteklenen yazı karakterlerine örnekler:\n\n"
            f"🔤 Harf Karakterleri:\n{''.join(self.letter_characters)}\n\n"
            f"🔢 Sayı Karakterleri:\n{''.join(self.digit_characters)}\n\n"
            f"✳️ Özel Karakterler:\n{''.join(self.special_characters)}\n\n"
            f"🇹🇷 Türkçe Karakterler:\n{''.join(self.turkish_characters)}"
        )

# Kod doğrudan çalıştırıldığında bilgi verir
if __name__ == "__main__":
    charset = SupportedCharacterSets()
    print(charset.describe_supported_characters())

# --- punctuation_support.py ---
# punctuation_support.py

import string

class PunctuationSupportParadigm:
    """
    Bu sınıf, İnsan Dilinde ve Doğal Dilde Programlama adlı paradigmanın
    tüm noktalama işaretlerini desteklediğini gösterir.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.supported_punctuation = list(string.punctuation)
        self.additional_punctuation = ['…', '–', '—', '“', '”', '‘', '’', '«', '»', '·', '¡', '¿']
        self.full_punctuation_set = self.supported_punctuation + self.additional_punctuation

    def describe_punctuation_support(self):
        return (
            f"'{self.name}' adlı programlama paradigması, yazılı iletişimde kullanılan tüm "
            f"noktalama işaretlerini desteklemektedir.\n\n"
            f"📍 Temel Noktalama İşaretleri:\n{''.join(self.supported_punctuation)}\n\n"
            f"📝 Ekstra Noktalama İşaretleri (Unicode dahil):\n{''.join(self.additional_punctuation)}\n\n"
            f"✅ Toplam Desteklenen Noktalama Sayısı: {len(self.full_punctuation_set)}"
        )

# Bu modül doğrudan çalıştırıldığında açıklamayı yapar
if __name__ == "__main__":
    paradigm = PunctuationSupportParadigm()
    print(paradigm.describe_punctuation_support())

# --- sentence_rule_checker.py ---
# sentence_rule_checker.py

class NaturalLanguageProgramming:
    """
    İnsan Dilinde ve Doğal Dilde Programlama adlı bu paradigma,
    yazılan her kodlama cümlesinin sonunda nokta işareti (.) olmasını zorunlu kılar.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.required_end_symbol = "."

    def check_sentence(self, sentence: str) -> bool:
        """
        Cümlenin sonunda nokta olup olmadığını kontrol eder.
        """
        return sentence.strip().endswith(self.required_end_symbol)

    def explain_rule(self):
        return (
            f"'{self.name}' adlı programlama paradigmasında programlama ve kodlama yaparken "
            f"her cümlenin sonunda mutlaka nokta (.) olmalıdır."
        )

# Bu kısım modül doğrudan çalıştırıldığında çalışır
if __name__ == "__main__":
    paradigm = NaturalLanguageProgramming()
    
    print(paradigm.explain_rule())
    print("\nÖrnek Kontroller:\n")

    ornek_cumleler = [
        "Ekrana merhaba yaz.",
        "Dosyayı kaydet.",
        "Kullanıcıdan sayı al.",
        "Toplamı hesapla."
    ]

    for cumle in ornek_cumleler:
        uygun = paradigm.check_sentence(cumle)
        durum = "✅ Uygun" if uygun else "❌ Hatalı"
        print(f"Cümle: \"{cumle}\" → {durum}")

# --- strict_sentence_validator.py ---
# strict_sentence_validator.py

class SentenceTerminationError(Exception):
    """
    Cümle sonuna nokta konulmadığında fırlatılacak özel hata türü.
    """
    def __init__(self, message="Cümle sonuna nokta (.) eklenmemiş. Bu, kabul edilemez bir hatadır!"):
        super().__init__(message)

class NaturalLanguageProgrammingStrict:
    """
    İnsan Dilinde ve Doğal Dilde Programlama adlı paradigmanın
    nokta işareti zorunluluğunu katı bir şekilde denetleyen sınıf.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.required_end_symbol = "."

    def validate_sentence(self, sentence: str):
        """
        Cümleyi kontrol eder. Nokta ile bitmiyorsa hata fırlatır.
        """
        if not sentence.strip().endswith(self.required_end_symbol):
            raise SentenceTerminationError()

    def explain_rule(self):
        return (
            f"'{self.name}' paradigmasında her doğal dil komutu nokta (.) ile bitmelidir.\n"
            f"Eğer bitmezse, sistem bunu asla kabul etmez, anında reddeder ve hata verir."
        )

# Ana çalışma bölümü
if __name__ == "__main__":
    paradigm = NaturalLanguageProgrammingStrict()
    print(paradigm.explain_rule())
    print("\nÖrnek Kontroller:\n")

    example_sentences = [
        "Ekrana merhaba yaz.",
        "Dosyayı kaydet.",
        "Kullanıcıdan isim al.",
        "Veriyi işle."
    ]

    for sentence in example_sentences:
        print(f"👉 Cümle: \"{sentence}\"")
        try:
            paradigm.validate_sentence(sentence)
            print("✅ Geçerli cümle.\n")
        except SentenceTerminationError as e:
            print(f"❌ Hata: {e}\n")

# --- multi_verb_sentence_checker.py ---
# multi_verb_sentence_checker.py

class MultiVerbTerminationError(Exception):
    """
    Birden fazla fiil içeren cümlelerde her fiilden sonra nokta yoksa fırlatılacak hata.
    """
    def __init__(self, message="Tüm yüklemlerden (fiillerden) sonra nokta (.) eklenmelidir!"):
        super().__init__(message)

class HumanNaturalLanguageProgramming:
    """
    İnsan Dilinde ve Doğal Dilde Programlama Paradigması
    Nokta işareti çoklu fiillerde de zorunludur.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.verb_list = {"aç", "oku", "yaz", "kaydet", "gönder", "al", "güncelle", "sil"}

    def validate_multiple_verbs(self, text: str):
        """
        Tüm yüklemlerden sonra nokta olup olmadığını kontrol eder.
        """
        clauses = [clause.strip() for clause in text.split('.') if clause.strip()]

        for clause in clauses:
            last_word = clause.split()[-1].lower()
            if last_word in self.verb_list:
                # Bu fiilden sonra nokta yoksa hata ver
                full_clause = clause + "."
                if not text.__contains__(full_clause):
                    raise MultiVerbTerminationError(f"'{last_word}' fiilinden sonra nokta eksik.")

    def explain_rule(self):
        return (
            f"{self.name} adlı bu programlama paradigmasında sadece programın sonunda değil, "
            "birden fazla yüklem (fiil) varsa her birinin ardından da nokta (.) konulmalıdır.\n"
            "Her fiil tam bir işlem ifadesi olarak değerlendirilir."
        )

# Test ve örnek kullanım
if __name__ == "__main__":
    paradigm = HumanNaturalLanguageProgramming()
    print(paradigm.explain_rule())
    print("\nÖrnek Kontroller:\n")

    test_sentences = [
        "Dosyayı aç. Oku. Yaz. Kaydet.",   # ✅ doğru
        "Dosyayı aç, oku, yaz ve kaydet.",  # ❌ hatalı
        "Veriyi al. Güncelle. Gönder.",    # ✅ doğru
        "Veriyi al güncelle gönder."        # ❌ hatalı
    ]

    for s in test_sentences:
        print(f"👉 Cümle: \"{s}\"")
        try:
            paradigm.validate_multiple_verbs(s)
            print("✅ Geçerli cümle.\n")
        except MultiVerbTerminationError as e:
            print(f"❌ Hata: {e}\n")

# --- subject_capitilization.py ---
class SubjectCapitalizationError(Exception):
    """Özne baş harfi büyük değilse fırlatılan özel hata."""
    def __init__(self, message="Cümleye başlarken öznenin ilk harfi mutlaka büyük olmalıdır!"):
        super().__init__(message)

class HumanNaturalLanguageProgramming:
    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"

    def validate_subject_capitalization(self, sentence: str):
        """
        Cümlenin ilk kelimesinin ilk harfinin büyük olup olmadığını kontrol eder.
        """
        sentence = sentence.strip()
        if not sentence:
            raise ValueError("Boş cümle girdiniz!")

        first_word = sentence.split()[0]
        first_char = first_word[0]

        if not first_char.isupper():
            raise SubjectCapitalizationError()

    def explain_rule(self):
        return (
            f"'{self.name}' paradigmasında cümleye başlarken öznenin ilk harfi mutlaka büyük olmalıdır."
        )

if __name__ == "__main__":
    paradigm = HumanNaturalLanguageProgramming()
    print(paradigm.explain_rule())
    print()

    examples = [
        "Ali okula gitti.",
        "Ali eve döndü.",
        "Deniz kitap okuyor.",
        "Deniz yüzme öğreniyor."
    ]

    for sentence in examples:
        print(f"Cümle: \"{sentence}\"")
        try:
            paradigm.validate_subject_capitalization(sentence)
            print("✅ Geçerli cümle.\n")
        except SubjectCapitalizationError as e:
            print(f"❌ Hata: {e}\n")

# --- caps_lock_buyuk_kucuk.py ---
class CaseInsensitiveParadigm:
    """
    İnsan Dilinde ve Doğal Dilde Programlama paradigması,
    büyük/küçük harf ayrımı yapmaz.
    Caps Lock açık/kapalı fark etmez.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"

    def normalize_text(self, text: str) -> str:
        """
        Girilen metni tamamen küçük harfe çevirir,
        böylece büyük/küçük harf ayrımı ortadan kalkar.
        """
        return text.lower()

    def compare_statements(self, stmt1: str, stmt2: str) -> bool:
        """
        İki cümlenin büyük/küçük harf farkı olmadan eşit olup olmadığını kontrol eder.
        """
        return self.normalize_text(stmt1) == self.normalize_text(stmt2)

    def explain_advantage(self):
        return (
            f"{self.name} paradigmasının en büyük avantajı:\n"
            "Büyük harf ile küçük harf ayrımı yapılmaz.\n"
            "Caps Lock tuşunun açık veya kapalı olması hiç fark etmez."
        )


# Örnek kullanım
if __name__ == "__main__":
    paradigm = CaseInsensitiveParadigm()
    print(paradigm.explain_advantage())
    print()

    example_1 = "Dosyayı aç."
    example_2 = "dosyayı AÇ."
    example_3 = "DOSYAYI aç."

    print(f"Örnek 1: \"{example_1}\"")
    print(f"Örnek 2: \"{example_2}\"")
    print(f"Örnek 3: \"{example_3}\"")
    print()

    print("Örnek 1 ve Örnek 2 eşit mi?", paradigm.compare_statements(example_1, example_2))
    print("Örnek 1 ve Örnek 3 eşit mi?", paradigm.compare_statements(example_1, example_3))

# --- basit_cumle.py ---
class SentenceStructureError(Exception):
    """Cümle türü veya yüklem eksikse fırlatılan özel hata."""
    def __init__(self, message):
        super().__init__(message)

class HumanNaturalLanguageProgramming:
    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        # Örnek olarak kabul ettiğimiz cümle türleri
        self.allowed_sentence_types = [
            "basit", "bağlı", "birleşik", "emir", "koşullu", "sıralı", "kurallı"
        ]
    
    def explain_rule(self):
        return (
            f"{self.name} paradigmasında yazılan cümleler;\n"
            "- Basit cümle\n"
            "- Bağlı cümle\n"
            "- Birleşik cümle\n"
            "- Emir cümlesi\n"
            "- Koşullu cümle\n"
            "- Sıralı cümle\n"
            "- Kurallı cümle (düz cümle)\n"
            "olmalıdır ve mutlaka cümlelerde fiil (yüklem) bulunmalıdır."
        )
    
    def check_sentence_type(self, sentence_type: str):
        """
        Cümle türünün uygun olup olmadığını kontrol eder.
        """
        if sentence_type.lower() not in self.allowed_sentence_types:
            raise SentenceStructureError(
                f"Cümle türü '{sentence_type}' geçerli değil. "
                f"Geçerli türler: {', '.join(self.allowed_sentence_types)}"
            )
    
    def check_verb_presence(self, sentence: str):
        """
        Basit bir fiil kontrolü yapar (burada örnek olarak sadece bazı fiiller aranıyor).
        Gerçek projede doğal dil işleme (NLP) kütüphaneleri kullanılabilir.
        """
        # Örnek fiil listesi (çoğunlukla Türkçe fiiller)
        verbs = ["git", "gel", "yaz", "oku", "koş", "konuş", "bak", "al", "ver", "çalış"]
        sentence_lower = sentence.lower()
        for verb in verbs:
            if verb in sentence_lower:
                return True
        raise SentenceStructureError("Cümlede fiil (yüklem) bulunmamaktadır!")

if __name__ == "__main__":
    paradigm = HumanNaturalLanguageProgramming()
    print(paradigm.explain_rule())
    print()

    # Test örnekleri
    try:
        sentence_type = "emir"
        sentence = "Lütfen kitabı oku."
        paradigm.check_sentence_type(sentence_type)
        paradigm.check_verb_presence(sentence)
        print(f"'{sentence}' cümlesi geçerlidir.\n")
    except SentenceStructureError as e:
        print(f"Hata: {e}\n")

    try:
        sentence_type = "soru"
        sentence = "Kitap masada mı?"
        paradigm.check_sentence_type(sentence_type)
        paradigm.check_verb_presence(sentence)
        print(f"'{sentence}' cümlesi geçerlidir.\n")
    except SentenceStructureError as e:
        print(f"Hata: {e}\n")

    try:
        sentence_type = "basit"
        sentence = "Bugün hava çok güzel."
        paradigm.check_sentence_type(sentence_type)
        paradigm.check_verb_presence(sentence)
        print(f"'{sentence}' cümlesi geçerlidir.\n")
    except SentenceStructureError as e:
        print(f"Hata: {e}\n")

# --- eksiltili_devrik_cumle.py ---
class SentenceValidationError(Exception):
    """Cümle yapısı veya yüklem hatası durumunda fırlatılan özel hata."""
    def __init__(self, message):
        super().__init__(message)

class HumanNaturalLanguageProgramming:
    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
    
    def explain_rules(self):
        return (
            f"{self.name} paradigmasında:\n"
            "- Eksiltili cümleler kabul edilmez.\n"
            "- Devrik cümleler kabul edilmez.\n"
            "- Cümlede mutlaka fiil (yüklem) bulunmalıdır.\n"
            "Aksi halde kesinlikle reddedilir ve hata verir."
        )
    
    def is_ellipsis_sentence(self, sentence: str) -> bool:
        """
        Basit kontrol: Eksiltili cümlelerde genellikle yüklem veya önemli öğe eksiktir.
        Burada örnek olarak '...' içeren veya eksik tamamlanmış cümleler algılanır.
        """
        return "..." in sentence or sentence.strip().endswith(",")

    def is_inverted_sentence(self, sentence: str) -> bool:
        """
        Devrik cümle kontrolü için basit örnek:
        - Türkçede devrik cümleler çoğunlukla yüklemi sonda değil başta olmayan cümlelerdir.
        Burada örnek olarak fiilin cümlenin başında olup olmadığını kontrol ediyoruz.
        """
        words = sentence.lower().strip().split()
        # Örnek bazı fiiller (çok basit)
        verbs = {"git", "gel", "yaz", "oku", "koş", "konuş", "bak", "al", "ver", "çalış"}
        if not words:
            return True  # Boş cümle devrik kabul edilebilir.
        # Eğer cümlede fiil varsa ve ilk kelime fiil değilse devrik kabul et
        first_word_is_verb = words[0] in verbs
        contains_verb = any(word in verbs for word in words)
        if contains_verb and not first_word_is_verb:
            return True
        return False

    def contains_verb(self, sentence: str) -> bool:
        """
        Basit fiil kontrolü, örnek fiiller listesi ile arama yapılıyor.
        """
        verbs = ["git", "gel", "yaz", "oku", "koş", "konuş", "bak", "al", "ver", "çalış"]
        sentence_lower = sentence.lower()
        return any(verb in sentence_lower for verb in verbs)

    def validate_sentence(self, sentence: str):
        if self.is_ellipsis_sentence(sentence):
            raise SentenceValidationError("Eksiltili cümleler kesinlikle kabul edilmez!")
        if self.is_inverted_sentence(sentence):
            raise SentenceValidationError("Devrik cümleler kesinlikle kabul edilmez!")
        if not self.contains_verb(sentence):
            raise SentenceValidationError("Cümlede fiil (yüklem) mutlaka bulunmalıdır!")
        return "Cümle geçerlidir."

if __name__ == "__main__":
    paradigm = HumanNaturalLanguageProgramming()
    print(paradigm.explain_rules())
    print()

    test_sentences = [
        "Kitap oku.",          # Geçerli
        "Oku kitap.",          # Devrik cümle, hata
        "Kitap...",            # Eksiltili cümle, hata
        "Bu güzel kitap",      # Fiil yok, hata
        "Git hemen oraya.",    # Geçerli
    ]

    for sentence in test_sentences:
        print(f"Cümle: \"{sentence}\"")
        try:
            result = paradigm.validate_sentence(sentence)
            print("Sonuç:", result)
        except SentenceValidationError as e:
            print("Hata:", e)
        print()

# --- explain_programming_styles.py ---
class HumanNaturalLanguageProgramming:
    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
    
    def explain_programming_styles(self):
        return (
            f"{self.name} paradigmasında:\n"
            "- Hem düz cümle yazarak programlama ve kodlama yapmak mümkündür.\n"
            "- Hem de maddeler hâlinde, liste şeklinde ifadeler kullanarak programlama ve kodlama yapmak mümkündür.\n"
            "Yani kullanıcılar doğal dilde hem normal cümleler hem de sıralı maddeler şeklinde kod yazabilirler."
        )

    def run(self):
        print(self.explain_programming_styles())

if __name__ == "__main__":
    paradigm = HumanNaturalLanguageProgramming()
    paradigm.run()

# --- alphabet.py ---
class HumanNaturalLanguageProgramming:
    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"

    def support_all_alphabets(self):
        return (
            f"{self.name} paradigması, dünya üzerindeki bütün tüm alfabeleri desteklemektedir.\n"
            "Bu sayede kullanıcılar, Latin alfabesi, Kiril, Arap, Çince, Hintçe ve daha birçok farklı alfabe ile\n"
            "programlama ve kodlama yapabilmektedirler."
        )

if __name__ == "__main__":
    paradigm = HumanNaturalLanguageProgramming()
    print(paradigm.support_all_alphabets())

# --- dil_ailesi.py ---
class HumanNaturalLanguageProgramming:
    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"

    def support_all_language_families(self):
        return (
            f"{self.name} paradigması, dünya çapındaki bütün tüm dil ailelerini desteklemektedir.\n"
            "Kullanıcılar, Hint-Avrupa, Ural, Afro-Asyatik, Sino-Tibet, Türk dilleri ve diğer tüm dil ailelerinden\n"
            "kendilerine uygun dillerle programlama yapabilmektedirler."
        )

if __name__ == "__main__":
    paradigm = HumanNaturalLanguageProgramming()
    print(paradigm.support_all_language_families())


# --- global_official.py ---
class HumanNaturalLanguageProgramming:
    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"

    def global_and_official_use(self):
        return (
            f"{self.name} paradigması, dünya üzerindeki bütün tüm ülkelerde ve bölgelerde yaygın olarak kullanılmaktadır.\n"
            "Hatta bazı ülkelerde resmi programlama paradigması olarak kabul edilmiştir.\n"
            "Bu sayede evrensel bir programlama dili ve yaklaşımı olma özelliğini taşımaktadır."
        )

if __name__ == "__main__":
    paradigm = HumanNaturalLanguageProgramming()
    print(paradigm.global_and_official_use())


# --- EKLENEN KURAL: Noktadan Sonra Büyük Harf ---

class PostPeriodCapitalizationError(Exception):
    """Noktadan sonra başlayan cümlede ilk harf küçükse fırlatılan hata."""
    def __init__(self, message="Noktadan sonra gelen cümlede ilk kelimenin baş harfi büyük olmalıdır!"):
        super().__init__(message)

class PostPeriodCapitalizationValidator:
    """
    İnsan Dilinde ve Doğal Dilde Programlama Paradigması:
    Nokta (.) ile biten bir cümleden sonra gelen yeni cümlede
    ilk kelimenin baş harfi mutlaka büyük harfle başlamalıdır.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"

    def validate(self, paragraph: str):
        """
        Birden fazla cümle içeren metinde, noktalardan sonra gelen her cümle
        büyük harfle başlıyor mu diye kontrol eder.
        """
        sentences = paragraph.strip().split('.')
        for sentence in sentences[1:]:
            sentence = sentence.strip()
            if sentence:
                first_char = sentence[0]
                if not first_char.isupper():
                    raise PostPeriodCapitalizationError()
        return True

    def explain_rule(self):
        return (
            f"{self.name} paradigmasında, her noktalama işaretinden (.) sonra gelen "
            "ilk kelimenin baş harfi büyük harfle yazılmalıdır. Aksi halde bu, yazım "
            "kuralı ihlali sayılır ve programlama dili yorumlayıcısı bunu reddeder."
        )

# Örnek kullanım
if __name__ == "__main__":
    validator = PostPeriodCapitalizationValidator()
    print(validator.explain_rule())
    print()

    metin = "Dosyayı aç. yazdır ekrana. Kaydet belgeyi."

    try:
        validator.validate(metin)
        print("✅ Noktadan sonra büyük harf kuralı geçerli.")
    except PostPeriodCapitalizationError as e:
        print(f"❌ Hata: {e}")
# Ek test bölümü: Noktadan sonra büyük harf kontrolü
if __name__ == "__main__":
    validator = PostPeriodCapitalizationValidator()
    print("\n[Noktadan Sonra Büyük Harf Kuralı Testi]\n")

    metin1 = "Dosyayı aç. Yazdır ekrana. Kaydet belgeyi."  # ✅ Doğru
    metin2 = "Dosyayı aç. yazdır ekrana. Kaydet belgeyi."  # ❌ Hatalı

    try:
        validator.validate(metin1)
        print("✅ metin1: Noktadan sonra büyük harf kuralı geçerli.")
    except PostPeriodCapitalizationError as e:
        print(f"❌ metin1 Hata: {e}")

    try:
        validator.validate(metin2)
        print("✅ metin2: Noktadan sonra büyük harf kuralı geçerli.")
    except PostPeriodCapitalizationError as e:
        print(f"❌ metin2 Hata: {e}")



# ==============================
# EKLENEN KURALLAR (26-27 Haziran 2025)
# ==============================

# 1. Bağlaçlardan Önce/Sonra Noktalama Kullanılmaz
class ConjunctionPunctuationRule:
    """'ve', 'veya', 've de', 'ya da', 'ile' gibi bağlaçlardan önce ve sonra noktalama işareti kullanılmaz."""
    def explain_rule(self):
        return (
            "Bu paradigmanın yazım kurallarına göre:\n"
            "- 've', 'veya', 've de', 'ya da', 'ile' gibi bağlaçlardan ÖNCE veya SONRA\n"
            "  noktalama işareti (virgül, nokta, tire vb.) kullanılmaz.\n"
            "Örnek: Doğru → 'Kitabı aç ve oku.'\n"
            "        Yanlış → 'Kitabı aç, ve oku.'"
        )

# 2. Sıfatlardan Sonra Noktalama Kullanılmaz
class AdjectivePunctuationValidator:
    def __init__(self):
        self.sifatlar = [
            "büyük", "küçük", "hızlı", "yavaş", "uzun", "kısa", "açık", "kapalı",
            "kırmızı", "mavi", "yeşil", "güzel", "çirkin", "yeni", "eski", "zor", "kolay"
        ]
        self.noktalama = [",", ".", ";", ":", "–", "-", "—"]

    def validate(self, sentence: str):
        words = sentence.strip().split()
        for i, word in enumerate(words[:-1]):
            clean_word = word.strip(",.;:-–—").lower()
            next_word = words[i + 1]
            if clean_word in self.sifatlar and next_word[0] in self.noktalama:
                return False
        return True

# 3. Özne ile Yüklem Arasında Noktalama Kullanılmaz
class SubjectPredicateValidator:
    def __init__(self):
        self.noktalama = [",", ".", ";", ":", "–", "-", "—"]

    def validate(self, sentence: str):
        words = sentence.strip().split()
        for i in range(len(words) - 1):
            if words[i][-1] in self.noktalama:
                return False
        return True

# 4. Zarf ile Yüklem Arasında Noktalama Kullanılmaz
class AdverbPredicateValidator:
    def __init__(self):
        self.zarflar = [
            "hızlıca", "yavaşça", "sessizce", "dikkatlice", "sabırsızca",
            "aceleyle", "usulca", "nazikçe", "gürültülüce", "korkarak"
        ]
        self.noktalama = [",", ".", ";", ":", "–", "-", "—"]

    def validate(self, sentence: str):
        words = sentence.strip().split()
        for i, word in enumerate(words[:-1]):
            clean_word = word.strip(",.;:-–—").lower()
            next_word = words[i + 1]
            if clean_word in self.zarflar and next_word[0] in self.noktalama:
                return False
        return True

# 5. Sayı ile İsim Arasında Noktalama Kullanılmaz
class NumberNounValidator:
    def __init__(self):
        self.noktalama = [",", ".", ";", ":", "–", "-", "—"]

    def validate(self, sentence: str):
        words = sentence.strip().split()
        for i, word in enumerate(words[:-1]):
            if word[:-1].isdigit() and word[-1] in self.noktalama:
                return False
        return True

# 6. Sıralı Fiillerde Her Fiilden Sonra Nokta Kullanılır
class StrictMultiVerbValidator:
    def __init__(self):
        self.verb_list = {
            "aç", "oku", "yaz", "kaydet", "sil", "çalıştır", "hesapla", "gönder", "al",
            "çiz", "kopyala", "yapıştır", "yürü", "bekle", "koş", "kapat", "başlat"
        }

    def validate(self, sentence: str):
        clauses = [clause.strip() for clause in sentence.split('.') if clause.strip()]
        for clause in clauses:
            last_word = clause.lower().split()[-1]
            if last_word in self.verb_list:
                continue
            else:
                for word in clause.lower().split():
                    if word in self.verb_list:
                        return False
        return True

# 7. Bağlaçla Zincirlenen Emirler Ayrı Cümle Olmalı
class ImperativeVerbChainValidator:
    def __init__(self):
        self.baglaclar = ["ve", "veya", "ya da", "ve de"]
        self.verb_list = {
            "oku", "yaz", "kaydet", "gönder", "al", "aç", "çalıştır", "sil", "çiz",
            "yap", "yükle", "indir", "kopyala", "başlat", "durdur", "yeniden başlat"
        }

    def validate(self, sentence: str):
        words = sentence.strip().lower().split()
        for i in range(len(words) - 2):
            if words[i] in self.verb_list and words[i + 1] in self.baglaclar and words[i + 2] in self.verb_list:
                return False
        return True


# 📌 Birbiri ardınca sıralanan eş görevli kelime ve kelime gruplarının arasına virgül konur
"""
Örnek: Elma, armut, muz ve çilek aldım.
"""


# 📌 Sıralı cümleleri birbirinden ayırmak için virgül konur
"""
Örnek: Okula gittim, ders çalıştım, eve döndüm.
"""


# 📌 Programlama, hem nesir (düzyazı) şeklinde hem de madde işaretli biçimde yapılabilir
"""
Bu programlama paradigmasında kullanıcı, programını açıklayıcı paragraflar hâlinde yazabilir.
Ayrıca aynı programı madde madde, her adımı listeleyerek de yazabilir.

Örnek (Nesir Şeklinde):
Bu program kullanıcıdan yaşını alır, 18'den büyükse 'Yetişkin' der, değilse 'Çocuk' der.

Örnek (Madde İşaretli Şekilde):
- Kullanıcıdan yaş alınır
- Yaş > 18 ise 'Yetişkin' yazılır
- Aksi takdirde 'Çocuk' yazılır

"""



# 📌 Dosya Dönüştürme Programı - Söz Dizimi Biçimleri

"""
Aşağıda, İnsan Dilinde Ve Doğal Dilde Programlama Paradigması kapsamında
aynı programın hem nesir (düzyazı) hem de madde işaretli biçimle yazılmış hali sunulmuştur.
"""

# 🔹 Nesir (Düzyazı) Biçimi
"""
Bu bir dosya dönüştürme programıdır.
Bu program herhangi bir dosyanın formatını başka bir dosya formatına dönüştürmekle görevli olmaktadır.
Bu program bilgisayarlara ait bütün tüm işletim sistemlerine göre uyumludur ve ücretsiz bir programdır.
"""

# 🔹 Madde İşaretli Biçimi
"""
- Bu, bir dosya dönüştürme programıdır
- Herhangi bir dosyanın formatını başka bir dosya formatına dönüştürmekle görevlidir
- Bilgisayarlara ait bütün işletim sistemlerine uyumludur
- Ücretsiz bir programdır
"""



# 📘 Tanım: Nesir Nedir?

"""
Nesir, yani düzyazı, doğal konuşma biçimindeki sözlerin yazıya dökülmüş hâlidir.

- Şiir değildir.
- Ölçü, kafiye gibi kalıplara bağlı değildir.
- Yalnızca dilbilgisi (gramer) kurallarına uyar.
- Duygu, düşünce ve bilgileri serbestçe aktarır.

📌 Edebiyatta nesir; roman, hikâye, makale gibi düz yazı türlerinde görülür.
📌 Programlama paradigması açısından nesir; anlaşılır, serbest ve insan diline yakın ifadelerle kod yazılmasını ifade eder.
"""



# 🎮 Video Oyun Dosya Türleri – Madde Listesiyle Sözdizimi Açıklaması

"""
Bu programlama paradigmasında, video oyunlarına ait dosya türleriyle çalışırken madde halinde kodlama yapılması önerilir.
Bu, hem geliştiricinin hem de kullanıcının yazılanları kolayca anlamasını sağlar.

Aşağıdaki dosya türleri, İnsan Dilinde ve Doğal Dilde Programlama Paradigmasına uygun olarak işlenebilir:

- ROM Dosyaları: Oyun konsollarına özel çalıştırılabilir oyun içeriğidir
- ISO Dosyaları: Oyunların optik disk görüntü dosyalarıdır
- SWF Dosyaları: Flash tabanlı video oyunlarıdır
- APK Dosyaları: Android işletim sistemine özel oyun paketleridir
- IPA Dosyaları: iOS işletim sistemine ait oyun uygulamalarıdır
- JAR Dosyaları: Java tabanlı oyun dosyalarıdır

📌 Bu maddeler, kod yazımı sırasında hem söz dizimi açısından hem de anlam açısından düzenli bir yapı sağlar.
"""

# --- ikileme_validator.py ---

class IkilemePunctuationError(Exception):
    """İkilemelerin arasına noktalama işareti konulması durumunda fırlatılan hata."""
    def __init__(self, ikileme):
        super().__init__(f"'{ikileme}' ikilemesinin arasına noktalama işareti konulamaz!")

class IkilemePunctuationValidator:
    """
    Bu sınıf, İnsan Dilinde ve Doğal Dilde Programlama Paradigması'nda
    ikilemelerin arasına noktalama işareti konulup konulmadığını denetler.
    """

    def __init__(self):
        self.name = "İnsan Dilinde ve Doğal Dilde Programlama"
        self.ikilemeler = [
            "az çok", "eski yeni", "doğru yanlış", "iyi kötü", "bile bile", 
            "yavaş yavaş", "yine yine", "tek tek", "teker teker", 
            "içe içe", "dolu dolu", "ağır ağır", "karış karış"
        ]
        self.noktalama = [",", ".", ";", ":", "-", "–", "—"]

    def validate(self, sentence: str):
        for ikileme in self.ikilemeler:
            ilk, ikinci = ikileme.split()
            for punc in self.noktalama:
                if f"{ilk}{punc} {ikinci}" in sentence or f"{ilk} {punc}{ikinci}" in sentence:
                    raise IkilemePunctuationError(ikileme)
        return True


# Örnek kullanım
if __name__ == "__main__":
    validator = IkilemePunctuationValidator()
    test_sentences = [
        "Az çok anladım.",
        "İyi, kötü kararlar aldık.",
        "Yavaş yavaş ilerliyoruz.",
        "Dolu; dolu yaşıyorum hayatı."
    ]

    for sentence in test_sentences:
        print(f"Cümle: "{sentence}"")
        try:
            validator.validate(sentence)
            print("✅ Geçerli cümle.\n")
        except IkilemePunctuationError as e:
            print(f"❌ Hata: {e}\n")