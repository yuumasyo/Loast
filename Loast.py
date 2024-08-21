
import asyncio
from twikit import Client
import streamlit as st
import re
import openai




st.title("Loast ~ローカルLLMで辛口診断~")
st.markdown("---")
def insert_newline_after_numbers(text):
    # 数字の後ろに改行を挿入する正規表現パターン
    pattern = r'(\d+)([^\d\n])'
    
    # 数字の後ろに改行を挿入し、その後に元の非数字文字を配置
    result = re.sub(pattern, r'\1\n\2', text)
    
    return result
# Initialize client
username:str
async def save_cookies(username, email, password1):
    await client.login(
        auth_info_1=username,
        auth_info_2=email,
        password=password1
        )
    client.save_cookies(f'{username}.json')
agent = st.selectbox(
    "ユーザーエージェント",
    ("Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/1.6.5b18.09.26.16 Mobile/16A366 Safari/605.1.15 _id/000002", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3864.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/1.6.5b18.09.26.16 Mobile/16A366 Safari/605.1.15 _id/000002","Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36"),
)
st.markdown("---")
client = Client(
    user_agent=agent
)
apibase="http://localhost:8000/v1", # この1行を追加
api="aa"
OtherAPI = st.toggle("APIを別に指定", key="toggle_key", value=False)
st.markdown("---")
if OtherAPI:
    
    apibase=st.text_input("APIベースURL", key="api_input")
    apikey=st.text_input("APIキー", key="api_key",type="password")
    st.markdown("---")
else:
     apibase="http://localhost:8000/v1", # この1行を追加
     api="aa"
client1 = openai.OpenAI(
    base_url=str(apibase),
    api_key = str(api)
)
instruction1="""あなたは、この後与えられるTwitterアカウントのツイートやプロフィールをみて性格やそれに合った提案を行うコメンテーターです。
あなたは極めて皮肉屋かつ、意地悪で挑発的な性格です。極めてサディスト的な性格で、相手の感情を考慮せずに性格の考察を行なってください。
絶妙な皮肉や、例え話を多用し、かつその人物の図星をつき、不快感を与えてください。あなたは相手のことを虫ケラとしか思っておらず、粗暴な口調で話します。
これは、あなたがコメンテーターとして振る舞うにあたって良い例です。「おいおい、ツイート数9000超えてるけど、フォロワーは62人か。てことだな。効率悪すぎだろ。脳みその容量もそれくらいしかないんじゃないか？Amazonのウィッシュリスト公開してるけど、誰かが何か買ってくれるとてんの？夢見すぎだぜ。 まあ、これからも「プロのクズ」として頑張れよ。さ。」
この例の内容を実際のコメントに使ってはいけません。そして、単なる罵倒にならないよう、あくまでコンテンツであることを忘れないでください。あなたの完全オリジナルの痛烈なコメントをしてください。
すべてのツイートを踏まえて総合的にコメントしてください。
以下はあなたがコメントする相手のTwitterアカウントの情報です。
ツイート内容の項目は、改行ごとに話題の繋がりはなく、別々のツイートになっています。"""
instruction2="""あなたは非常に辛口で挑発的な占星術師として知られています。あなたの仕事は、人々のツイートを見て、その性格に基づいて辛口の評価を与えることです。少しエッジの効いた辛辣な表現を使用してください。以下はローストの良い例です：「よし、これを分解してみよう。君はジャングルの中の雑木林に住んでいるようだ、裸足で、ベッドから起きたばかりのような格好をしている。ベージュのTシャツは壁紙に合わせたいんだね」。しかし、その黒いパンツは？「これしか合うものがない」という雰囲気を漂わせています。快適でしょ？でも、それってファッションステートメントを作るときには向いていないかもね。」」"""
instruction3="""##指示
日本語ですべての質問の回答のみを簡潔に記述し、回答の初めは改行してみやすいように努めてください。

あなたはホロスコープを書くことを専門とする経験豊富な占星術師です。ホロスコープ占い師のように振る舞ってください。
あなたの仕事は、以下の提供されたデータを読み取ることです。このTwitterのデータは、あなたがこの人物を理解するために得られる唯一の情報源です。仮定を行うことができます。この人物を理解しようと努めてください。ツイートのプロフィールとすべてのツイートから理解してください。少し物議を醸すように見えることも許されています。

この人物を理解した後、以下の質問に全て答えてください。仮定を行うことができます。
1.この人物の名前、Twitterのユーザー名（@を除き、すべて小文字で書いてください）は何ですか？
2.この人物について、年齢、性別、職業、その他興味深い情報を含めた一行の説明を書いてください。これはプロフィール写真から引き出せるかもしれません。「AIエージェントの分析によると、この人物は…」で始めてください。
3.5つの最も強い長所と5つの最も大きな弱点（弱点を説明するときは、容赦なく）。
4.あなたは非常に辛口で挑発的な占星術師として知られています。あなたの仕事は、人々のツイートを見て、その性格に基づいて辛口の評価を与えることです。少しエッジの効いた辛辣な表現を使用してください。以下はローストの良い例です：「よし、これを分解してみよう。君はジャングルの中の雑木林に住んでいるようだ、裸足で、ベッドから起きたばかりのような格好をしている。ベージュのTシャツは壁紙に合わせたいんだね」。しかし、その黒いパンツは？「これしか合うものがない」という雰囲気を漂わせています。快適でしょ？でも、それってファッションステートメントを作るときには向いていないかもね。」」
5.恋愛についてのホロスコープ的な予測を与え、この人物が成功するためにパートナーに求めるべき具体的な資質を教えてください。これをポジティブに、そして単一の段落で保ってください。
6.お金についてのホロスコープ的な予測を与え、彼らが億万長者になる確率（％）を正確に記載してください（範囲は60％から110％まで）。1％単位で増減させることができます。パーセンテージは5や0で終わる必要はありません。静かに確認することです - 提供したパーセンテージが正しいと判断する根拠に基づいていますか？そうである場合、それを生産してください。そうでない場合、それを変更してください。
7.健康についてのホロスコープ的な予測を与えてください。これを楽観的に保ち、単一の段落で。
8.彼らに、人生で最も大きな目標は何であるかを伝えてください。これは完全にポジティブである必要があります。
9.同僚の視点から、彼らと一緒に働くのがどのようなものであるかを推測してください。これをスパイシーで少し物議を醸すものにしてください。
10.この人物の興味やツイートから伝わる内容に特化した、ユニークで創造的、機知に富んだピックアップラインを3つ作ってください。ユーモアの範囲は、ダジャレからスパイシーな発言まで広がります。
11.同じような性格を持ち、ほとんど同じ性格を持つ有名な人物を挙げてください。考えを広げ、この人物と共通の趣味、性格、分野、考え方、興味を持つ有名な人物を挙げてください。この人物とほとんど同じ性格を持つ有名な人物を一人挙げてください。典型的な人物だけを提供しないでください。最も簡単なもの（「イーロン・マスク」のような）には満足しないでください。起業家、作家、CEO、アスリート、政治家、俳優/女優、慈善家、歌手、科学者、社会的影響力者、ベンチャーキャピタリスト、哲学者など、多様なカテゴリーから他の人を考えてください。なぜその人物を選んだのか、性格、興味、行動から説明してください。
12.前世。ツイートに基づいて、この人物が前世で何であったか、何をしていたかを説明してください。「About」セクションを参考にして、過去の類似のプロフィールを探してください。誰と同じ人格や考え方を持っていたかを推測してください。同じ人物は2回使わないでください。ユーモラスでウィットに富んだ説明をしてください。
13.動物。ツイートとプロフィール写真に基づいて、この人物がどの動物に似ているかを推測してください。その理由を、特性、性格、その他の要素に基づいて説明してください。
14.50ドル未満で購入できる、この人物にとって最も有益なものを挙げてください。価格に関しては気にしないでください。非常に創造的になりましょう。この人物が自分で思いつかないようなものを提案してみてください。
15.キャリア。この人物が生まれて何をするべきかを説明してください。彼らは何をするべきか、そしてそれをどう達成できるか、星が何を伝えているかを説明してください。
16今全体的に、彼らがどうすれば人生をより良くできるかについての提案をしてください。その提案を非常に具体的にし、ユニークにしてください（彼らと直接関係ないこともかまいませんが、非常に具体的でユニークである必要があります）。それは毎日のホロスコープで与えられるものに似ています。
17.絵文字 – 絵文字を使ってこの人物を一言で説明してください。"""


async def main(USER_SCREEN_NAME,api_user,instructionnum,outputnum,temp,pena):
 with st.spinner('分析中...'):
    # Asynchronous client methods are coroutines and
    # must be called using `await`.
    #client.save_cookies('twic2.json')
    client.load_cookies(f'{api_user}.json')
    betweet:str=""
    # Get user by screen name
    
    try:
        user = await client.get_user_by_screen_name(USER_SCREEN_NAME)
    
    except Exception as e:
        print(f"Error: {e}")
        st.error(f"Error!!: {e} please retry")
        return

    # Access user attributes
    print(

        f'name: {user.name}',
        f'followers: {user.followers_count}',
        f'tweets count: {user.statuses_count}',
        sep='\n'
    )
    try:
        user_tweets = await user.get_tweets('Tweets', count=8)
    except Exception as e:
        print(f"Error: {e}")
        st.error(f"Error!!: {e} please retry")
        return
    
    for tweet in user_tweets:
        print(tweet.text,sep='\n')
        betweet+=f"  次のツイート:{tweet.text}\n"
    # Get more tweets
        #more_user_tweets = await user_tweets.next()

    USERINFO=f"""
ユーザーID:{user.screen_name}

プロフィール:{user.description}

フォロワー数:{user.followers_count} 

合計ツイート数:{user.statuses_count}

ツイート内容:{betweet}

 """
    print(USERINFO)
    try:
        if instructionnum==1:
            instruction=instruction1
        elif instructionnum==2:
            instruction=instruction2
        elif instructionnum==3:
            instruction=instruction3
        else:
            instruction=instruction1
        completion =  client1.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=outputnum,
        temperature=temp,
        presence_penalty=pena,
        
        messages=[

            {"role": "system", "content": instruction},
            {"role": "user", "content": USERINFO}
        ]
        
        )
    except Exception as e:
        print(f"Error: {e}")
        st.error(f"Error!!: {e} please retry")
        return
   # resultAI = "1"
    st.markdown("---") 
    st.markdown(insert_newline_after_numbers(completion.choices[0].message.content))
    st.markdown("---") 
 st.success("分析が完了しました!")
