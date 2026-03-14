# React + FastAPI on Docker

このプロジェクトは、フロントエンドに **React**、バックエンドに **FastAPI** を使用したWebアプリケーションを、Docker Composeを使ってコンテナ環境で実行するためのサンプルテンプレートです。

## 🌟 Firebase Studio とは

**Firebase Studio** は、Googleが提供する次世代のクラウド開発環境です。ブラウザだけで、ローカル開発環境と遜色ないフルスタックの開発・テスト・プレビューが可能になります。
本リポジトリは、この Firebase Studio 上で Docker 構成を即座に立ち上げられるよう最適化されています。

### 💳 料金と利用制限について

Firebase Studio は無料で利用可能ですが、[Google Developer Program](https://www.google.com/search?q=https://developers.google.com/community/dev-program) の参加状況によって作成できる「ワークスペース」の数が決まります。

* **基本利用:** 無料（Googleアカウントがあれば誰でも利用可能）
* **ワークスペースの上限:**
* **プログラム未参加:** 最大 **3つ** まで
* **Google Developer Program (無料版) 参加:** 最大 **10つ** まで
* **Google Developer Program (プレミアム) 参加:** 最大 **30つ** まで


* **注意点:** Firebase App Hosting などの一部機能を利用する場合は、Firebaseプロジェクトを Blaze プラン（従量課金）へアップグレードする必要がある場合があります。

## 🚀 1分で開始：Firebase Studio へのインポート

最も簡単な開始方法は、Firebase Studioに直接インポートすることです。

1. **[Firebase Studio Import](https://studio.firebase.google.com/import) を開く**
2. **Repository URL** に以下を貼り付けて **Import** をクリック：
```text
https://github.com/eigozatsudan/firebasestudio-bootstrap

```


3. **初回のみ：依存関係のインストール**
インポート完了後、Studio内のターミナル（画面下部）で以下のコマンドを実行します：
```bash
docker compose run --rm frontend npm install

```


4. **起動**
画面上部の **「Web」タブ** 内にある **"Hard restart"** ボタンをクリックして起動します。

---

## 🛠️ ローカル環境でのセットアップ

PCローカルに構築する場合は、以下の手順に従ってください。

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
├── .nix            # Firebase Studio 環境設定 (Nix shells)
├── backend         # バックエンド (FastAPI)
├── compose.yml     # Docker Compose 設定
├── frontend        # フロントエンド (React)
└── nginx.conf      # Nginx 設定

```

---

## ❓ FAQ

**Q: なぜ Nginx が必要なのですか？**
A: Nginx はリバースプロキシとして動作します。パス（例: `/api/*` はバックエンドへ、それ以外はフロントエンドへ）に応じて適切なコンテナへリクエストを振り分ける役割を担っています。

**Q: CORS（Cross-Origin Resource Sharing）への対応はどうなっていますか？**
A: 本構成では **Nginx がすべてのリクエストを集約し、同一ドメイン・同一ポートとして各コンテナへ振り分ける**ため、ブラウザから見れば「同じ場所」への通信となります。そのため、複雑な CORS 設定を意識することなく開発が可能です。

**Q: なぜ Firebase Studio で "Hard restart" が必要なのですか？**
A: Firebase Studio の環境で Docker Compose の設定変更を確実に反映させ、プレビューURLとコンテナを正しく同期させるために必要です。

**Q: フロントエンドにライブラリを追加した場合は？**
A: `frontend/package.json` を更新後、ターミナルで `docker compose run --rm frontend npm install` を実行し、再度 "Hard restart" を行ってください。

**Q: バックエンドのコードを変更しても反映されません。**
A: FastAPI はホットリロード設定（`--reload`）で起動していますが、依存関係（`requirements.txt`）などを変更した場合は、`docker compose up --build` を実行してイメージを再構築する必要があります。