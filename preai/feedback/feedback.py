import sys

def analyze_video(filename):
    # ここに動画解析のロジックを記述
    # 例として、単純にファイル名を返す
    return f"解析結果: {filename}"

if __name__ == "__main__":
    filename = sys.argv[1]
    result = analyze_video(filename)
    print(result)