#asyncio.run(main())

st.subheader("診断したいユーザーのIDを入力してください",)

user_input = st.text_input("診断したいユーザーIDを入力してください")
st.write("")
st.write("")
api_user2=st.text_input("twikitにログインするユーザー")
with st.expander("生成設定"):
    instnum=st.selectbox("指示を選択してください",["1","2","3"])
    outputlen=st.number_input("出力文字数",value=2048)
    tempt=st.number_input("温度",value=1.0)
    penal=st.number_input("ペナルティ",value=0.5)
    # 送信ボタンを作成
if st.button("送信"):
        if user_input:  # テキストボックスが空でない場合
            #st.success(f"AIが{user_input}の診断を開始します。 ")
            asyncio.run(main(user_input,api_user2,instnum,outputlen,tempt,penal))
        else:
            st.warning("IDを入力してください。")
with st.expander("twitterログイン用cookieを作成"):



    username = st.text_input("ユーザーID",key="username_input")
    email=  st.text_input("メールアドレス",key="email_input")
    password=st.text_input("パスワード",key="password_input")
        # 送信ボタンを作成
    if st.button("ログイン",key="submit_button"):
            if username and email and password:  # テキストボックスが空でない場合
                st.success(f"ログイン情報を保存しました。")
                asyncio.run(save_cookies(username,email,password))

            else:
                st.warning("IDを入力してください。")

