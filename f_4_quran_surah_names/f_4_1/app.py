from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    # List of Surah names from the Quran
    surah_names = [
        "Al-Fatiha", "Al-Baqarah", "Aal-E-Imran", "An-Nisa", "Al-Maidah", "Al-An'am",
        "Al-A'raf", "Al-Anfal", "At-Tawbah", "Yunus", "Hud", "Yusuf", "Ar-Ra'd",
        "Ibrahim", "Al-Hijr", "An-Nahl", "Al-Isra", "Al-Kahf", "Maryam", "Ta-Ha",
        "Al-Anbiya", "Al-Hajj", "Al-Mu'minun", "An-Nur", "Al-Furqan", "Ash-Shu'ara",
        "An-Naml", "Al-Qasas", "Al-Ankabut", "Ar-Rum", "Luqman", "As-Sajda", "Al-Ahzab",
        "Saba", "Fatir", "Ya-Sin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir", "Fussilat",
        "Ash-Shura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiya", "Al-Ahqaf", "Muhammad",
        "Al-Fath", "Al-Hujraat", "Qaf", "Adh-Dhariyat", "At-Tur", "An-Najm", "Al-Qamar",
        "Ar-Rahman", "Al-Waqia", "Al-Hadid", "Al-Mujadila", "Al-Hashr", "Al-Mumtahina",
        "As-Saff", "Al-Jumu'a", "Al-Munafiqun", "At-Taghabun", "At-Talaq", "At-Tahrim",
        "Al-Mulk", "Al-Qalam", "Al-Haaqqa", "Al-Ma'arij", "Nuh", "Al-Jinn", "Al-Muzzammil",
        "Al-Muddathir", "Al-Qiyama", "Al-Insan", "Al-Mursalat", "An-Naba", "An-Nazi'at",
        "Abasa", "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj",
        "At-Tariq", "Al-Ala", "Al-Ghashiya", "Al-Fajr", "Al-Balad", "Ash-Shams", "Al-Lail",
        "Ad-Duha", "Ash-Sharh", "At-Tin", "Al-Alaq", "Al-Qadr", "Al-Bayyina", "Az-Zalzala",
        "Al-Adiyat", "Al-Qaria", "At-Takathur", "Al-Asr", "Al-Humaza", "Al-Fil", "Quraish",
        "Al-Ma'un", "Al-Kawthar", "Al-Kafirun", "An-Nasr", "Al-Masad", "Al-Ikhlas", "Al-Falaq", "An-Nas"
    ]
    return render_template('index.html', surahs=surah_names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
