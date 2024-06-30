import mlx_whisper
import sys


def main():
    if len(sys.argv) < 2:
        print("使用方法: python transcribe.py <音声ファイルのパス> [モデル名]")
        return

    speech_file = sys.argv[1]
    model = "mlx-community/whisper-tiny"  # デフォルトモデル

    if len(sys.argv) > 2:
        model = sys.argv[2]

    print(f"モデル {model} を使用して文字起こしを開始します...")
    result = mlx_whisper.transcribe(speech_file, path_or_hf_repo=model)

    print("\n文字起こし結果:")
    print(result["text"])

    # 単語レベルのタイムスタンプを表示（オプション）
    if "segments" in result and result["segments"]:
        print("\n単語レベルのタイムスタンプ:")
        for word in result["segments"][0].get("words", []):
            print(f"{word['text']}: {word['start']:.2f}s - {word['end']:.2f}s")


if __name__ == "__main__":
    main()