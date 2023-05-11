# ----------------Info Developer-------------
# -Last Name : Lecheheb
# -First Name : Djaafar
# -Country : Algeria
# -Age : 26
# -Skills : Python - HTML - CSS - C
# -instagram : @ddos_attack_co
# ------------Fallowed Me for instagram-------


# pip install nltk
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from click import clear


def Sentiment_Analyzer(comment):
    # تحميل القاموسسث
    nltk.download("Brown Corpus") 
    # انواع القاموس
    # ----------------------------------------------------------------
    # WordNet: قاموس شامل يحتوي على معاني الكلمات وعلاقاتها اللغوية مثل الرموز والمرادفات والهجاء والمضادات والعلاقات الجزئية والعلاقات الأخرى.
    # CMU Pronouncing Dictionary: قاموس يحتوي على نطق الكلمات الإنجليزية المنطوقة، بما في ذلك المقاطع الصوتية والأنماط اللهجية.
    # SentiWordNet: قاموس يحتوي على تصنيفات المشاعر (الإيجابية والسلبية والمحايدة) للكلمات في اللغة الإنجليزية.
    # Brown Corpus: مجموعة من النصوص المكتوبة باللغة الإنجليزية التي تغطي مختلف المواضيع والأنواع اللغوية، وتستخدم لأغراض تحليل النصوص والتعلم الآلي.
    # ----------------------------------------------------------------

    # إنشاء محلل المشاعر
    sia = SentimentIntensityAnalyzer()
    #   تحليل التعليق السلبي او ايجابي
    negative_sentiment = sia.polarity_scores(comment)
    # النتيجة النهائية للتحليل
    if negative_sentiment['compound'] >=0: # اذا اكبر من 0 يعني اجيابي
        return True # يرجع صح
    else:#او
        return False # خطاء
    

def main():
    # طلب تعليق من المستخدم
    comment = input("Please enter your comment: ") 

    # فحص التعليق باستخدام دالة Sentiment_Analyzer
    if Sentiment_Analyzer(comment) == True:
        clear()
        # طباعة رسالة إيجابية إذا كان التعليق إيجابيًا
        print("This Comment is Positive")
    else:
        clear()
        # طباعة رسالة سلبية إذا كان التعليق سلبيًا
        print("This Comment is Negative")


main()