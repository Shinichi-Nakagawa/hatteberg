hatteberg
=================

PyCon JP 2015「野球Hack~Pythonを用いたデータ分析と可視化」のデモです。Retrosheetを利用しています。

## Description

メジャーリーグの試合・イベントデータ、「RETROSHEET」のデータを元に、野球データを分析・可視化するためのライブラリ群です。

DatabaseをDockerコンテナ上に構築（migrationにはpy-retrosheetを使用）、Jupyter notebookからデータの分析・可視化を行います。

このプロジェクトには、

 * MySQL 5.7 Server(Docker container, docker-composeを使って立ちあげ）
 * py-retrosheet(サブモジュール)
 * retrosheet用ライブラリ(pandasおよびSQLAlchemyメインで開発)
 * 分析サンプル(Joey Votto, Jon Lester, Hideki Matsui)
 
上記の役割を果たすコードが含まれています。

## Demo

このプロジェクトを用いてできる事は以下のスライドおよび動画を参照ください。

なお、含まれているのはMLBの分析例(Jon Lester, Joey Votto)のみです。

### スライド

http://www.slideshare.net/shinyorke/hackpython-pyconjp

### YouTube

https://youtu.be/MBAh5qE57Hs?t=8m51s

## 推奨環境

作者が保証するのはMac OS XおよびLinuxのみ。


 * Mac OS X v10.10(Yosemite)以上 ※10.11(El Capitan)での動作確認済み
 * Ubuntu 14.04 LTS(64bit)

WindowsおよびLinuxの他Distributionは未検証ですがMac/Ubuntu(Debian)依存の処理は無いため動くと思われます。


## Requirement

このプロジェクトを適用する際は以下のアプリケーション・ライブラリが必要となります。

プロジェクトをCloneする前にご準備願います。

Python 3.5が対話モードで起動&Dockerでのコンテナ起動・停止まで出来ればOKです。

 * Python 3.5.x ※Python 2.x未サポート、py-retrosheet(高速Ver.)を使うため3.5以上必須
 * Docker Toolbox https://www.docker.com/docker-toolbox
 
PythonのインストールおよびDockerのインストール・設定は公式サイト等を参照ください。
 
## Usage
 
### MySQL Server 設定&起動
 
docker-compose.ymlを開き、MySQLのデータベース、ユーザー設定をしてください。

     environment:
       MYSQL_ROOT_PASSWORD: your_root_password
       MYSQL_DATABASE: retrosheet
       MYSQL_USER: app_user
       MYSQL_PASSWORD: your_password

 
プロジェクトルート(cloneした元directory、docker-compose.ymlがある所)で以下のコマンドを実行してください。
 
     docker-compose up -d
 
### スキーマ&Index作成

スキーマはpy-retrosheetのsqlを利用して作成してください。

     mysql -u root -p {データベース名} < ./py-retrosheet/sql/schema.sql

Indexはretrosheet_appのsqlを使ってください。

     mysql -u root -p {データベース名} < ./retrosheet_app/sql/create_index.sql

### データ取得とデータベース作成

#### 1.ライブラリのインストール(py-retrosheet)

     cd py-retrosheet
     pip install -r requirements.txt


#### 2.MySQLコネクタのインストール

好きなコネクタでOKですが、推奨はPyMySQLです。

     pip install PyMySQL


#### 3.設定ファイル作成

config.iniをコピーして作成してください。

     cp scripts/config.ini.dist scripts/config.ini

以下のとおりconfig.iniを設定。

     [database]
     engine = mysql+pymysql     # mysql+{コネクタ名}
     host = 192.168.99.100      # Docker HOSTのIP、 docker-machine ip defaultの値
     database = retrosheet      # docker-compose.ymlのMYSQL_DATABASEと同じ値
     schema = retrosheet        # docker-compose.ymlのMYSQL_DATABASEと同じ値
     user = app_user            # docker-compose.ymlのMYSQL_USERと同じ値
     password = your_password   # docker-compose.ymlのMYSQL_PASSWORDと同じ値


#### 4.データ取得と作成

-fで開始年、-tで終了年を指定。サンプル起動には2009-2014年のデータが必要です。

ネットの混み具合・環境によりますが、サンプル用データ作成は10~20分程度かかります。

     cd scripts
     python migration.py -f 2009 -t 2014    # 開始と終了は好きな年でOK

### Jupyter notebook起動と分析・可視化

#### 1. ライブラリのインストール

     cd retrosheet_app
     pip install -r requirements.txt


#### 2. 設定ファイル作成

     cp config.ini.example config.ini

以下のとおりconfig.iniを設定。

     [mysql]
     encoding=utf-8             # そのまま
     dialect=mysql              # そのまま
     driver=pymysql             # 使いたいコネクタ（推奨pymysql）
     user=app_user              # docker-compose.ymlのMYSQL_USERと同じ値
     password=your_password     # docker-compose.ymlのMYSQL_PASSWORDと同じ値
     host=192.168.99.100        # Docker HOSTのIP、 docker-machine ip defaultの値
     port=3306                  # そのまま
     database=retrosheet        # docker-compose.ymlのMYSQL_DATABASEと同じ値


#### 3. Jupyter notebook起動

あとは好きにnotebookを使ったりあそんだりましょう！

    jupyter notebook

## License

MIT License http://opensource.org/licenses/MIT

## 問い合わせ・質問・Support（特にデータとライブラリの解説）

徐々に準備する予定ですが、問い合わせ等はこちらまで。

Shinichi Nakagawa <spirits.is.my.rader@gmail.com>

Twitter: @shinyorke
