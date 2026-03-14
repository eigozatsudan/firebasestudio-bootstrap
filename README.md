# React + FastAPI on Docker

このプロジェクトは、フロントエンドにReact、バックエンドにFastAPIを使用したWebアプリケーションを、Docker Composeを使ってコンテナ環境で実行するためのサンプルです。
Nginxがリバースプロキシとして機能し、フロントエンドとバックエンドへのリクエストを振り分けます。

## 概要

*   **Frontend:** React (Vite)
*   **Backend:** Python (FastAPI)
*   **Reverse Proxy:** Nginx
*   **Containerization:** Docker, Docker Compose

## 前提条件

*   Docker
*   Docker Compose

## セットアップ

1.  **リポジトリをクローンします。**

2.  **フロントエンドの依存関係をインストールします。**
    `package.json` を編集して新しいライブラリを追加した場合など、依存関係を更新する必要があります。
    以下のコマンドを実行してください。

    ```bash
    docker compose run --rm frontend npm install
    ```

3.  **コンテナをビルドして起動します。**
    初回起動時や `Dockerfile` を変更した場合は `--build` オプションを付けてください。

    ```bash
    docker compose up --build
    ```

    バックグラウンドで実行する場合は `-d` オプションを追加します。

    ```bash
    docker compose up --build -d
    ```

## Firebase Studioでの起動と再起動

**初回起動時:**

Webプレビューの "Hard restart" ボタンをクリックして、コンテナを起動します。

**再起動時:**

1.  ターミナルで以下のコマンドを実行して、現在のコンテナを停止します。

    ```bash
    docker compose down
    ```

2.  Webプレビューの "Hard restart" ボタンをクリックして、コンテナを再起動します。

## アクセス

コンテナが起動すると、Firebase StudioのWebプレビューにアプリケーションが表示されます。

*   **Frontend:** Webプレビューで直接確認できます。
*   **Backend API:** WebプレビューのURLに `/api/hello` を追加することで、バックエンドAPIにアクセスできます。

## ディレクトリ構成

```
.
├── backend         # バックエンド (FastAPI)
├── compose.yml     # Docker Compose 設定
├── frontend        # フロントエンド (React)
└── nginx.conf      # Nginx 設定
```
