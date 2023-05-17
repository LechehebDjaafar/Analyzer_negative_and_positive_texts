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
from googletrans import Translator


from pyarabic.araby import normalize_hamza, normalize_ligature, normalize_alef, strip_tashkeel

def darija_to_fusha(text):
    # التطبيع الأولي للنص لإزالة الأحرف المتشابهة
    text = normalize_hamza(text)
    text = normalize_ligature(text)
    text = normalize_alef(text)
    
    # إزالة التشكيل (الحركات) من النص
    text = strip_tashkeel(text)
    return text



def translate_arabic_to_english(text):
    # إنشاء كائن مترجم من Google Translate
    translator = Translator(service_urls=['translate.google.com'])
    
    # استخدام المترجم لترجمة النص من العربية إلى الإنجليزية
    translation = translator.translate(text, src='ar', dest='en')
    
    # إرجاع الترجمة المستلمة
    return translation.text


def Sentiment_Analyzer(comment):
    # تحميل القاموسسث
    nltk.download("WordNet") 
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
    try:
        
        negative_sentiment = sia.polarity_scores(translate_arabic_to_english(darija_to_fusha(comment) ))
        # النتيجة النهائية للتحليل
        if negative_sentiment['compound'] >=0: # اذا اكبر من 0 يعني اجيابي
            return True # يرجع صح
        else:#او
            return False # خطاء
    except:
        return -1 #
    

def main():
    # طلب تعليق من المستخدم
    comment = input("Please enter your comment: ") 

    # فحص التعليق باستخدام دالة Sentiment_Analyzer
    if Sentiment_Analyzer(comment) == True:
        clear()
        # طباعة رسالة إيجابية إذا كان التعليق إيجابيًا
        print("This Comment is Positive")
        print(f"\n {translate_arabic_to_english(comment)}")
    elif Sentiment_Analyzer(comment) == -1:
        clear()
        print("This Comment Error")
        print(f"\n {translate_arabic_to_english(comment)}")
    else:
        clear()
        # طباعة رسالة سلبية إذا كان التعليق سلبيًا
        print("This Comment is Nigatif")
        print(f"\n {translate_arabic_to_english(comment)}")
        print(f"\n {darija_to_fusha(comment)}")


main()