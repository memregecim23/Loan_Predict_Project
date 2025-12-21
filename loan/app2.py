import streamlit as st
import pandas as pd
import joblib

# Sayfa Ayarları
st.set_page_config(page_title="Banka Kredi Tahmin Sistemi", layout="wide")


# Modeli Yükleme
@st.cache_resource
def load_model():
    try:
        model = joblib.load('loan_model.pkl')
        return model
    except Exception as e:
        st.error(f"Model dosyası (loan_model.pkl) bulunamadı veya yüklenemedi: {e}")
        return None


model = load_model()

# Başlık
st.title("🏦 Banka Kredi Değerlendirme Sistemi")
st.markdown("Müşteri bilgilerini girerek kredi uygunluk durumunu analiz ediniz.")

# SIDEBAR (VERİ GİRİŞİ)
st.sidebar.header("Müşteri Bilgi Girişi")

with st.sidebar.form("loan_form"):
    # KULLANICI İSMİ
    customer_name = st.text_input("Müşteri Adı Soyadı", placeholder="Örn: Ahmet Yılmaz")

    st.markdown("---")
    st.subheader("📋 Kişisel Bilgiler")

    # Risk Score
    risk_score = st.number_input("Kredi Puanı", min_value=0, max_value=1900, value=1200)

    # Yıllık Gelir
    annual_income = st.number_input("Yıllık Gelir (TL)", min_value=0.0, value=150000.0, step=1000.0)

    # Çalışma Durumu
    emp_options = ["Bordrolu Çalışan", "İşsiz", "Serbest Meslek / Esnaf"]
    employment_input = st.selectbox("Çalışma Durumu", emp_options)

    st.markdown("---")
    st.subheader("⚙️ Finansal Veriler")

    # Age
    age = st.number_input("Yaş", min_value=18, max_value=100, value=30)

    # Credit Score(Bankanın oluşturduğu)
    credit_score = st.number_input("Banka İçi Skor", min_value=0, max_value=2000, value=650)

    # Experience
    experience = st.number_input("Deneyim Yılı", min_value=0, max_value=80, value=5)

    # Loan Amount
    loan_amount = st.number_input("Talep Edilen Kredi Miktarı", min_value=1000.0, value=50000.0, step=1000.0)

    # Loan Duration
    loan_duration = st.number_input("Vade (Ay)", min_value=1, max_value=360, value=24)

    # Monthly Debt Payments
    monthly_debt = st.number_input("Aylık Mevcut Borç Ödemeleri", min_value=0.0, value=2000.0, step=100.0)

    # Bankruptcy History
    bankruptcy_hist = st.number_input("İflas Geçmişi (Adet)", min_value=0, value=0)

    # Previous Loan Defaults
    prev_defaults = st.number_input("Önceki Kredi Temerrütleri (Adet)", min_value=0, value=0)

    # Length of Credit History
    credit_hist_len = st.number_input("Kredi Geçmişi Uzunluğu (Yıl)", min_value=0, value=5)

    # Total Assets
    total_assets = st.number_input("Toplam Varlıklar", min_value=0.0, value=100000.0, step=1000.0)

    # Monthly Income
    monthly_income = st.number_input("Aylık Gelir", min_value=0.0, value=12500.0, step=500.0)

    # Net Worth
    net_worth = st.number_input("Net Değer (Net Worth)", value=50000, step=1000)

    # Faiz Oranları
    base_interest = st.number_input("Taban Faiz Oranı (Örn: 0.05)", min_value=0.0, max_value=5.0, format="%.4f",
                                    value=0.05)
    interest_rate = st.number_input("Uygulanan Faiz Oranı (Örn: 0.08)", min_value=0.0, max_value=5.0, format="%.4f",
                                    value=0.08)

    # Monthly Loan Payment
    monthly_loan_pay = st.number_input("Hesaplanan Aylık Taksit", min_value=0.0, value=1500.0)

    # DTI Ratio
    dti_ratio = st.number_input("Borç/Gelir Oranı (DTI - Örn: 0.3)", min_value=0.0, format="%.4f", value=0.3)

    # EĞİTİM SEVİYESİ
    edu_options_tr = ["Lise", "Önlisans", "Lisans", "Yüksek Lisans", "Doktora"]
    education_input = st.selectbox("Eğitim Seviyesi", edu_options_tr, index=2)

    # Türkçe -> Model Encode Dönüşümü
    edu_map = {
        "Lise": 0,
        "Önlisans": 1,
        "Lisans": 2,
        "Yüksek Lisans": 3,
        "Doktora": 4
    }
    education_encoded = edu_map[education_input]

    submit_btn = st.form_submit_button("ANALİZİ BAŞLAT")

#SONUÇ ALANI

if submit_btn and model is not None:

    # İsim Gösterimi
    if customer_name:
        st.subheader(f"Sayın {customer_name}, Kredi Başvuru Analiziniz")
    else:
        st.subheader("Kredi Başvuru Analiz Sonuçları")

    # ÖZET BİLGİLER TABLOSU
    st.info("📊 Başvuru Özeti")

    summary_data = {
        "Müşteri": [customer_name if customer_name else "-"],
        "Yaş": [age],
        "Eğitim": [education_input],
        "Meslek Durumu": [employment_input],
        "Yıllık Gelir": [f"{annual_income:,.2f} TL"],
        "Talep Edilen Kredi": [f"{loan_amount:,.2f} TL"],
        "Vade": [f"{loan_duration} Ay"],
        "Kredi Skoru (Risk)": [risk_score],
        "Mevcut Borç": [f"{monthly_debt:,.2f} TL"]
    }

    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df, hide_index=True, use_container_width=True)

    # MODEL TAHMİNİ
    model_input = pd.DataFrame({
        'Age': [age],
        'CreditScore': [credit_score],
        'Experience': [experience],
        'LoanAmount': [loan_amount],
        'LoanDuration': [loan_duration],
        'MonthlyDebtPayments': [monthly_debt],
        'BankruptcyHistory': [bankruptcy_hist],
        'PreviousLoanDefaults': [prev_defaults],
        'LengthOfCreditHistory': [credit_hist_len],
        'TotalAssets': [total_assets],
        'MonthlyIncome': [monthly_income],
        'NetWorth': [net_worth],
        'BaseInterestRate': [base_interest],
        'InterestRate': [interest_rate],
        'MonthlyLoanPayment': [monthly_loan_pay],
        'TotalDebtToIncomeRatio': [dti_ratio],
        'Educationlevelencoded': [education_encoded]
    })

    try:
        prediction = model.predict(model_input)
        # Olasılık değeri
        try:
            probability = model.predict_proba(model_input)
            prob_score = probability[0][1] * 100
            has_proba = True
        except:
            has_proba = False

        st.markdown("### 🎯 Sonuç Değerlendirmesi")

        # Sonuç görselleştirme
        if prediction[0] == 1:
            st.success("✅ KREDİ ONAYLANDI")
            if has_proba:
                st.write(f"Bankamız kriterlerine göre krediniz **uygundur**. (Güven Skoru: %{prob_score:.2f})")
        else:
            st.error("❌ KREDİ REDDEDİLDİ")
            if has_proba:
                st.write(
                    f"Bankamız kriterlerine göre şu an için kredi **verilememektedir**. (Red Olasılığı: %{100 - prob_score:.2f})")

    except Exception as e:
        st.error(f"Tahminleme sırasında hata oluştu: {e}")