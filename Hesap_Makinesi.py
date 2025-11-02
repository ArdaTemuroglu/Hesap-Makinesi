import math


def hesap_makinesi():
    işlemler = ["+", "-", "*", "/", "//", "%", "**", "kök", "log",
                "sin", "cos", "tan", "cot", "sec", "csc",
                "faktöriyel", "gcd", "lcm", "abs", "yuvarla"]

    def işlem_seç():
        print("Hesap Makinesine Hoşgeldiniz!")
        print("Yapmak istediğiniz işlemi seçiniz.")

        seçim = input("Toplama (+), Çıkarma (-), Çarpma (*), Bölme (/), "
                      "Kalansız Bölme (//), Bölümden Kalan (%) , Üs (**), "
                      "Kök Alma (kök), Logaritma (log), Sinüs (sin), "
                      "Kosinüs (cos), Tanjant (tan), Kotanjant (cot), "
                      "Sekant (sec), Kosekant (csc), Faktöriyel (faktöriyel), "
                      "EBOB (gcd), EKOK (lcm), Mutlak Değer (abs), "
                      "Yuvarlama (yuvarla): ")

        if seçim in işlemler:
            return seçim
        else:
            print("Geçersiz işlem. Lütfen tekrar deneyiniz.")
            return işlem_seç()   # burada return çok önemli
    seçim = işlem_seç()

    def sayı_seç(seçim):
        if seçim in ["kök", "sin", "cos", "tan", "cot", "sec",
                     "csc", "faktöriyel", "abs", "yuvarla"]:
            while True:
                try:
                    sayı1 = float(input("Bir sayı giriniz: "))
                    sayı2 = None
                    return sayı1, sayı2
                except ValueError:
                    print("Geçersiz giriş. Lütfen geçerli bir sayı giriniz.")
                    continue
        elif seçim in ["+", "-", "*", "/", "//", "%", "**", "log", "gcd", "lcm"]:
            while True:
                try:
                    sayı1 = float(input("Birinci sayıyı giriniz: "))
                    sayı2 = float(input("İkinci sayıyı giriniz: "))
                    return sayı1, sayı2
                except ValueError:
                    print("Geçersiz giriş. Lütfen geçerli bir sayı giriniz.")
                    continue

    sayı1, sayı2 = sayı_seç(seçim)

    def işlem_yap(seçim, sayı1, sayı2):
        if seçim == "+":
            print(f"{sayı1} + {sayı2} = {sayı1 + sayı2}")
        elif seçim == "-":
            print(f"{sayı1} - {sayı2} = {sayı1 - sayı2}")
        elif seçim == "*":
            print(f"{sayı1} * {sayı2} = {sayı1 * sayı2}")
        elif seçim == "/":
            if sayı2 != 0:
                print(f"{sayı1} / {sayı2} = {sayı1 / sayı2}")
            else:
                print("Hata: Bir sayı sıfıra bölünemez.")
                sayı_seç()
        elif seçim == "//":
            if sayı2 != 0:
                print(f"{sayı1} // {sayı2} = {sayı1 // sayı2}")
            else:
                print("Hata: Bir sayı sıfıra bölünemez.")
                sayı_seç()
        elif seçim == "%":
            if sayı2 != 0:
                print(f"{sayı1} % {sayı2} = {sayı1 % sayı2}")
            else:
                print("Hata: Bir sayı sıfıra bölünemez.")
                sayı_seç()
        elif seçim == "**":
            print(f"{sayı1} ** {sayı2} = {sayı1 ** sayı2}")
        elif seçim == "sin":
            print(f"sin({sayı1}) = {math.sin(math.radians(sayı1))}")
        elif seçim == "cos":
            print(f"cos({sayı1}) = {math.cos(math.radians(sayı1))}")
        elif seçim == "kök":
            while True:
                kök_derecesi = int(
                    input("Kök derecesini giriniz (örneğin karekök için 2): "))
                if kök_derecesi > 1:
                    if kök_derecesi % 2 == 0 and sayı1 < 0:
                        print(
                            "Hata: Çift dereceli kökler negatif sayılar için tanımsızdır.")
                        continue
                    else:
                        print(
                            f"{sayı1} sayısının {kök_derecesi}. dereceden kökü = {sayı1 ** (1 / kök_derecesi)}")
                        break
                else:
                    print(
                        "Kök derecesi 1'den büyük olmalıdır. Lütfen tekrar deneyiniz.")
                    continue
        elif seçim == "log":
            while True:
                if sayı1 > 0 and sayı2 > 0 and sayı2 != 1:
                    print(
                        f"{sayı2} tabanında logaritma {sayı1} = {math.log(sayı1, sayı2)}")
                    break
                else:
                    print(
                        "Hata: Logaritma tabanı pozitif ve 1'den farklı ve logaritma üssü 0'dan büyük olmalıdır. Lütfen tekrar deneyiniz.")
                    sayı1, sayı2 = sayı_seç("log")
                    continue
        elif seçim == "faktöriyel":
            while True:
                if sayı1 >= 0 and sayı1.is_integer():
                    print(f"{int(sayı1)}! = {math.factorial(int(sayı1))}")
                    break
                else:
                    print(
                        "Hata: Faktöriyel negatif veya tam sayı olmayan sayılar için tanımsızdır.")
                    sayı1, sayı2 = sayı_seç("faktöriyel")
                    continue
        elif seçim == "tan":
            while True:
                rad = math.radians(float(sayı1))
                cosv = math.cos(rad)
                if math.isclose(cosv, 0.0, abs_tol=1e-12):
                    print(
                        "Hata: tan(x) tanımsızdır (cos(x)=0). Lütfen farklı bir açı giriniz.")
                    sayı1, sayı2 = sayı_seç("tan")
                    continue
                else:
                    print(f"tan({sayı1}) = {math.tan(rad)}")
                    break
        elif seçim == "cot":
            while True:
                rad = math.radians(float(sayı1))
                sinv = math.sin(rad)
                if math.isclose(sinv, 0.0, abs_tol=1e-12):
                    print(
                        "Hata: cot(x) tanımsızdır (sin(x)=0). Lütfen farklı bir açı giriniz.")
                    sayı1, sayı2 = sayı_seç("cot")
                    continue
                else:
                    print(f"cot({sayı1}) = {math.cos(rad) / sinv}")
                    break
        elif seçim == "abs":
            print(f"|{sayı1}| = {abs(sayı1)}")
        elif seçim == "round":
            print(f"({sayı1}) sayısının yuvarlanmış hali  = {round(sayı1)}")
        elif seçim == "sec":
            while True:
                rad = math.radians(float(sayı1))
                cosv = math.cos(rad)
                if math.isclose(cosv, 0.0, abs_tol=1e-12):
                    print(
                        "Hata: sec(x) tanımsızdır (cos(x)=0). Lütfen farklı bir açı giriniz.")
                    sayı1, sayı2 = sayı_seç("sec")
                    continue
                else:
                    print(f"sec({sayı1}) = {1 / cosv}")
                    break
        elif seçim == "csc":
            while True:
                rad = math.radians(float(sayı1))
                sinv = math.sin(rad)
                if math.isclose(sinv, 0.0, abs_tol=1e-12):
                    print(
                        "Hata: csc(x) tanımsızdır (sin(x)=0). Lütfen farklı bir açı giriniz.")
                    sayı1, sayı2 = sayı_seç("csc")
                    continue
                else:
                    print(f"csc({sayı1}) = {1 / sinv}")
                    break
        elif seçim == "gcd":
            while True:
                if sayı1.is_integer() and sayı2.is_integer():
                    print(
                        f"{int(sayı1)} ve {int(sayı2)} sayılarının EBOB'u = {math.gcd(int(sayı1), int(sayı2))}")
                    break
                else:
                    print("EBOB sadece tam sayılar için tanımlıdır.")
                    sayı1, sayı2 = sayı_seç("gcd")
                    continue
        elif seçim == "lcm":
            while True:
                if sayı1.is_integer() and sayı2.is_integer():
                    def lcm(a, b):
                        return abs(a * b) // math.gcd(a, b)
                    print(
                        f"{int(sayı1)} ve {int(sayı2)} sayılarının EKOK'u = {lcm(int(sayı1), int(sayı2))}")
                    break
                else:
                    print("EKOK sadece tam sayılar için tanımlıdır.")
                    sayı1, sayı2 = sayı_seç("lcm")
                    continue

    def devam_durumu():
        devam = input("Başka bir işlem yapmak ister misiniz? (E/H): ")
        if devam.lower() == "e":
            hesap_makinesi()
        elif devam.lower() == "h":
            print("Hesap makinesini kullandığınız için teşekkürler!")
            print("Program sonlandırılıyor...")
        else:
            print("Geçersiz giriş. Lütfen E, H, e veya h giriniz.")
            devam_durumu()

    işlem_yap(seçim, sayı1, sayı2)
    devam_durumu()


hesap_makinesi()
