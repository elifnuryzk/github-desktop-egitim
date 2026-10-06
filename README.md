# Arkadaş Panosu — GitHub Desktop Eğitimi

Herkesin kendini eklediği küçük bir Python programı. Amaç programın kendisi değil,
**GitHub Desktop ile clone, commit, push, pull, branch, pull request ve merge conflict** öğrenmek.

Çalıştırmak için:

```bash
python3 main.py
```

---

## Temel kavramlar

| Kavram | Ne demek? | GitHub Desktop'ta nerede? |
|---|---|---|
| **Repository (repo)** | Projenin klasörü + tüm geçmişi | Sol üst: *Current repository* |
| **Clone** | GitHub'daki repoyu bilgisayarına indirmek | *File → Clone repository* |
| **Commit** | Yaptığın değişikliğin "kaydı" (fotoğrafı) | Sol alttaki *Summary* kutusu + *Commit to ...* |
| **Push** | Commit'lerini GitHub'a göndermek | Üstte *Push origin* |
| **Pull** | Başkalarının commit'lerini bilgisayarına çekmek | Üstte *Fetch origin → Pull origin* |
| **Branch** | Ana koddan ayrılan paralel bir çalışma kolu | Üstte *Current branch* |
| **Pull Request (PR)** | "Benim branch'imi main'e ekler misiniz?" isteği | *Branch → Create pull request* |
| **Merge conflict** | İki kişi aynı satırı değiştirince çıkan çakışma | Desktop otomatik uyarır |

---

## Görevler

### Görev 1 — Clone
1. GitHub Desktop'ı aç, GitHub hesabınla giriş yap.
2. *File → Clone repository* → bu repoyu seç → *Clone*.
3. *Repository → Show in Finder/Explorer* ile klasörü aç, `python3 main.py` ile çalıştır.

### Görev 2 — İlk commit ve push (doğrudan main'e)
1. `arkadaslar.py` dosyasını aç, listeye kendi satırını ekle.
2. GitHub Desktop'a dön: sol tarafta değişikliği yeşil satır olarak göreceksin.
3. Summary kutusuna `Ali'yi listeye ekledim` gibi bir mesaj yaz → **Commit to main**.
4. **Push origin**'e bas.
5. GitHub sitesinde dosyaya bak, satırın orada mı?

> Biri senden önce push'ladıysa Desktop "önce pull yap" diyecek. **Pull origin**'e bas, sonra tekrar push'la.

### Görev 3 — Pull
1. Diğerleri de push'ladıktan sonra **Fetch origin** → **Pull origin**.
2. `python3 main.py` çalıştır, herkes panoda mı?

### Görev 4 — Branch + Pull Request
1. *Current branch → New branch* → adı: `ali-yeni-ozellik`.
2. `main.py`'de küçük bir değişiklik yap. Fikirler:
   - `BASLIK` yazısını değiştir
   - Her arkadaşın yanına bir emoji ekle
   - En sona "Bugünün tarihi" yazdır
3. Commit et → **Publish branch**.
4. **Create Pull Request** → GitHub sitesinde PR açılır, açıklama yaz.
5. Bir arkadaşın PR'ı incelesin ve **Merge** etsin.
6. Desktop'ta `main` branch'ine geç ve **Pull origin**.

### Görev 5 — Merge conflict (bilerek!)
1. İki kişi aynı anda `main.py` içindeki `BASLIK = "ARKADAŞ PANOSU"` satırını **farklı** şekilde değiştirsin.
2. Biri commit + push yapsın.
3. Diğeri commit yapıp pull etmeye çalışsın → **conflict!**
4. Desktop'ta *Open in editor* de. Dosyada şunu göreceksin:
   ```
   <<<<<<< HEAD
   BASLIK = "BENİM BAŞLIĞIM"
   =======
   BASLIK = "ONUN BAŞLIĞI"
   >>>>>>> origin/main
   ```
5. Hangisini istiyorsan onu bırak, `<<<<<<<`, `=======`, `>>>>>>>` satırlarını sil, kaydet.
6. Desktop'a dön → **Continue merge** → **Push origin**.

### Bonus
- *History* sekmesinde kim neyi ne zaman değiştirmiş bak.
- Bir commit'e sağ tıkla → *Revert changes in commit* ile geri al.
