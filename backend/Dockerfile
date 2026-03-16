# 軽量なslimイメージでベースサイズを削減
FROM python:3.14-slim

# 非rootユーザーで実行（セキュリティ）
RUN groupadd --gid 1000 app && \
    useradd --uid 1000 --gid app --shell /bin/bash --create-home app

WORKDIR /app

# 依存関係を先にコピーしてレイヤーキャッシュを活用
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip check

# アプリケーションコードをコピー
COPY --chown=app:app . .

# コンテナ内のログをバッファリングしない（リアルタイム表示）
ENV PYTHONUNBUFFERED=1

# 非rootユーザーに切り替え
USER app

EXPOSE 8000

# ヘルスチェック（オーケストレーター用）
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/hello')" || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
