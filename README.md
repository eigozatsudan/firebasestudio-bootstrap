# React + FastAPI on Docker

このプロジェクトは、フロントエンドにReact、バックエンドにFastAPIを使用したWebアプリケーションを、Docker Composeを使ってコンテナ環境で実行するためのサンプルです。

## 🚀 1分で開始：Firebase Studio へのインポート

最も簡単な開始方法は、Firebase Studioに直接インポートすることです。

1. **[Firebase Studio Import](https://studio.firebase.google.com/import) を開く**
2. **Repository URL** に以下を貼り付けて **Import** をクリック：
```text
https://github.com/eigozatsudan/firebasestudio-bootstrap
```


3. **初回のみ：依存関係のインストール**
インポート完了後、Studio内のターミナルで以下のコマンドを実行します：
```bash
docker compose run --rm frontend npm install
```


4. **起動**
画面上部の **「Web」タブ** 内にある **"Hard restart"** ボタンをクリックして起動します。

---

## 🛠️ ローカル環境でのセットアップ

開発環境をローカルに構築する場合は、以下の手順に従ってください。

### 前提条件

* Docker / Docker Compose

### 手順

1. **リポジトリをクローン**
2. **フロントエンドの依存関係をインストール**
```bash
docker compose run --rm frontend npm install

```


3. **コンテナをビルドして起動**
```bash
docker compose up --build -d

```



---

## 🔄 Firebase Studio での操作（重要）

Firebase Studio 上でコンテナを制御する際は、**「Web」タブ**にある操作パネルを使用します。

* **初回起動:** 上記の `npm install` 完了後、画面上部の **「Web」タブ** を選択し、その中にある **"Hard restart"** ボタンをクリックしてください。
* **コンテナの再起動:**
1. Studio内のターミナルで `docker compose down` を実行。
2. **「Web」タブ** の **"Hard restart"** ボタンを再度クリックします。



## 🌐 アクセス方法

コンテナ起動後、以下の場所から各機能にアクセスできます。

* **Frontend (React):** Firebase Studio の **「Web」タブ** で直接確認できます。
* **Backend API:** 「Web」タブに表示されているURLの末尾に `/api/hello` を追加することでAPIにアクセスできます。

## 📂 ディレクトリ構成

```
.
├── backend         # バックエンド (FastAPI)
├── compose.yml     # Docker Compose 設定
├── frontend        # フロントエンド (React)
└── nginx.conf      # Nginx 設定

```