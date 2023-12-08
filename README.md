# Rules-Suricata

Repositori ini berisi koleksi besar aturan untuk sistem deteksi intrusi jaringan Suricata (IDS). Suricata adalah IDS jaringan sumber terbuka yang dapat mendeteksi berbagai ancaman, termasuk malware, eksploit, dan aktivitas berbahaya lainnya. Aturan kami dirancang untuk sangat efektif dalam mendeteksi serangan aplikasi web, khususnya dalam mendeteksi CVE terbaru.

> Repositori ini sangat dipengaruhi oleh repositori `nuclei-templates` oleh ProjectDiscovery.

## Penggunaan

`main.py` akan menggabungkan semua aturan menjadi satu file.

```python
python3 main.py --path=/path/to/rules
```

## Statistik Aturan Suricata

| Aturan | Jumlah |
| ------ | ------ |
| linux-structures.rules | 16 |
| CNVD-2021.rules | 10 |
| CVE-2008.rules | 9 |
| CVE-2013.rules | 8 |
| sql-injection.rules | 6 |
| CNVD-2020.rules | 5 |
| miscellaneous.rules | 4 |
| CVE-2007.rules | 4 |
| CVE-2020.rules | 4 |
| CVE-2002.rules | 4 |

## To-Do

- [ ] Menambahkan lebih banyak aturan [cvnd](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/cvnd).
- [ ] Menambahkan lebih banyak aturan [cves](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/cves).
- [ ] Menambahkan lebih banyak aturan [default-logins](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/default-logins).
- [ ] Menambahkan lebih banyak aturan [miscellaneous](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/miscellaneous).
- [ ] Menambahkan lebih banyak aturan [vulnerabilities](https://github.com/projectdiscovery/nuclei-templates/tree/main/http/vulnerabilities).
- [ ] Menambahkan lebih banyak aturan `Malware`.
- [ ] Menambahkan `URL Reference`.
- [ ] Menambahkan lebih banyak aturan serangan aplikasi web (misalnya `SQL Injection`, `XSS`, dll).

## Kontributor

Anda dapat berkontribusi pada repositori ini dengan menambahkan aturan baru atau memperbarui aturan yang ada.

<p align="center">
<a href="https://github.com/vinzel-ops/Rules-Suricata/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vinzel-ops/Rules-Suricata&max=25">
</a>
</p>
