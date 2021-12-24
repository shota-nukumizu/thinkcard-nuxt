# Thinkcard-nuxtアプリ

アイデア共有アプリ「Thinkcard-nuxt」のバックエンドをDjango REST Frameworkで実装した。

フロントエンドはNuxtで動かした。Vueでも十分に構わなかったが、**Nuxtのほうが構造がシンプルで凝った設定を行う必要がなかった**のでNuxtを導入した。

Tailwind CSSをフロントエンド構築のために導入したかったが、Tailwindを使わなくても十分に良質なWEBデザインを構築できたのでnode-scss中心でフロントのデザインを完成させた。(一部不備が多少あるが...)

# 開発環境

* Windows11
* Python 3.10.0
* Django 3.2.9
* NuxtJS
* Django REST Framework

# 実行

```powershell
$ python manage.py runserver
```