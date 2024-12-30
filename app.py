from flask import Flask, render_template

app = Flask(__name__)

# Data structure with personalized messages, moments, and images
data = {
    "Lista": {
        "message": "MERRY CHRISTMAS AND HAPPY NEW YEAAAAAAAR! Thank you for being here for me in 2024 too, I know I'm not the easiest person to be around, but I'm grateful for your patience and understanding. Semangat terus buat segala urusan di tahun 2025 nanti termasuk urusan jaga kesehatan, jaga makan, skripsi, kerja, dan juga urusan mencintai Seungkwan! So happy u finally bakalan ketemu Seungkwan bentar lagiiiii. Semoga di 2025 nanti pun kita bakal tetep main terus yaa, me and seungkwan loves you, so please be healthy always!",
        "moment": "Baru nyadar kalo kita gaada foto bareng yang proper this year, jadi ini foto ini aja yaaa HAHAHAHAAH. Semoga next year bakal lebih banyak foto bareng yang proper!",
        "image": "Lista.jpg"
    },
    "Nayu": {
        "message": "HAPPY NEW YEAR SOBAT KAP!! Thank you for being around in the past 8 years! Jujur gue juga gak nyangka this friendship would last this long, despite being a low maintenance one. Semangat mencari pundi-pundi uang di tahun 2025 juga yaak, we all know kerja di Big4 Big4 ini demanding banget, so please jaga kesehatan jangan sampai tumbang! Semoga di tahun 2025 ini kita bisa ketemu lebih sering, dan bisa main bareng lagi! Semoga juga bisa ketemu sama calon jodoh masing-masing, aamiin. Once again, happy new year!",
        "moment": "Will always love all our jajan and makan moments together! Semoga bisa ketemu lagi dan jajan bareng lagi!",
        "image": "Nayu.jpg"
    },
    "Arooo": {
        "message": "Hi Aro, Happy New Year! Gimana kabarnya ro? Semoga sehat selalu. Thanks banget karena udah mau ngonser Bruno Mars barengan waktu itu, that was one of my 2024 highlights! Thanks juga waktu itu udah sempetin buat dateng ke arak-arakan aing di wispril, really appreciate it soalnya jadi berasa less lonely arak-arakannya! Semoga di tahun 2025 ini rezeki dan segala urusannya dilancarkan sama Allah ya, ro! Semoga proses ngerjain TA-nya juga lancar sampe lulus dari ITB, aamiin. Jangan lupa makan enak dan jaga kesehatan ya, semoga next time bisa main bareng lagi!",
        "moment": "Kita gaada foto bareng yg berdua gitu ya, jadi ini fotonya ini aja ya, aing nemu di folder dokum HIMAFI HAHAHAHAHA. Semoga bisa ketemu lagi dan foto bareng pas main bareng lagi!",
        "image": "Arooo.jpg"
    },
    "Ciciii": {
        "message": "Ciciiiii, Happy New Year! Thank you for being around ya ci, I know I'm not the easiest person to be friend with tapi thanks berat karena kamu selalu supportive sama aku. Selamat juga sudah berhasil menamatkan ITB. Semoga di tahun 2025 ini kita bisa ketemu lebih sering ya ci, dan bisa main bareng lagi! Semoga semua hal yang direncanakan untuk tahun 2025 ini bisa tercapai, ya cii, be it for your career or anything. Once again, happy new year and please send my warmest regards to Adit ya!",
        "moment": "Here's the prettiest cici, arak-arakan version! Semoga bisa ketemu lagi dan main bareng lagi!",
        "image": "Ciciii.jpg"
    },
    "Enjel": {
        "message": "Marry Christmas and Happy New Year, Enjeeeeel!!!! Terima kasih banyak ya njel soalnya kamu tuh selalu ada inisiatif buat ngajak kita-kita kumpul atau main, I seriously think you are the glue of this friendship. Gimana di kantor baru? Semoga lancar terus ya, dan semoga di tahun 2025 ini bisa lebih banyak jalan-jalan bareng lagi! Semoga juga bisa ketemu sama calon jodoh masing-masing, aamiin. Once again, happy new year!",
        "moment": "Disini kita cantik sekaliii meskipun ini line-up main tetap tahun ini dan agak mengecewakan ya heheh. Semoga bisa ketemu lagi dan main bareng lagi soon!",
        "image": "Enjel.jpg"
    },
    "Dinar": {
        "message": "SELAMAT TAHUN BARU DINAAAAAR!! Jujur masih gak nyangka kita bisa sedeket ini lagi di 2024! Makasih ya udah memotivasi gue buat olahraga HAHAHAHAHA semoga di 2025 kita makin konsisten olahraganya dan jadi lebih sehat! Semoga segala urusan lain juga dilancarkan di tahun baru ini dan semoga rezeki kita terus ngalir karena kita suka impulsive. Thank you for being around and happy new year, Din!",
        "moment": "Sejujurnya kita banyak bgt ketemu di 2024, tapi minim banget foto yang proper, jadi ini aja ya cakep pas dinner!",
        "image": "Dinar.jpg"
    },
    "Akmals": {
        "message": "Hi Akmaaaaals, Happy New Year ya maaals. Selamat sudah berhasil menamatkan ITB di 2024 ini. Semoga rezekinya semakin dilancarkan sama Allah di tahun 2025 ini, dan semoga bisa ketemu sama calon jodoh masing-masing, aamiin. Semoga juga bisa lebih sering main bareng lagi ya, maaals. Once again, happy new year!",
        "moment": "Sadly kita cuma ada foto ini pas aku wisudaaa, thank you ya mals udah nyempetin dateng ke arak-arakan wispril aku!",
        "image": "Akmals.jpg"
    },
    "Metha": {
        "message": "Happy New Year adik jahimku yang baru bonding pas aku udah lulus HAHAHAHA. Gimana tingkat akhirnya? semoga aman ya biar TA-nya lancar dan bisa cepetan kabur dari ITB. Semoga di tahun 2025 ini bisa lebih sering main bareng lagi ya, metha. Once again, happy new year!",
        "moment": "Inilah foto yang diambil karena bete soalnya hasil photoboxnya gembel banget di Row9 HAHAHAHAHAHAH",
        "image": "Metha.jpg"
    },
    "Daniel": {
        "message": "Merry Christmas & Happy New Year, Daniel! Selamat ya sobat mencengku sudah menamatkan matem ITB di 2024 ini. Semoga selalu sehat di 2025 dan bisa mencapai semua hal yang dipengenin, baik itu untuk karir atau hal lainnya. Ayolah kapan-kapan kita main bareng lagi, di citra 6 gitu yang deket HAHAHAHAH. once again, happy new year!",
        "moment": "Kita gaada foto bareng yang proper, jadi ini aja ya foto kita pas arak-arakan wispril! Makasih ya nil udah nyempetin dateng pas ituuu",
        "image": "Daniel.jpg"
    },
    "Evaaa": {
        "message": "MErry Christmas and Happy New Year, Evaaaa! Congrats for graduating and starting a new job too ya, Va! Semoga di tahun 2025 bisa mewujudkan semua impian dan harapan yang ada, baik itu untuk karir atau hal lainnya. Please be healthy ya, Va! Semoga juga bisa ketemu dan main bareng lagi. Once again, happy new year, Va!",
        "moment": "Here's gorgeous Eva, arak-arakan version! Semoga bisa ketemu lagi dan main bareng lagi!",
        "image": "Evaaa.jpg"
    },
    "Ucups": {
        "message": "Selamat tahun baru, Ucuup! Gimana nih kabarnya? Semoga sehat selalu ya, Ucup! Semoga di tahun 2025 ini kamu bisa achieve apapun yang kamu impikan. Tapi jangan lupa buat jaga kesehatan ya, Cup. Semoga bisa main bareng lagi ya kapan-kapan. Once again, happy new year and I'm wishing all the best for you!",
        "moment": "Ucup versi rapih pas arak-arakan wisuda! Semoga next time bisa ketemu lagi dan foto bareng lagi!",
        "image": "Ucups.jpg"
    }
}

@app.route('/')
def home():
    return "Hi guys, welcome to my personal greetings website! Webnya sangat amat seadanya karena ini lagi latihan aja, doain semoga bisa jadi webdev beneran ya. Happy New Year!"

@app.route('/<name>')
def greeting(name):
    # Fetch data for the given name
    name = name.strip().capitalize()
    person = data.get(name, {
        "message": "Happy New Year! Wishing you all the best this coming year!",
        "moment": "Here's to making new memories together!",
        "image": "default.jpg"  # Provide a default image
    })
    return render_template('greeting.html', name=name, message=person["message"], moment=person["moment"], image=person["image"])

if __name__ == '__main__':
    app.run(debug=True)
