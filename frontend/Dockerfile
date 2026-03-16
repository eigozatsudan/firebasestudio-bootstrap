# 軽量なAlpineイメージでベースサイズを削減
FROM node:24-alpine

WORKDIR /app

# 依存関係を先にコピーしてレイヤーキャッシュを活用
COPY package.json package-lock.json* ./
RUN npm ci

# アプリケーションコードをコピー
COPY . .

# compose の volume (./frontend:/app) 利用時に npm install が書けるよう root で実行
EXPOSE 5173

# ヘルスチェック（オーケストレーター用）
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD node -e "require('http').get('http://127.0.0.1:5173/', (r) => process.exit(r.statusCode === 200 ? 0 : 1)).on('error', () => process.exit(1))"

CMD ["npm", "run", "dev", "--", "--port", "5173", "--host", "0.0.0.0"]
