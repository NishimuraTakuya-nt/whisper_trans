# Whisper文字起こしプロジェクト

このプロジェクトは、MLXを使用してWhisper AIモデルによる音声の文字起こしを行うためのツールです。Apple Silicon搭載Macに最適化されています。

## 前提条件

- macOS Monterey (12.0) 以降
- Apple Silicon搭載Mac（M1, M2, M3チップ）推奨
- Python 3.10以上
- Homebrew
- ffmpeg

## セットアップ

1. 必要なツールのインストール:
   ```
   brew install ffmpeg python@3.10 git
   ```

2. 仮想環境の作成とアクティベーション:
   ```
   python -m venv whisper_env
   source whisper_env/bin/activate
   ```

3. リポジトリをクローン:
   ```
   git clone https://github.com/your-username/whisper-transcription-project.git
   cd whisper-transcription-project
   ```
   
4. 依存関係のインストール:
   ```
   pip install --upgrade pip
   pip install mlx-whisper
   ```

## 使用方法

1. 文字起こしの実行:
   ```
   python transcribe.py path/to/your/audio/file.mp3 [モデル名]
   ```

   モデル名は省略可能です。デフォルトは "mlx-community/whisper-tiny" です。

2. 利用可能なモデル:
   - mlx-community/whisper-tiny
   - mlx-community/whisper-base
   - mlx-community/whisper-small
   - mlx-community/whisper-medium
   - mlx-community/whisper-large-v3

## 注意事項

- 大きなモデルを使用する場合、初回実行時にモデルのダウンロードに時間がかかる場合があります。
- モデルサイズが大きいほど、より多くのメモリと処理時間を必要としますが、精度が向上する可能性があります。
- 会社や組織でこのツールを使用する場合は、適切なセキュリティポリシーを確認してください。
- 録音を行う際は、必ず参加者全員の同意を得てください。

## トラブルシューティング

問題が発生した場合は、以下を確認してください：
- 仮想環境が正しくアクティベートされているか
- 必要なパッケージが全てインストールされているか
- ffmpegが正しくインストールされているか
- 十分なメモリがあるか（特に大きなモデルを使用する場合）
