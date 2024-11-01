import streamlit as st
from PIL import Image

# タイトルを表示
st.title("複数画像アップロードアプリ")

# 複数の画像をアップロードするファイルアップローダー
uploaded_files = st.file_uploader("画像ファイルを選択してください（複数選択可）", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# ファイルがアップロードされた場合
if uploaded_files:
    # アップロードされた各ファイルについて処理
    for uploaded_file in uploaded_files:
        # 画像をPILで開く
        image = Image.open(uploaded_file)

        # 画像を表示
        st.image(image, caption=f"アップロードされた画像: {uploaded_file.name}", use_column_width=True)
    st.write("画像の表示が完了しました。")
    st.write("以下に要約を表示します。")