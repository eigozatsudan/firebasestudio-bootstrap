# React + FastAPI on Docker

このプロジェクトは、フロントエンドに **React**、バックエンドに **FastAPI** を使用したWebアプリケーションを、Docker Composeを使ってコンテナ環境で実行するためのサンプルテンプレートです。

## 🌟 Firebase Studio とは

**Firebase Studio** は、Googleが提供する次世代のクラウド開発環境です。ブラウザだけで、ローカル開発環境と遜色ないフルスタックの開発・テスト・プレビューが可能になります。

* **低スペックPCでも快適:** クラウド上で動作するため、手元のPCに負荷をかけずブラウザだけでサクサク開発できます。
* **無料で利用可能:** Googleアカウントがあれば、追加費用なしでワークスペースを作成可能です。

## 🚀 1分で開始：Firebase Studio へのインポート

最も簡単な開始方法は、Firebase Studioに直接インポートすることです。

1. **[Firebase Studio Import](https://studio.firebase.google.com/import) を開く**
2. **Repository URL** に以下を貼り付けて **Import** をクリック：
```text
https://github.com/eigozatsudan/firebasestudio-bootstrap

```


3. **初回のみ：依存関係のインストールとビルド**
インポート完了後、Studio内のターミナル（画面下部）で以下のコマンドを順番に実行します：
```bash
# 1. フロントエンドの依存関係をインストール
docker compose run --rm frontend npm install

# 2. 事前にイメージをビルド（Webタブでのフリーズを回避するため）
docker compose up --build -d

```


4. **起動確認**
ビルド完了後、画面上部の **「Web」タブ** 内にある **"Hard restart"** ボタンをクリックしてアプリケーションを表示します。

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

* **初回起動:** 上記の `npm install` および `up --build` 完了後、画面上部の **「Web」タブ** を選択し、その中にある **"Hard restart"** ボタンをクリックしてください。
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

**Q: なぜ事前にターミナルで `up --build` を行うのですか？**
A: 初回起動時はイメージのビルドに時間がかかります。Webタブの "Hard restart" だけでは、ビルド中に画面が固まった（フリーズした）ように見えることがあるため、あらかじめターミナルでビルドを完了させておくことでスムーズに起動できます。

**Q: なぜ Nginx が必要なのですか？**
A: Nginx はリバースプロキシとして動作します。パス（例: `/api/*` はバックエンドへ、それ以外はフロントエンドへ）に応じて適切なコンテナへリクエストを振り分けます。

**Q: CORS（Cross-Origin Resource Sharing）への対応はどうなっていますか？**
A: 本構成では **Nginx がすべてのリクエストを集約し、同一ドメイン・同一ポートとして各コンテナへ振り分ける**ため、ブラウザから見れば「同じ場所」への通信となります。そのため、複雑な CORS 設定を意識することなく開発が可能です。

**Q: フロントエンドにライブラリを追加した場合は？**
A: `frontend/package.json` を更新後、ターミナルで `npm install` コマンドを実行し、再度 "Hard restart" を行ってください。
