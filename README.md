# Whisper 文字起こしプロジェクト

## 概要

このプロジェクトは、OpenAIのWhisperモデルを使用して、音声ファイルの文字起こしを行うためのツールです。Apple Silicon搭載のMacに最適化されており、MLXフレームワークを利用しています。

## 特徴

- Apple Silicon (M1/M2/M3) チップに最適化
- 複数のWhisperモデルサイズに対応（tiny, base, small, medium, large）
- ローカルでの高速な文字起こし処理
- 柔軟なモデル選択（ローカル変換モデルまたはHugging Faceからのダウンロード）

## 前提条件

- macOS Monterey (12.0) 以降
- Apple Silicon搭載Mac（M1, M2, M3チップ）
- Python 3.10以上
- Homebrew
- Git

## セットアップ

1. リポジトリのクローン:
   ```
   git clone https://github.com/NishimuraTakuya-nt/whisper_trans.git
   cd whisper_trans
   ```

2. 必要なツールのインストール:
   ```
   brew install ffmpeg python@3.10 git
   ```

3. 仮想環境の作成とアクティベーション:
   ```
   python3 -m venv whisper_env
   source whisper_env/bin/activate
   ```

4. 依存関係のインストール:
   ```
   pip install --upgrade pip
   pip install mlx-whisper torch
   ```

5. サブモジュールの初期化と更新:
   ```
   git submodule update --init --recursive
   ```

## モデルの変換（オプション）

ローカルで最適化されたモデルを使用する場合、以下のコマンドでモデルを変換できます：

```
cd mlx-examples/whisper
python convert.py --torch-name-or-path [モデル名] --mlx-path ../../mlx_models/[モデル名] --dtype float16
cd ../..
```

利用可能なモデル名: tiny, base, small, medium, large-v1, large-v2, large-v3

例（largeモデルの場合）:
```
python convert.py --torch-name-or-path large-v3 --mlx-path ../../mlx_models/large-v3 --dtype float16
```

## 使用方法

1. 文字起こしの実行:
   ```
   python transcribe.py [音声ファイルのパス] [モデル名]
   ```

   例：
   ```
   python transcribe.py path/to/your/audio.mp3 mlx_models/large-v3
   ```

2. モデルの指定:
   - ローカルで変換したモデル: `mlx_models/[モデル名]`
   - Hugging Faceのモデル: モデル名のみ（例：`large-v3`）

## 注意事項

- 大きなモデル（medium, large）を使用する場合、十分なメモリと処理能力が必要です。
- 初回実行時、Hugging Faceからのモデルダウンロードに時間がかかる場合があります。
- 会社や組織で使用する場合は、適切なセキュリティポリシーを確認してください。
- 音声の録音・文字起こしを行う際は、必ず関係者の同意を得てください。

## トラブルシューティング

問題が発生した場合は、以下を確認してください：
- 仮想環境が正しくアクティベートされているか
- 必要なパッケージが全てインストールされているか
- ffmpegが正しくインストールされているか
- サブモジュールが正しく初期化されているか

詳細な手順やトラブルシューティングについては、[Notionドキュメント](https://aquatic-night-0f7.notion.site/Whisper-AI-ae3f181c86a84aeda121612386b62ba2)を参照してください。
