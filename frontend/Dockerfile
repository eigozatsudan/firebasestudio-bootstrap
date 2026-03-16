# 軽量なAlpineイメージでベースサイズを削減
FROM node:24-alpine

# 非rootユーザーで実行（セキュリティ）
RUN addgroup --system --gid 1000 app && \
    adduser --system --uid 1000 --ingroup app --no-create-home app

WORKDIR /app

# 依存関係を先にコピーしてレイヤーキャッシュを活用
COPY package.json package-lock.json* ./
RUN npm ci

# アプリケーションコードをコピー
COPY --chown=app:app . .

USER app

EXPOSE 5173

# ヘルスチェック（オーケストレーター用）
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD node -e "require('http').get('http://127.0.0.1:5173/', (r) => process.exit(r.statusCode === 200 ? 0 : 1)).on('error', () => process.exit(1))"

CMD ["npm", "run", "dev", "--", "--port", "5173", "--host", "0.0.0.0"]
