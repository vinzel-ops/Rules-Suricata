# Rules-Suricata

Repositori ini berisi koleksi besar aturan untuk sistem deteksi intrusi jaringan Suricata (IDS). Suricata adalah IDS jaringan sumber terbuka yang dapat mendeteksi berbagai ancaman, termasuk malware, eksploit, dan aktivitas berbahaya lainnya. Aturan kami dirancang untuk sangat efektif dalam mendeteksi serangan aplikasi web, khususnya dalam mendeteksi CVE terbaru.

> Repositori ini sangat dipengaruhi oleh repositori `nuclei-templates` oleh ProjectDiscovery.

## Penggunaan

`gabungkan.py` akan menggabungkan semua aturan menjadi satu file.

```python
python3 gabungkan.py --path=/path/to/rules
```

## Statistik Aturan Suricata

| Aturan | Jumlah |
| ------ | ------ |
| linux-structures.rules | 0 |
| CNVD | 0 |
| CVE | 0 |

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
